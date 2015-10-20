#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_cls_dataset.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'dataTools' 

sys.path.append(pth)


import cls_dataset as cl
                    
class TestClassDataSet(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_01_create_folder(self):
        fldr = cl.DataSet('Folder of CSV Files', 'folder')
        fldr.add('file1.csv')
        fldr.add('file2.csv')
        display_str = str(fldr)
        print(display_str)
        
        self.assertEqual(len(fldr.datatables), 2) 
        self.assertEqual(len(fldr.list_tables('\n')), 19)
        self.assertEqual(display_str, """Folder of CSV Files contains the tables 
file1.csv
file2.csv""")
        
        
    def test_02_create_database(self):
        schema = cl.DataSet('schema', 'database')
        schema.add('C_CUSTOMERS')
        schema.add('C_PRODUCTS')
        schema.add('C_SALES')
        print("test 2 - database")
        self.assertEqual(len(schema.datatables), 3)  
        self.assertEqual(len(schema.list_tables('')), 28)  

    def test_03_check_creds(self):
        schema2 = cl.DataSet('schema', 'database', ['dbase_name', 'username', 'password'])
        print(schema2)
        
    def test_04_creds_added_later(self):
        schema3 = cl.DataSet('schema', 'database' )
    
        schema3.login('dbase_name', 'username', 'password')
        schema3.logout()
        
if __name__ == '__main__':
    unittest.main()