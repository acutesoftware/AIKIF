# test_mapper.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)
print(root_fldr)
import config as mod_cfg
import mapper as mod_map

class MapTest(unittest.TestCase):
    
    def setUp(self):
        """ gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.mymap = mod_map.Mapper()
        
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    """ 
    tests for maps go below - use mymap instantiated object
    """
    def test_01_instantiate(self):
        self.assertEqual(len(str(self.mymap)) > 500, True)

    def test_11_process_text_1(self):
        res = self.mymap.process_data('text', 'hello world')
        self.assertEqual(res , 4)

    def test_12_process_file_1(self):
        res = self.mymap.process_data('file', 'test.csv')
        self.assertEqual(res , 10)

    def test_13_process_unknown(self):
        res = self.mymap.process_data('blah blah', 'SOME_STUFF')
        #print(res)
        self.assertEqual(res , 0)
        
        
    def test_20_save_mapping(self):
        self.mymap.save_rules('rules_saved.txt')
        self.assertTrue(os.path.exists('rules_saved.txt'))
    
    def test_24_create_map_from_file(self):
        self.mymap.create_map_from_file(mod_map.sample_datafile)
        self.assertTrue(os.path.exists(mod_map.sample_datafile + '.rule' ))
     
    def test_30_map_columns(self):
        mc = mod_map.MapColumns(mod_map.map_file)
        self.assertTrue(len(str(mc)) > 10)
        
         
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        #print(str(self.mymap))
        pass
    
if __name__ == '__main__':
    unittest.main()
