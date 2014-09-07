# test_context.py     written by Duncan Murray 6/9/2014
# unit testing for context class

import unittest
import os
import sys
import csv
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
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
 
    def test_05_is_user_busy(self):
        me = context.Context()
        me.phone_on_charge = True
        me.user = 'Developer'
        self.assertEqual(me.is_user_busy(), False)
        me.user = 'User'
        self.assertEqual(me.is_user_busy(), True)

    def test_06_is_host_busy(self):
        me = context.Context()
        me.host_cpu_pct = '20'
        me.host_mem_available = '400000'
        self.assertEqual(me.is_host_busy(), False)
        me.host_mem_available = '600000'
        self.assertEqual(me.is_host_busy(), True)
        me.host_cpu_pct = '50'
        self.assertEqual(me.is_host_busy(), False)



        
if __name__ == '__main__':
    unittest.main()