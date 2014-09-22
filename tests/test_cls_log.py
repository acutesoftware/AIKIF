# test_cls_log.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)
import cls_log

class LogTest(unittest.TestCase):
    
    def setUp(self):
        """ Note, this gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.mylog = cls_log.Log('T:\\user\\AIKIF')
        self.mylog.record_command('test.txt', 'hello')
    
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)


    def test_01_new_log(self):
        self.assertTrue(len(str(self.mylog)) > 10)

    def test_02_get_folder(self):
        result = self.mylog.get_folder_process()
        self.assertEqual(result, 'T:\\user\\AIKIF\\log\\process.log')
    
    def test_03_logsum_init(self):
        sum = cls_log.LogSummary(self.mylog, 'T:\\user\\AIKIF')
        self.assertTrue(len(str(sum)) > 10)
        #print (sum)
    
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        #print(str(self.mylog))
        pass
    
if __name__ == '__main__':
    unittest.main()