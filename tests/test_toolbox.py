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
        self.tb.add({'file':'test_tool.py', 'function':'sum_even_numbers', 'args':['list'], 'return':['int']})
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)


    def test_01_instantiate_class(self):
        self.assertTrue(len(str(self.tb)) > 10)

    def test_02_add_tool(self):
        self.tb.add({'file':'tool2.py', 'function':'do_stuff', 'args':['list'], 'return':['int']})
        self.assertEqual(str(self.tb), 'test_tool.py.sum_even_numbers\ntool2.py.do_stuff\n')
        
    def test_03_run_tool(self):
        test_result = self.tb.run(self.tb.lstTools[0], [1,2,3,4,5,6,7], 'Y')
        self.assertEqual(test_result, 12)

    def test_04_run_wrong_tool(self):
        suspect_tool = {'file':'ANOTHER_tool.py', 'function':'do_stuff', 'args':['list'], 'return':['int']}
        self.tb.add(suspect_tool)
        if self.tb.verify(suspect_tool):
            test_result = self.tb.run(self.tb.lstTools[1], ['this', 'should', 'fail'], 'Y')
        else:
            test_result = 555
        self.assertEqual(test_result, 555)
 
 
    def test_05_run_external_tool(self):
        ext_tool = {'file':'method1.py', 'function':'solve_example', 'args':['list'], 'return':['int']}
        ext_path = '/home/duncan/dev/src/python/kaggle/aicomp'
        self.tb.add(ext_tool)
        if os.path.exists(ext_path):  # dont test this on travis-CI, and DONT verify
            test_result = self.tb.run(self.tb.lstTools[1], ['AAAA', 'BBB'], 'N', import_path=ext_path)
        else:
            test_result = 454
 
        self.assertEqual(test_result, 454)
        
if __name__ == '__main__':
    unittest.main()
