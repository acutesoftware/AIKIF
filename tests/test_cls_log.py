# test_cls_log.py

import unittest
import sys
import os
import time
test_fldr = os.getcwd() + os.sep + 'test_results'
import aikif.cls_log as mod_log

class LogTest(unittest.TestCase):
    
    def setUp(self):
        """ Note, this gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.mylog = mod_log.Log(test_fldr)
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)


    def test_01_new_log(self):
        self.assertTrue(len(str(self.mylog)) > 10)

    def test_02_get_folder(self):
        result = self.mylog.get_folder_process()
        self.assertEqual(result, test_fldr + os.sep + 'process.log')

    def test_03_append_log_process(self):
        self.mylog.record_process('test', 'hello - recording process')
        self.assertEqual(self.mylog.logFileProcess, os.getcwd() + os.sep + 'test_results' + os.sep + 'process.log')
        self.assertEqual(os.path.isfile(self.mylog.logFileProcess), True)


    def test_04_append_log_command(self):
        self.mylog.record_command('test', 'hello - recording command')        
        self.assertEqual(self.mylog.logFileCommand, os.getcwd() + os.sep + 'test_results' + os.sep + 'command.log')
        self.assertEqual(os.path.isfile(self.mylog.logFileCommand), True)


    def test_05_append_log_result(self):
        self.mylog.record_result('test', 'hello - recording result')        
        self.assertEqual(self.mylog.logFileResult, os.getcwd() + os.sep + 'test_results' + os.sep + 'result.log')
        self.assertEqual(os.path.isfile(self.mylog.logFileResult), True)


    def test_06_append_log_source(self):
        self.mylog.record_source('test', 'hello - recording source')        
        self.assertEqual(self.mylog.logFileSource, os.getcwd() + os.sep + 'test_results' + os.sep + 'source.log')
        self.assertEqual(os.path.isfile(self.mylog.logFileSource), True)

        
    def test_10_logsum_init(self):
        time.sleep(4)  # warning - fails first time this is run if no logs exist
        sum = mod_log.LogSummary(self.mylog, test_fldr)
        self.assertTrue(len(str(sum)) > 10)
    
    def test_11_summarise_results(self):
        sum = mod_log.LogSummary(self.mylog, test_fldr)
        sum.summarise_events()
    
if __name__ == '__main__':
    unittest.main()