# test_context.py     written by Duncan Murray 6/9/2014
# unit testing for context class

import unittest
import os
import sys
import csv
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
print("HI root_folder = " + root_folder)
sys.path.append(root_folder)

import lib.cls_context as context
                    
class ContextTest(unittest.TestCase):
         
    def test_01_instantiation(self):
        me = context.Context()
        self.assertEqual(str(me)[0:7], 'Hello, ')
    
    def test_02_user_types(self):
        self.assertEqual(context.users[0]['type'], 'Developer')
        self.assertEqual(context.users[1]['type'], 'User')
        self.assertEqual(context.users[2]['type'], 'Tester')
        self.assertEqual(context.users[3]['type'], 'web_user')
    
    def test_03_host_types(self):
        pass
    
    def test_04_host_stats(self):
        """ check for reasonable ranges in CPU stats """
        me = context.Context()
        res = me.dump_all('SILENT')
        self.assertGreaterEqual(res[5]['val'], '0')
    
if __name__ == '__main__':
    unittest.main()