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
        with open(map_file, 'w') as f:
            for map in self.maps:
                f.write(map.format_for_file_output())
                
    def process_data(self, type, raw_data):
        """
        top level function to decide how to process 
        the raw data (which can be any format)
        """
        num_applicable_rules = 0
        formatted_data = self.format_raw_data(type, raw_data)
        for m in self.maps:
            if m.type == type:
                num_applicable_rules += 1
                self.process_rule(m, formatted_data, type)
        return num_applicable_rules
        
    def process_rule(self, m, dict, type):
        """ 
        uses the MapRule 'm' to run through the 'dict'
        and extract data based on the rule
        """
        print(type + ': applying rule ' + str(m) + ' to dict')
    
    def format_raw_data(self, type, raw_data):
        """
        uses type to format the raw information to a dictionary
        usable by the mapper
        """
        
        if type == 'text':
            formatted_raw_data = self.parse_text_to_dict(raw_data)
        elif type == 'file':
            formatted_raw_data = self.parse_file_to_dict(raw_data)
        else:
            formatted_raw_data = {'ERROR':'unknown data type', 'data':[raw_data]}
        return formatted_raw_data
    
    def parse_text_to_dict(self, txt):
        """ 
        takes a string and parses via NLP, ready for mapping
        """
        op = {}
        print('TODO - import NLP, split into verbs / nouns')
        op['nouns'] = txt
        op['verbs'] = txt
        
        return op
    
    def parse_file_to_dict(self, fname):
        pass
    
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
    map.process_data('text', 'the cat sat on the mat')
    # use this to clean up file or AFTER web updates map.save_rules()
  
 
TEST()        