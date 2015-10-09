#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_sql_tools.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
sys.path.append(pth)

import sql_tools


class TestToolboxSqlTools(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_init(self):
        fldr = sql_tools.root_folder
        print('test_toolbox_sql_tools, root_folder = ', fldr)
        self.assertEqual(os.path.exists(fldr), True)

    def test_02_load_txt_to_sql(self):
        src_file = 'test_src_file.csv'
        with open(src_file, 'w') as f:
            f.write('col1,col2\nval1,val2\n')
        sql_tools.load_txt_to_sql('tbl_testload', src_file, os.getcwd(), ['col1','col2'] )
        self.assertTrue(os.path.exists('BACKOUT_tbl_testload.SQL'))
        self.assertTrue(os.path.exists('CREATE_tbl_testload.SQL'))
        self.assertTrue(os.path.exists('LOAD_tbl_testload.BAT'))
        self.assertTrue(os.path.exists('tbl_testload.CTL'))

        # test to see if cols are created when not passed
        sql_tools.load_txt_to_sql('tbl_testload', src_file, os.getcwd(), None )

    def test_03_count_lines_in_file(self):
        self.assertEqual(sql_tools.count_lines_in_file('test_src_file.csv'), '2 recs read')
        self.assertEqual(sql_tools.count_lines_in_file('NO_FILE'), 'ERROR -couldnt open file')
       
    def test_04_get_CTL_log_string(self):
        details = sql_tools.get_CTL_log_string('mytbl', 'src', 'ctl')
        print(details)
        expected = r"log='logs\mytbl.log' bad='logs\mytbl.bad' discard='logs\mytbl.discard' control=ctl data='src'\n"
        self.assertEqual(len(details), len(expected))

        
if __name__ == '__main__':
    unittest.main()
