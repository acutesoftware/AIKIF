# test_agent_map_data.py

import os
import unittest
import aikif.agents.agent_map_data as mod_map
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__))+os.sep+'..'+os.sep + '..')
test_file = root_fldr + os.sep + 'aikif' + os.sep + 'agents' + os.sep + 'test_map.csv'
mapping = {
    'name':'recipes', 
    'col_list':['ingredient', 'quant', 'calories'],
    'ingredient':'',
    'quant':'',
    'calories':''
}
map_agt = mod_map.AgentMapDataFile('recipes', test_file, mapping)

class TestAgentMapData(unittest.TestCase):
    def test_01_(self):
        print('test')
    
        print(map_agt)
        
        self.assertEqual(map_agt.mapping['name'], 'recipes')
        self.assertEqual(map_agt.mapping['col_list'], ['ingredient', 'quant', 'calories'])
        
        #map_agt.map_data()
    
    def test_02_process(self):
        map_agt.add_process('test1')
        self.assertEqual(map_agt.process[0],'test1')
    
    
   
if __name__ == '__main__':
    unittest.main()



