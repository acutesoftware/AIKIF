#!/usr/bin/python3
# coding: utf-8
# xls_tools.py

import os
import xlrd
import pandas as pd

xls_file = r'N:\DATA\opendata\datasets\ABS\5209055001DO001_202021.xlsx'
sheet_name = 'Table 4'
header_row = 1
data_row_start = 2
cols_by_position = [0,1,2]
cols_by_name = ['Final Uses ;\n Basic Prices', 'Households ;\nFinal Consumption Expenditure ;\nPurchaser''s Prices']

def self_test():
    print('testing XLS tools with ' + xls_file)
    tbl = extract_dataset(xls_file, sheet_name)
    print(tbl)
    #res = get_cols_by_name(tbl, header_row, cols_by_position, cols_by_name )
    #print(res)
    print(tbl[cols_by_name[0]])

def extract_dataset(xls_file, sheet_name):
    xls = pd.ExcelFile(xls_file)
    tbl = xls.parse(sheet_name)
    return tbl

def get_cols_by_name(tbl, header_row, cols_by_position, cols_by_name ):
    op = []
    print(tbl)

    hdr = tbl[header_row]
    print('header = ' + str(hdr()))
    for rownum, row in enumerate(tbl):
        cur_row = []
        for colnum, col in enumerate(tbl):
            if colnum in cols_by_position:
                cur_row.append(col)
        op.append(cur_row)                
    return op
self_test()    

