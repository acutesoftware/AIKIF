# test_toolbox.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif"  + os.sep + "toolbox")
test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")
sys.path.append(root_fldr)
import Toolbox as mod_tool

class LogTest(unittest.TestCase):
    
    def setUp(self):
        """ Note, this gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.tb = mod_tool.Toolbox()
        print(self.tb)
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)


    def test_01_instantiate_class(self):
        self.assertTrue(len(str(self.tb)) == 0)

    def test_02_add_tool(self):
        self.tb.add({'file':'test_tool.py', 'function':'sum_even_numbers', 'args':['list'], 'return':['int']})
        self.assertTrue(len(str(self.tb)) > 10)



    
if __name__ == '__main__':
    unittest.main()