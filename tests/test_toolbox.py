# test_toolbox.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif"  + os.sep + "toolbox")
test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")
#print('root_fldr = ' , root_fldr)
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
        
        t1 = self.tb.get_tool_by_name('tool2.py')
        self.assertEqual(t1['file'], 'tool2.py')
        
    def test_03_run_tool(self):
        test_result = self.tb.run(self.tb.lstTools[0], [1,2,3,4,5,6,7], 'Y')
        self.assertEqual(test_result, 12)

    def test_04_run_wrong_tool(self):
        suspect_tool = {'file':'ANOTHER_tool.py', 'function':'do_stuff', 'args':['list'], 'return':['int']}
        self.tb.add(suspect_tool)
        if self.tb.verify(suspect_tool):
            test_result = self.tb.run(self.tb.lstTools[1], ['this', 'should', 'fail'])
        else:
            test_result = 555
        self.assertEqual(test_result, 555)
 
 
    def test_05_run_external_tool(self):
        ext_tool = {'file':'method1.py', 'function':'solve_example', 'args':['list'], 'return':['int']}
        ext_path = '/home/duncan/dev/src/python/kaggle/aicomp'
        self.tb.add(ext_tool)
        print('ext_path=', ext_path)
        if os.path.exists(ext_path):  # dont test this on travis-CI, and DONT verify
            test_result = self.tb.run(self.tb.lstTools[1], ['AAAA', 'BBB'], new_import_path=ext_path)
        else:
            test_result = 454
 
        self.assertEqual(test_result, 454)
    
    def test_06_predefined_list(self):
        tool1 = {'file':'tool1.py', 'function':'do_stuff', 'args':['list'], 'return':['int']}
        tool2 = {'file':'tool2.py'}
        
        tb2 = mod_tool.Toolbox(lst=[tool1, tool2])

        tb2.list()
        
        self.assertEqual(tb2.tool_as_string(tool1), 'tool1.py.do_stuff\n')
        self.assertEqual(tb2.tool_as_string(tool2), 'tool2.py\n')
        
    def test_08_save_tools(self):
        self.tb.save('tool_list.txt')
        txt = open('tool_list.txt', 'r').read()
        self.assertEqual(txt, 'test_tool.py.sum_even_numbers\n')
    
    def test_09_verify_missing_tool(self):
        tool1 = {'file':'tool_doesnt_exist.py'}
        tb9 = mod_tool.Toolbox(lst=[tool1])
        self.assertFalse(tb9.verify(tool1))
        
    def test_10_get_tool_by_name(self):

        self.tb.add({'name':'my cool tool', 'file':'tool15.py', 'function':'main'})
        t2 = self.tb.get_tool_by_name('my cool tool')
        self.assertEqual(t2['name'], 'my cool tool')

        t2 = self.tb.get_tool_by_name('tool15.py')
        self.assertEqual(t2['name'], 'my cool tool')
    
        t_not_found = self.tb.get_tool_by_name('Non existant tool')
        self.assertEqual(t_not_found, None)
    
if __name__ == '__main__':
    unittest.main()
