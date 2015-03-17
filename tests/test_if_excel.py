# test_if_excel.py  written by Duncan Murray 17/3/2015

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 

test_folder = os.getcwd() + os.sep + 'test_results'
test_file = test_folder + os.sep + 'test_pandas.xlsx'

import aikif.dataTools.if_excel as mod_xl
                    
class DataIfEmailTest(unittest.TestCase):
    def setup(self):
        print('running excel tests')
        
    def test_01_create_excel_file(self):
        """
        TODO - pandas installed ok, running Python 3.4 but 
        complains of missing xlwt (xls) or openpyxl (xlsx)
        """
        dummy_file = test_folder + os.sep + 'dummy.xls'
        try:
            os.remove(dummy_file)
        except:
            pass
        # doesnt work      xls = mod_xl.create_blank_xls_file(dummy_file)
        
        
    def test_02_get_name(self):
        xls = mod_xl.Excel(test_file)
        self.assertEqual('test_pandas.xlsx' in str(xls), True)
        
        
    def test_03_export_csv2(self):
        """ 
        export to CSV test - you can do this in one line
        but not a good idea to do it twice in the tests as 
        timing issues mean CSV's are still open when next test
        starts
            mod_xl.Excel(test_file).csv_from_excel() 
        """
        op_csv1 = test_folder + os.sep + 'test_pandas_ages.csv'
        op_csv2 = test_folder + os.sep + 'test_pandas_codes.csv'
        op_csv3 = test_folder + os.sep + 'test_pandas_notes.csv'
        try:
            os.remove(op_csv1)
            os.remove(op_csv2)
            os.remove(op_csv3)
        except:
            pass
            
        xls = mod_xl.Excel(test_file)
        xls.csv_from_excel()        
        self.assertEqual(os.path.isfile(op_csv1),  True)
        self.assertEqual(os.path.isfile(op_csv2),  True)
        self.assertEqual(os.path.isfile(op_csv3),  True)
        
        
if __name__ == '__main__':
    unittest.main()        