# if_excel.py

import os
import sys
import csv
import string
import pandas as pd

def create_blank_xls_file(fname):
    """
    create a blank dummy XLS file (buggy)
    """
    
    df = pd.DataFrame({'Col1' : [32,0,-6,7], 'Col2' : [9,66,30,73],'Col3' : [89,50,-31,-50]})
    print(df)
 #  df.to_excel('pandas.xls', sheet_name='Pandas_test')   # NOTE - xlsx not supported
 #  df.to_excel('pandas.xls')   # NOTE - xlsx not supported
 #  df.to_csv('pandas.csv')  # works
    print('WARNING - doesnt work in all systems\n saving dataframe to Excel = ', fname)
    df.to_excel(fname, sheet_name='sheet1', index=False)

def xls_to_csv(xls_filename):
    """
    function to be used by Toolbox to allow for easy 
    definition (so it can be added as normal)
    """
    xls = Excel(xls_filename)
    op_file = xls.get_base_filename('') + '.csv'
    xls.csv_from_excel(op_folder='', first_sheet_only=True) 
    return op_file
    
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
    
    
    def csv_from_excel(self, op_folder='', first_sheet_only=False):
        """
        uses pandas to convert Excel workbooks to CSV
        If multiple sheets are in the excel file exist
        a separate excelfile_WORKSHEET.CSV file is 
        made for each tab
        """
        
        base_csv = self.get_base_filename(op_folder)
        
        if len(self.xl_file.sheet_names) == 1 or first_sheet_only == True:
            xls = pd.read_excel(self.excel_filename)
            xls.to_csv(base_csv + '.csv', encoding='utf-8')
        
        else:
            for worksheet in self.xl_file.sheet_names:
                xls = pd.read_excel(self.excel_filename, worksheet)
                xls.to_csv(base_csv + '_' + worksheet + '.csv', encoding='utf-8')
                
#create_blank_xls_file('test2.xlsx')