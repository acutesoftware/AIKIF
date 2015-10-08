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

    
    def test_01_count_lines_in_file(self):
        lines = sql_tools.count_lines_in_file('test_toolbox_sql_tools.py' )
        self.assertEqual(lines > '29 recs read', True)

    def test_02_load_txt_to_sql(self):
        src_file = 'test_src_file.csv'
        with open(src_file, 'w') as f:
            f.write('col1,col2\nval1,val2\n')
        sql_tools.load_txt_to_sql('tbl_testload', src_file, os.getcwd(), ['col1','col2'] )
        self.assertTrue(os.path.exists('BACKOUT_tbl_testload.SQL'))
        self.assertTrue(os.path.exists('CREATE_tbl_testload.SQL'))
        self.assertTrue(os.path.exists('LOAD_tbl_testload.BAT'))
        self.assertTrue(os.path.exists('tbl_testload.CTL'))
        
        
if __name__ == '__main__':
    unittest.main()
