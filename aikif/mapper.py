# mapper.py     written by Duncan Murray 21/10/2014


import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder)
print('mapper, root_folder = ', root_folder)
import aikif.agents.agent as agt

import cls_log as mod_log
import config as mod_cfg

map_file = root_folder + os.sep + 'data' + os.sep +  'ref' + os.sep + 'mapping_rules.csv'

  
class Mapper:    
    """
    Main class to map input information to aikif data structures
    based on a mapping table
    """
    
    def __init__(self):
        """
        setup that reads the table
        """
        self.load_rules()

    def __str__(self):
        res = ' -- List of Mapping Business Rules -- \n'
        for map in self.maps:
            res += str(map)
        return res

    def load_rules(self):
        """ 
        load the rules from file
        """
        self.maps = []
        print("reading mapping table")
        with open(map_file, 'r') as f:
            for line in f:
                rule = MapRule(line)
                self.maps.append(rule)
    
    def save_rules(self):
        """ 
        load the rules to file after web updates or program changes 
        """
        with open(map_file + '.txt', 'w') as f:
            for map in self.maps:
                f.write(map.format_for_file_output())

class MapRule:
    """
    manages the parsing of rules in the mapping table
    """
    def __init__(self, raw_line):
        """
        takes a raw row in the map file and extracts info
        """
        cols = raw_line.split(',')
        self.type = cols[0].strip()
        self.key = cols[1].strip()
        self.val = cols[2].strip()
    
    def __str__(self):
        """
        display a map rule to string
        """
        return self.type.ljust(15) + self.key.ljust(15) + self.val.ljust(15) + '\n'
        
    def format_for_file_output(self):
        return self.type + ',' + self.key + ',' + self.val + '\n'
 

def TEST():
    """ 
    local test function for mapper
    """
    map = Mapper()
    print(map)
    # use this to clean up file or AFTER web updates map.save_rules()
  
 
TEST()        