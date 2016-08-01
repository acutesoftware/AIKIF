#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_file_tools.py
import os
import sys
import unittest
import time

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
sys.path.append(pth)

#temp_fldr = os.path.join(os.getcwd(),'test')
temp_fldr = os.path.join(root_folder,'tests', 'test')
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
        ensure_dir(temp_fldr)
        
        
        file_tools.delete_file(test_file, True)
        self.assertEqual(os.path.exists(test_file), False)
        with open(test_file, 'w') as f:
            f.write('test file')
        self.assertEqual(os.path.exists(test_file), True)
        file_tools.delete_file(temp_fldr + os.sep + test_file, True)
        self.assertEqual(os.path.exists(temp_fldr + os.sep + test_file), False)
        #file_tools.copy_file(test_file, 'test_results')
        #self.assertEqual(os.path.exists(os.getcwd() + os.sep + 'test_results' + os.sep + test_file), True)
            
            
    def test_05_copy_files_to_folder(self):
        file_tools.copy_files_to_folder(os.getcwd(), temp_fldr)
        #self.assertEqual(os.path.exists(os.path.join(temp_fldr,'file_to_copy.txt')), True)

            
    def test_07_copy_all_files_and_subfolders(self):
        self.assertEqual(os.path.exists(temp_fldr + os.sep + 'test_toolbox_file_tools.py'), False)
        # TODO - fix this, copies too many files on travis-ci
        #file_tools.copy_all_files_and_subfolders(os.getcwd(), temp_fldr, os.getcwd(), ['*.py'])
        #self.assertEqual(os.path.exists(temp_fldr + os.sep + 'test_toolbox_file_tools.py'), True)
        
        
    def test_12_delete_files_in_folder(self):
        file_tools.delete_file('no_such_file.txt')
        file_tools.delete_files_in_folder(temp_fldr)
        self.assertEqual(os.path.exists(temp_fldr + os.sep + 'file_to_copy.txt'), False)

        
         
if __name__ == '__main__':
    unittest.main()
