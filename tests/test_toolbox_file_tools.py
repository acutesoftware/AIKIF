#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_file_tools.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
#sys.path.append(pth)

import file_tools


class TestToolboxFileTools(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_get_filelist(self):
        fl = file_tools.get_filelist(os.getcwd())
        #print(fl)
        self.assertEqual(len(fl) > 2, True)
        for f in fl:
            print('checking ' + f.replace(os.getcwd(), ''))
            self.assertEqual(os.path.exists(f), True)

            
    def test_02_download(self):
        
        self.assertEqual(1, 1)
            
    def test_03_delete_files_in_folder(self):
        
        self.assertEqual(1, 1)
            
    def test_04_copy_files_to_folder(self):
        
        self.assertEqual(1, 1)
            
            
if __name__ == '__main__':
    unittest.main()
