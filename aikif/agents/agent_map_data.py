# agent_map_data.py   written by Duncan Murray 30/9/2014

import os
import agent as mod_agt
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..' + os.sep + '..'  )

def TEST():
    agt = mod_agt.Agent('Testing Map Agent')
    print(agt)
    test_file = root_fldr + os.sep + 'aikif' + os.sep + 'agents' + os.sep + 'test_map.csv'
    mapping = {
        'name':'recipes', 
        'col_list':['ingredient', 'quant', 'calories'],
        'ingredient':'',
        'quant':'',
        'calories':''
    }
    map_agt = AgentMapDataFile('recipes', test_file, mapping)
    print(map_agt)
    #agt.map_data()

class AgentMapDataFile(object):
    def __init__(self, list_name, src_file, mapping):
        """
        class to map a data file to aikif structures
        """
        self.name = list_name
        self.list = []
        self.mapping = mapping
        self.src_file = src_file
        
    def __str__(self):
        """
        returns the name and list of mappings
        """
        txt = self.name + '\n'
        txt += '------------------------------\n'
        for num, map in enumerate(self.mapping):
            txt += str(num).zfill(3) + ' ' + map + '\n'
        return txt

    def map_data(self):
        """
        provides a mapping from the CSV file to the 
        aikif data structures.
        """
        with open(self.src_file, "r") as f:
            for rownum, line in enumerate(f):
                cols = line.split(',')
                print(cols)
                
        
if __name__ == '__main__':    
    TEST()

