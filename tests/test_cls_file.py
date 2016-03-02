# test_cls_file.py     written by Duncan Murray 22/6/2014
# unit testing for collection class

import unittest
import os
import sys
import csv

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'lib' )

import cls_file as cl
                    
class TestClassFile(unittest.TestCase):
 
    def setUp(self):
        self.fname = 'test_results' + os.sep + 'cls_file_test_data.txt'
        self.fname = 'cls_file_test_data.txt'

    def test_01_file_create(self):
        self.assertEqual(1, 1)  # dummy
        f = cl.TextFile(self.fname)
        f.delete()
        f.append_text('# test file for cls_file\n')
        f.append_text('this is the 2nd line\n')
        f.append_text('this is the last line\n')
        
    def test_02_file_print(self):
        f = cl.File(self.fname)
        print(f)

    def test_03_file_load_string(self):
        f = cl.TextFile(self.fname)
        txt = f.load_file_to_string()
        self.assertEqual(len(txt), 68) 

    def test_04_file_load_list(self):
        f = cl.TextFile(self.fname)
        lst = f.load_file_to_list()
        self.assertEqual(len(lst), 3) 
        
  
    def test_06_launch(self):
        f = cl.File(self.fname)
        f.launch()    


    def test_07_get_file_sample(self):
        f = cl.TextFile(self.fname)
        print(f)
        self.assertTrue(len(str(f)) > 10)
        sample = f.get_file_sample(2)
        self.assertEqual(len(sample.split('\n')) - 1, 2)

    def test_08_convert_to_csv(self):
        chr31_delimited_data = """D20130611000920130611PCFile0122 15UsageFacebook - Google Chrome
D20130611001020130611PCFile0123 1UsageGoogle - Google Chrome
D20130611001120130611PCFile0400 61UsageDesktop
D20130611001220130611PCFile0500 60UsageDesktop
"""
        with open('chr31_delimited_data_file.dat', 'w') as d:
            d.write(chr31_delimited_data)
            
        f = cl.TextFile('chr31_delimited_data_file.dat')
        #self.assertEqual(f.get_file_sample(1), '00000 D20130611000920130611PCFile0122 15UsageFacebook - Google Chrome')
        
        f.convert_to_csv('chr31_delimited_data_file.csv', chr(31))
        
        f_csv = cl.TextFile('chr31_delimited_data_file.csv')
        self.assertEqual(f_csv.get_file_sample(1), '00000 "D201306110009","20130611","PCFile","0122"," 15","Usage","","","","","","","","","Facebook - Google Chrome",""\n')
    
    def test_99_file_delete(self):
        f = cl.File(self.fname)
        self.assertEqual(f.exists(), True)
        f.delete()
        self.assertEqual(f.exists(), False)
        
        # try deleting a non existing file
        f_no_file = cl.File('')
        f_no_file.delete()
        
      
if __name__ == '__main__':
    unittest.main()
