# test_cls_file.py     written by Duncan Murray 22/6/2014
# unit testing for collection class

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)


import AI.lib.cls_filelist as fl 
                    
class TestClassFile(unittest.TestCase):
 
    def setUp(self):
        self.fname = 'test_results/cls_filelist_results1.csv'
        
    def test_one_file_result(self):
        print("test1 - Collecting one file")
        lst1 = fl.FileList([root_folder + os.sep + 'README.md'], ['*.*'], [],  self.fname)
        self.assertEqual(len(lst1.get_list()), 1) 
        
    def test_multiple_file_result(self):
        print("test2 - Collecting multiple file metadata")
        lst2 = fl.FileList([root_folder + os.sep + 'tests'], ['*.*'], [],  self.fname)
        self.assertEqual(len(lst2.get_list()), 25) 
        
    def save_filelist(self):
        self.lst.save_filelist(lst.filelist, lst.output_file_name, ["name", "path", "size", "date"])
        print("test3 - saving filelist to ", lst.output_file_name)
        self.assertEqual(3, 3) 
        

        
if __name__ == '__main__':
    unittest.main()