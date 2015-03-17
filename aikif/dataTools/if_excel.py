# if_excel.py

import os
import sys
import csv
import string
import pandas as pd

def TEST():
    """
    Test functions to go into test_if_excel.py
    """
    df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
    print(df)
 #   df.to_excel('pandas.xls', sheet_name='Pandas_test')   # NOTE - xlsx not supported
 #   df.to_excel('pandas.xls')   # NOTE - xlsx not supported
#    df.to_csv('pandas.csv')  # works

    xls_small = Excel('test.xlsx')
    print(xls_small)
    print(xls_small.get_base_filename(os.getcwd()))
    
    for num, tab in enumerate(xls_small.get_sheets()):
        print('Worksheet #', num, ' = ', tab)
    
    xls_small.csv_from_excel()
    

    
class Excel():
    """
    Doesn't inherit from Database class as it is not
    really a database
    """
    def __init__(self, excel_file):
        """
        Pass the excel filename
        """
        self.excel_filename = excel_file
        self.xl_file = pd.ExcelFile(excel_file)

    def __str__(self):
        res = 'Excel object in Pandas\n'
        res += 'Name = ' + self.excel_filename + '\n'
        
        return res

    
    def get_sheets(self):
        """
        return a list of worksheet tab names
        """
        return self.xl_file.sheet_names
    
    def get_base_filename(self, op_folder):
        """
        return the base filename of the excel file
        used for exporting CSV
        """
        if self.excel_filename.lower()[-4:] == '.xls':
            base_csv = self.excel_filename.lower()[:-4]
        else:
            base_csv = self.excel_filename.lower()[:-5]
        
        if op_folder != '':
            if os.sep not in op.folder: # make sure full path not already passed
                base_csv = op_folder + os.sep + base_csv
        
        return base_csv
        
    def csv_from_excel(self, op_folder=''):
        """
        uses pandas to convert Excel workbooks to CSV
        If multiple sheets are in the excel file exist
        a separate excelfile_WORKSHEET.CSV file is 
        made for each tab
        """
        
        base_csv = self.get_base_filename(op_folder)
        
        if len(self.xl_file.sheet_names) == 1:
            xls = pd.read_excel(self.excel_filename)
            xls.to_csv(base_csv + '.csv', encoding='utf-8')
        
        else:
            for worksheet in self.xl_file.sheet_names:
                xls = pd.read_excel(self.excel_filename, worksheet)
                xls.to_csv(base_csv + '_' + worksheet + '.csv', encoding='utf-8')
                
