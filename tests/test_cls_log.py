# test_cls_log.py

import unittest
import sys
import os
import time
# test_fldr = os.getcwd() + os.sep + 'test_results'
test_fldr = '.'
import aikif.cls_log as mod_log
import aikif.config as cfg

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
        self.mylog.record_result('test', 'Minor Success = cool')        
        self.mylog.record_result('test', 'Massive Success = JACKPOT')        
        self.mylog.record_result('test', 'Minor Failure = meh')        
        self.mylog.record_result('test', 'Massive Failure = AAUURRGHH')        
        self.assertEqual(self.mylog.logFileResult, os.getcwd() + os.sep + 'test_results' + os.sep + 'result.log')
        self.assertEqual(os.path.isfile(self.mylog.logFileResult), True)


    def test_06_append_log_source(self):
        self.mylog.record_source('test', 'hello - recording source')        
        self.assertEqual(self.mylog.logFileSource, os.getcwd() + os.sep + 'test_results' + os.sep + 'source.log')
        self.assertEqual(os.path.isfile(self.mylog.logFileSource), True)

    def test_07_add_watch_point(self):
        self.mylog.add_watch_point('cool', 7,1)
        self.mylog.add_watch_point('JACKPOT', 9,9)
        self.mylog.add_watch_point('meh', 3,1)
        self.mylog.add_watch_point('AAUURRGHH', 1,9)
        self.assertEqual(len(self.mylog.watch_points), 4)   # 4 entries in watchpoints
        self.assertEqual(len(str(self.mylog.watch_points)), 207)   # 215 characters in watchpoints
        self.assertEqual(self.mylog.watch_points[0]['string'], 'cool')  
        self.assertEqual(self.mylog.watch_points[0]['rating'], 7)  
        self.assertEqual(self.mylog.watch_points[0]['importance'], 1)  
        self.assertEqual(self.mylog.watch_points[3]['string'], 'AAUURRGHH')  
        self.assertEqual(self.mylog.watch_points[3]['rating'], 1)  
        self.assertEqual(self.mylog.watch_points[3]['importance'], 9)  
        
    def test_10_logsum_init(self):
        time.sleep(4)  # warning - fails first time this is run if no logs exist
        sum = mod_log.LogSummary(self.mylog, test_fldr)
        self.assertTrue(len(str(sum)) > 10)
    
    def test_11_summarise_results(self):
        sum = mod_log.LogSummary(self.mylog, test_fldr)
        sum.summarise_events()


    def test_12_filter_by_program(self):
        # first create some sample log entries from separate programs
        lg = mod_log.Log(cfg.fldrs['log_folder'])
        lg.record_process('test_prog1.py', 'test_prog1.py - recording process')
        lg.record_source('test_prog1.py', 'test_prog1.py - recording source')
        lg.record_command('test_prog1.py', 'test_prog1.py - recording command')
        lg.record_result('test_prog1.py', 'test_prog1.py - recording result')
        
        lg.record_process('test_prog2.py', 'test_prog2.py - recording process')
        lg.record_source('test_prog2.py', 'test_prog2.py - recording source')
        lg.record_command('test_prog2.py', 'test_prog2.py - recording command')
        lg.record_result('test_prog2.py', 'test_prog2.py - recording result')
        
        # summarise by program
        sum = mod_log.LogSummary(lg, cfg.fldrs['log_folder'])
        sum.filter_by_program('prog1.py', cfg.fldrs['log_folder'] + os.sep + 'prog1.txt')
        sum.filter_by_program('prog2.py', cfg.fldrs['log_folder'] + os.sep + 'prog2.txt')
    
        self.assertEqual(os.path.isfile(cfg.fldrs['log_folder'] + os.sep + 'prog1.txt'), True)
        self.assertEqual(os.path.isfile(cfg.fldrs['log_folder'] + os.sep + 'prog2.txt'), True)
    
    
    def test_13_check_missing_logs_doesnt_break_sum(self):
        print("TODO = test_13_check_missing_logs_doesnt_break_sum (will fail)")
        

        
if __name__ == '__main__':
    unittest.main()