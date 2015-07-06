import unittest
import sys
import os
import time
import aikif.config as mod_cfg
import aikif.lib.cls_filelist as fl 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'toolbox' )
import zip_tools

test_file1 = root_folder + os.sep + 'tests' + os.sep + 'test_results' + os.sep + 'usda_national_nutrients-master.zip'
op_folder = root_folder + os.sep + 'tests' + os.sep + 'test_results' + os.sep + 'unzipped'	
class ToolboxZipToolsTest(unittest.TestCase):

    def test_01_instantiate(self):
        z = zip_tools.ZipFile(test_file1)
        #print(z.type)
        self.assertEqual(z.type,'ZIP')

    def test_02_extract(self):
        z = zip_tools.ZipFile(test_file1)
        z.extract(op_folder)
        
        lst1 = fl.FileList([op_folder], ['*.*'], [],  '')
        #print(lst1.get_list())
        self.assertEqual(len(lst1.get_list()) > 1, True) 
        extract_fldr = op_folder + os.sep + 'usda_national_nutrients-master' + os.sep
        
        self.assertEqual(extract_fldr + 'README.md' in lst1.get_list(), True) 
        self.assertEqual(extract_fldr + 'usda_national_nutrients.sql' in lst1.get_list(), True) 

if __name__ == '__main__':
	unittest.main()