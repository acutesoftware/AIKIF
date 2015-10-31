# test_agent_map_data.py

import os
import sys
import unittest

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..')
sys.path.append(root_fldr + os.sep + 'aikif' + os.sep + 'agents')

import agent_map_data as mod_map


mapping = {
    'name':'recipes', 
    'col_list':['ingredient', 'quant', 'calories'],
    'ingredient':'',
    'quant':'',
    'calories':''
}
map_agt = mod_map.AgentMapDataFile('recipes', 'test_map.csv', mapping)

class TestAgentMapData(unittest.TestCase):
    def test_01_(self):
        print('test')
    
        print(map_agt)
        
        self.assertEqual(map_agt.mapping['name'], 'recipes')
        self.assertEqual(map_agt.mapping['col_list'], ['ingredient', 'quant', 'calories'])
        
        #map_agt.map_data()
    
    def test_02_process(self):
        map_agt.add_process('test_process1')
        self.assertEqual(map_agt.process[0],'test_process1')
        self.assertTrue('test_process1' in str(map_agt))
        
    def test_03_map_data(self):
        # TODO - for now, create a temp file
        with open('test_map.csv', 'w') as f:
            f.write('map,comment\n01,test01\n')
        map_agt.map_data()
    
   
if __name__ == '__main__':
    unittest.main()



