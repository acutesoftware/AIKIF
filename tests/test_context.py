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
    
    def test_03_summarise(self):
        me = context.Context()
        res = me.summarise()
        print('res = ', res)
        if me.host == 'Home PC':
            self.assertEqual(res, 'At Home\nPhone is charging, sitting still')  
        else:
            if sys.platform == 'linux':
                self.assertEqual(res, '\nPhone is charging, sitting still')  
            else:
                self.assertEqual(res, 'At Home\nPhone is charging, sitting still')  
        me.host == 'Unknown'
        me.user == 'Developer'
        res_change1 = me.summarise()
        print('res_change1 = ', res_change1)
        if sys.platform == 'linux':
            self.assertEqual(res_change1, '\nPhone is charging, sitting still')
        else:
            self.assertEqual(res_change1, 'At Home\nPhone is charging, sitting still')
        self.assertTrue(len(res_change1) > 15)
        
        
        # check for other conditions
        me.user == 'Developer'
        me.host == 'Home PC'
        res_change3 = me.summarise()
        print('res_change3 = ', res_change3)
        me.host == 'Work PC'
        res_change4 = me.summarise()
        print('res_change4 = ', res_change4)
        
        
    
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
        
    def test_08_phone(self):
        ph = context.Context()
        self.assertEqual(ph.inspect_phone(), 'Phone is charging, sitting still')
        self.assertEqual(ph.inspect_phone(moving = True), 'Phone is charging, driving in Car')
        self.assertEqual(ph.inspect_phone(on_charge = False), 'Phone is being used')
        
        
    def test_10_where_am_i(self):
       location = context.where_am_i()
       self.assertEqual(location, 'Home')
       
        
if __name__ == '__main__':
    unittest.main()