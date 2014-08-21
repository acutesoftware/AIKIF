# test_cls_file.py     written by Duncan Murray 22/6/2014
# unit testing for collection class
# NOTE - this is different to the agent_filelist.py program because 
#        the agent_fileList USES this, and so should have a single 
#        higher level test.


import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
print("in test_cls_filelist : root_folder = " + root_folder)
sys.path.append(root_folder)


import aikif.lib.cls_filelist as fl 
                    
class TestClassFile(unittest.TestCase):
 
    def setUp(self):
        self.fname = 'test_results/cls_filelist_results1.csv'
        
    def test_01_file_result(self):
        """print("test1 - filelist with one file")"""
        lst1 = fl.FileList([root_folder ], ['README.md'], [],  self.fname)
        self.assertEqual(len(lst1.get_list()), 1) 
        
    def test_02_multiple_file_result(self):
        """print("test2 - Collecting multiple file metadata")"""
        lst2 = fl.FileList([root_folder + os.sep + 'tests'], ['*.*'], [],  self.fname)
        self.assertEqual(len(lst2.get_list()) > 50, True) 
        
    def test_03_exclude_files(self):
        """print("test2 - Collecting multiple file metadata")"""
        lst3 = fl.FileList([root_folder + os.sep + 'tests' + os.sep + 'test_results'], ['*.*'], ['*.sql'],  self.fname)
        self.assertEqual(len(lst3.get_list()), 12) 
        
    def test_04_save_filelist(self):
        """ test saving filelist  """
        
        if os.path.isfile(self.fname):
            os.remove(self.fname)
        aikif_fl = fl.FileList([root_folder + os.sep + 'tests'], ['*.py'], [],  self.fname)
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

        
if __name__ == '__main__':
    unittest.main()