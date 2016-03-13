# test_cls_collect.py     written by Duncan Murray 19/5/2014
# unit testing for collection class

import unittest
import os
import sys
import csv
import cls_collect_files as cl

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) ) 


class TestClassCollect(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_collect(self):
        my_files = cl.clsCollectFiles(root_folder, 'test_cls_collect.py')  # test_cls_collect
        my_files.collect_filelist()
        self.assertEqual(len(my_files.get_filelist()), 1)  # should be one file (this one)
        
    def test_filesize_cwd(self):
        my_files = cl.clsCollectFiles(root_folder, '*.*')  # test_cls_collect
        my_files.collect_filelist()
        self.assertEqual(my_files.get_tot_bytes() > 1000 , 1)  # should be at least 10k source code
        
    def test_folders_AI(self):
        my_files = cl.clsCollectFiles(root_folder, '*.*')  # test_cls_collect
        my_files.collect_filelist()
        self.assertEqual(len(my_files.get_folders())> 0, True)  # should only be at least 1 folder in .z_prototype (pycache)
        

    def test_local_list_python_folder(self):
        my_files = cl.clsCollectFiles("C:\\Python34", '*.*')  # test_cls_collect
        my_files.collect_filelist()
        self.assertEqual(my_files.get_tot_bytes() > 74913177, True ) 
        self.assertEqual(my_files.get_tot_files() > 4178, True ) 
          

    
if __name__ == '__main__':
    unittest.main()