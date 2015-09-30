# test_context.py     written by Duncan Murray 6/9/2014
# unit testing for context class
import os
import sys 
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'lib' 
sys.path.append(pth)

import cls_context as context
                    
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
        me = context.Context()
        res = me.summarise()
        #print(res)  
            # At Home
            # Phone is charging, sitting still
        self.assertEqual(res[0:7], 'At Home')
    
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

    def test_07_get_host_usage(self):
        me = context.Context()
        #print('me.get_host_usage() = ', me.get_host_usage())
        self.assertTrue(int(me.get_host_usage()[2]) > 1000000)
        
        #override available memory
        me.host_mem_available = '4000000'
        self.assertEqual(int(me.host_mem_available), 4000000)
        
        
if __name__ == '__main__':
    unittest.main()