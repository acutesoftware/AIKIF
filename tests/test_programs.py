#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_programs.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif'
sys.path.append(pth)

test_folder = os.getcwd()

import programs


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_do_everything_here_so_we_dont_rescan(self):
        prg = programs.Programs('AIKIF Test Programs', test_folder)
        prg.list_all_python_programs()
        prg.save(test_folder + os.sep + 'programs_test_folder.csv')
        self.assertEqual(os.path.exists(test_folder + os.sep + 'programs_test_folder.csv'), True)
        
        prg.collect_program_info(test_folder + os.sep + 'programs_test_folder.md')
        self.assertEqual(os.path.exists(test_folder + os.sep + 'programs_test_folder.md'), True)
        
 

if __name__ == '__main__':
    unittest.main()
