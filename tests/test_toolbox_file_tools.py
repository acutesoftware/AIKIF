#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_file_tools.py
import os
import sys
import unittest
import time
import shutil

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
sys.path.append(pth)

#temp_fldr = os.path.join(os.getcwd(),'test')
src_fldr = os.path.join(root_folder,'tests', 'test_src')
dest_fldr = os.path.join(root_folder,'tests', 'test_dest')
another_dest_fldr = os.path.join(root_folder,'tests', 'another_dest_fldr')

print('src folder = ', src_fldr)
print('Dest folder = ', dest_fldr)



import file_tools

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)


def build_random_file(full_filename):
    """
    make file of random letters
    """
    with open(full_filename, 'w') as f:
        f.write('hello - this is ' + full_filename)
 
class TestToolboxFileTools(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_get_filelist(self):
        """
        create temp files first in source folder
        """
        ensure_dir(src_fldr)
        build_random_file(src_fldr + os.sep + 'file1.txt')
        build_random_file(src_fldr + os.sep + 'file2.txt')
        build_random_file(src_fldr + os.sep + 'file3.txt')
        ensure_dir(src_fldr + os.sep + 'sub_folder1')
        build_random_file(src_fldr + os.sep + 'sub_folder1' + os.sep + 'file4.txt')
        build_random_file(src_fldr + os.sep + 'sub_folder1' + os.sep + 'file5.txt')
        ensure_dir(src_fldr + os.sep + 'sub_folder2')
        build_random_file(src_fldr + os.sep + 'sub_folder2' + os.sep + 'file6.txt')
        ensure_dir(src_fldr + os.sep + 'sub_folder2' + os.sep + 'sub_folder3')
        build_random_file(src_fldr + os.sep + 'sub_folder2' + os.sep + 'sub_folder3' + os.sep + 'file7.txt')
        build_random_file(src_fldr + os.sep + 'sub_folder2' + os.sep + 'sub_folder3' + os.sep + 'file8.txt')
        build_random_file(src_fldr + os.sep + 'sub_folder2' + os.sep + 'sub_folder3' + os.sep + 'file9.txt')
        
        
        # now do the tests
        fl = file_tools.get_filelist(src_fldr)
        #print(fl)
        self.assertEqual(len(fl), 9)
        for f in fl:
            print('checking ' + f.replace(os.getcwd(), ''))
            self.assertEqual(os.path.exists(f), True)

    def test_02_copy_file(self):
        test_file = 'file_to_copy.txt'
        
        #not sure if we need this for dest ? ensure_dir(dest_fldr)
        
        
        file_tools.delete_file(test_file, True)
        self.assertEqual(os.path.exists(test_file), False)
        with open(test_file, 'w') as f:
            f.write('test file')
        self.assertEqual(os.path.exists(test_file), True)
        file_tools.delete_file(test_file, True)
        self.assertEqual(os.path.exists(test_file), False)
        
        #file_tools.copy_file(test_file, dest_fldr)
        #self.assertEqual(os.path.exists(dest_fldr + os.sep + test_file), True)
        	
            
    def test_05_copy_files_to_folder(self):
        ensure_dir(another_dest_fldr)
        file_tools.copy_files_to_folder(src_fldr, another_dest_fldr) 
        
        # should only copy 3 root files
        fl5 = file_tools.get_filelist(another_dest_fldr)
        #print(fl)
        self.assertEqual(len(fl5), 3)

            
    def test_07_copy_all_files_and_subfolders(self):
        # copy the files to dest folder as is
        
        #ensure_dir(src_fldr)
        #ensure_dir(src_fldr)

        file_tools.copy_all_files_and_subfolders(src_fldr, dest_fldr, base_path_ignore=dest_fldr, xtn_list=['*.txt'])
        self.assertEqual(os.path.exists(dest_fldr + os.sep + 'file1.txt'), True)
        
        # there will be the 9 files backed up plus the CSV list
        fl7 = file_tools.get_filelist(dest_fldr)
        self.assertEqual(len(fl7), 10)
        

    def test_08_copy_all_files_and_subfolders_base_path(self):
        """
        copy the files using base path, e.g.

        """
        print('running test_08_copy_all_files_and_subfolders_base_path ')
        backup_path = "E:\\back2"  # this works on local PC only
        backup_path = another_dest_fldr  # use this for public tests on travis-CI
        
        file_tools.copy_all_files_and_subfolders(src_fldr, backup_path, base_path_ignore=dest_fldr, xtn_list=['*.txt'])
        self.assertEqual(os.path.exists(dest_fldr + os.sep + 'file1.txt'), True)
        
        # there will be the 9 files backed up plus the CSV list
        fl8 = file_tools.get_filelist(dest_fldr)
        self.assertEqual(len(fl8), 10)
        self.assertTrue(os.path.join(dest_fldr,'files_backed_up.csv') in fl8)

        
    def test_12_delete_files_in_folder(self):
        # file doesn't exist, show an error to console, but pass test
        file_tools.delete_file('no_such_file.txt')  
        
        """
        file_tools.delete_files_in_folder(another_dest_fldr)
        #self.assertEqual(os.path.exists(temp_fldr + os.sep + 'file_to_copy.txt'), False)
        fl12 = file_tools.get_filelist(another_dest_fldr)
        #print(fl)
        self.assertEqual(len(fl12), 6)  # files in folder are deleted, but the subfolders have files
        """
 

    def test_99_cleanup_temp_folders(self):
        """
        make sure we start tests cleanly
        To check results - comment out this test
        time.sleep(1)
        shutil.rmtree(src_fldr, ignore_errors=True, onerror=None)
        shutil.rmtree(dest_fldr, ignore_errors=True, onerror=None)
        shutil.rmtree(another_dest_fldr, ignore_errors=True, onerror=None)
        """
 
        pass
         
if __name__ == '__main__':
    unittest.main()
