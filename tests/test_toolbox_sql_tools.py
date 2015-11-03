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
        #print('test_toolbox_sql_tools, root_folder = ', fldr)
        self.assertEqual(os.path.exists(fldr), True)

    def test_02_load_txt_to_sql(self):
        src_file = 'test_src_file.csv'
        with open(src_file, 'w') as f:
            f.write('col1,col2\nval1,val2\n')
        sql_tools.load_txt_to_sql('tbl_testload', src_file, src_file, os.getcwd()  )
        self.assertTrue(os.path.exists('BACKOUT_tbl_testload.SQL'))
        self.assertTrue(os.path.exists('CREATE_tbl_testload.SQL'))
        self.assertTrue(os.path.exists('tbl_testload.CTL'))

        # test to see if cols are created when not passed
        sql_tools.load_txt_to_sql('tbl_testload', src_file, src_file, os.getcwd() )

    def test_03_count_lines_in_file(self):
        self.assertEqual(sql_tools.count_lines_in_file('test_src_file.csv'), '2 recs read')
        self.assertEqual(sql_tools.count_lines_in_file('NO_FILE'), 'ERROR -couldnt open file')
       
    def test_04_get_CTL_log_string(self):
        details = sql_tools.get_CTL_log_string('mytbl', 'src')
        expected = " log='mytbl.log' bad='mytbl.bad' discard='mytbl.discard' control=mytbl.ctl data='src'\n"
        self.assertEqual(len(details), len(expected))
        
        with open('tbl_testload.CTL', 'r') as f:
            contents = f.read()
        self.assertTrue(contents, """LOAD DATA
TRUNCATE
into table tbl_testload
fields terminated by ','
TRAILING NULLCOLS
(
COL1,
COL2)""")

    def test_05_create_BAT_file(self):
        sql_tools.create_BAT_file('LOAD_tbl_testload.BAT', 'mytbl', 'test_src_file.csv', 'test_src_file.csv', 'password.par')
        self.assertTrue(os.path.exists('LOAD_tbl_testload.BAT'))
        with open('LOAD_tbl_testload.BAT', 'r') as f:
            bat_contents = f.read()
        self.assertTrue(bat_contents, """REM Loads mytbl from test_src_file.csv
sqlldr parfile='password.par' log='mytbl.log' bad='mytbl.bad' discard='mytbl.discard' control=mytbl.CTL data='test_src_file.csv'""")

    
if __name__ == '__main__':
    unittest.main()
