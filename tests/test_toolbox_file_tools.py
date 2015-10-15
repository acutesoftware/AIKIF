#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_file_tools.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
sys.path.append(pth)

import file_tools

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        
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

    def test_02_copy_file(self):
        test_file = 'file_to_copy.txt'
        ensure_dir(os.getcwd() + os.sep + 'test_results')
        
        
        file_tools.delete_file(test_file, True)
        self.assertEqual(os.path.exists(test_file), False)
        with open(test_file, 'w') as f:
            f.write('test file')
        self.assertEqual(os.path.exists(test_file), True)
        file_tools.delete_file('test_results' + os.sep + test_file, True)
        self.assertEqual(os.path.exists('test_results' + os.sep + test_file), False)
        file_tools.copy_file(test_file, 'test_results')
        self.assertEqual(os.path.exists('test_results' + os.sep + test_file), True)
            
            
    def test_03_delete_files_in_folder(self):
        print('TODO - make temp folder')
        self.assertEqual(1, 1)
            
    def test_04_copy_files_to_folder(self):
        print('TODO - make temp folder')
        self.assertEqual(1, 1)
            
            
if __name__ == '__main__':
    unittest.main()
