#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_cls_file.py
# unit testing for collection class


import unittest
import os
import sys

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
#root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__))) 
print("in test_cls_filelist : root_folder = " + root_folder)
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'lib')


import cls_filelist as fl 
                    
class TestClassFile(unittest.TestCase):
 
    def setUp(self):
        self.fname = root_folder + os.sep + 'tests/test_results/cls_filelist_results1.csv'
        
    def test_01_file_result(self):
        """print("test1 - filelist with one file")"""
        lst1 = fl.FileList([root_folder + os.sep + 'tests'], ['test_*.py'], [],  self.fname)
        self.assertEqual(len(lst1.get_list()) > 18, True) 
        
    def test_02_multiple_file_result(self):
        """print("test2 - Collecting multiple file metadata")"""
        lst2 = fl.FileList([root_folder + os.sep + 'tests'], ['*.*'], [],  self.fname)
        self.assertEqual(len(lst2.get_list()) > 30, True) 
        
    def test_03_exclude_files(self):
        """print("test2 - Collecting multiple file metadata")"""
        lst3 = fl.FileList([root_folder + os.sep + 'tests' + os.sep + 'test_results'], ['*.*'], ['*.sql'],  self.fname)
        self.assertEqual(len(lst3.get_list()) > 10, True) 
        self.assertEqual(len(lst3.get_file_list([root_folder + os.sep + 'tests' + os.sep + 'test_results'], ['*.*'], ['*.sql'],VERBOSE=True)) > 10, True) 
        
        
        
    def test_04_save_filelist(self):
        """ test saving filelist  """
        
        if os.path.isfile(self.fname):
            os.remove(self.fname)
        aikif_fl = fl.FileList([root_folder + os.sep + 'tests'], ['*.py'], [],  self.fname)
        #print('FL = ', aikif_fl.get_list())
        aikif_fl.save_filelist(self.fname, ["name", "path", "size", "date"])
        if os.path.isfile(self.fname):
            self.assertEqual("File Exists", "File Exists") 
        else:
            self.assertEqual("File Exists", "Whoops - nope") 

    def test_05_check_metadata(self):
        """ make sure metadata is correct for this file """
        lst5 = fl.FileList([os.path.dirname(os.path.abspath(__file__))], ['test_cls_filelist.py'], [],  self.fname)
        files = lst5.get_metadata()
        for file_dict in files:
            self.assertEqual(file_dict["name"], 'test_cls_filelist.py') 
            self.assertTrue(file_dict["size"] > 2500) 
            self.assertTrue(file_dict["date"] > '2014-08-12 21:32:57') 
            self.assertEqual(file_dict["path"], os.path.dirname(os.path.abspath(__file__))) 
    
    def test_06_check_duplicate_folders(self):
        """ not really a test but more checking the version of python works as expected """
        lst = ['C:\\AAA', 'C:\\BBB', 'C:\\BBB', 'C:\\CCC', 'C:\\BBB', 'C:\\CCC']
        self.assertEqual(len(lst), 6)
        self.assertEqual(len(list(set(lst))), 3)

    def test_07_filelistGroup(self):
        fl_grp = fl.FileListGroup("AIKIF lib files", os.getcwd(), "E:\\backup")
        print(fl_grp)
        self.assertTrue(len(str(fl_grp)) > 6, True)
        # call empty functions
        fl_grp.backup()
        fl_grp.restore()
        fl_grp.backup_incremental()
        
        
    def test_08_metadata_columns(self):
        fldr = os.path.dirname(os.path.abspath(__file__))
        fl8 = fl.FileList([fldr], ['*.py'], [], "sample_filelist.csv")
        #col_headers = ["name", "size", "date", "path"]
        col_headers = ["name", "date", "size"]
        for f in fl8.fl_metadata:
            txt = fl8.print_file_details_in_line(f["fullfilename"], col_headers)
            self.assertTrue(len(str(txt)) > 6, True)
    
    def test_20_is_file_dirty(self):
        fldr = os.path.dirname(os.path.abspath(__file__))
        fl20 = fl.FileList([fldr], ['*.py'], [], "sample_filelist.csv")
        res_none = fl20.is_file_dirty(src_file_dict={}, dest_file='', date_accuracy='hour')
        
        fake_file = {}
        myfile = os.getcwd() + os.sep + 'fake_file.py'
        fake_file['fullfilename'] = myfile
        fake_file['size'] = 100
        fake_file['date'] = fl20.TodayAsString()
        res_none = fl20.is_file_dirty(fake_file, myfile, 'hour')
        self.assertEqual(res_none, True)
        
        # now pretend the file is old
        self.assertEqual(fl20.compare_file_date(fake_file['date'], myfile, 'hour'), False)
    
    def test_99_unbuilt_functions(self):
        fldr = os.path.dirname(os.path.abspath(__file__))
        fl99 = fl.FileList([os.getcwd()], ['*.*'], [], "sample_filelist.csv")
        #print(fl99.fl_metadata)
        fl99.get_dirty_filelist()
        fl99.get_metadata()
        fl99.get_failed_backups()
        fl99.add_failed_file('')
        fl99.check_files_needing_synch('', '', date_accuracy = 'hour')
        fl99.check_files_needing_synch('', 'IGNORE_BASE_PATH', date_accuracy = 'hour')
        fl99.get_file_hash('')
        self.assertTrue(True)
        
        
        
if __name__ == '__main__':
    unittest.main()