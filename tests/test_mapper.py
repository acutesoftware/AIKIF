# test_mapper.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
#sys.path.append(root_fldr)
import aikif.mapper as mod_map

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

    def test_21_process_file_1(self):
        res = self.mymap.process_data('file', 'test.csv')
        self.assertEqual(res , 10)

     
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        #print(str(self.mymap))
        pass
    
if __name__ == '__main__':
    unittest.main()