#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_transpose.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif'

sys.path.append(pth)
import transpose

import pprint

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results")

test_list = [['col1','col2','col3'],['r1c1','r1c2','r1c3'],['r2c1','r2c2','r2c3'],['r3c1','r3c2','r3c3'],['r4c1','r4c2','r4c3']]

lst_ppl = [['name','age','job'],['Fred','58','Miner'],['Jane','34','Doctor'],['John','27','Driver'],['Sarah','33','Auditor']]

class TransposeTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.obj_transpose = transpose.Transpose(test_list) 
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.obj_transpose = None

    def test_01_instantiate(self):
        print(self.obj_transpose)
        self.assertEqual(len(self.obj_transpose.ip_data) , 5) 
        
    def test_02_pivot(self):
        #print(self.obj_transpose.ip_data)
        
        self.assertEqual(self.obj_transpose.ip_data, [['col1', 'col2', 'col3'], ['r1c1', 'r1c2', 'r1c3'], ['r2c1', 'r2c2', 'r2c3'], ['r3c1', 'r3c2', 'r3c3'], ['r4c1', 'r4c2', 'r4c3']])
        self.obj_transpose.pivot()
        #print(self.obj_transpose.op_data)
        self.assertEqual(self.obj_transpose.op_data, [['col1', 'r1c1', 'r2c1', 'r3c1', 'r4c1'], ['col2', 'r1c2', 'r2c2', 'r3c2', 'r4c2'], ['col3', 'r1c3', 'r2c3', 'r3c3', 'r4c3']])
        

    def test_03_key_value_pairs(self):
        self.obj_transpose.key_value_pairs()
        #print(self.obj_transpose.op_data)
        self.assertEqual(self.obj_transpose.op_data, [['r1c1', 'col1', 'r1c1'], ['r1c1', 'col2', 'r1c2'], ['r1c1', 'col3', 'r1c3'], ['r2c1', 'col1', 'r2c1'], ['r2c1', 'col2', 'r2c2'], ['r2c1', 'col3', 'r2c3'], ['r3c1', 'col1', 'r3c1'], ['r3c1', 'col2', 'r3c2'], ['r3c1', 'col3', 'r3c3'], ['r4c1', 'col1', 'r4c1'], ['r4c1', 'col2', 'r4c2'], ['r4c1', 'col3', 'r4c3']])
    
    def test_04_kv_test2(self):
        obj2 = transpose.Transpose(lst_ppl) 
        print(obj2.ip_data)
        obj2.key_value_pairs()
        print(obj2.op_data)
        
    def test_05_data_to_links(self):
        """
        transpose a list into a cartesan product of links
        """
        lst_raw = [
        ['NAME','Location','Job'],
        ['John','Perth','Plumber'] ,
        ['Mary','Burra','Farmer' ],
        ['Jane','Darwin','Farmer'] , 
        ['Fred','Perth','Cleaner'],
        ['Cindy','Perth','Manager' ] ,
        ]
        
        obj5 = transpose.Transpose(lst_raw) 
        lst1 = obj5.data_to_links( 0, 1)    
        print('lst1 = ' + str(len(lst1)))
        #pprint.pprint(lst1)
        
        self.assertEqual(lst_raw[0], ['NAME','Location','Job'])
        self.assertEqual(len(lst_raw), 6)
        self.assertEqual(lst1[0], ['Cat_name', 'Location', 'NAME_a', 'NAME_b', 'link_count'])
        self.assertEqual(len(lst1), 9)
        #self.assertTrue(['Location', 'Perth', 'John', 'Fred'] OR ['Location', 'Perth', 'Fred', 'John'] in lst1)
        
        lst2 = obj5.data_to_links( 0, 1, include_links_self='N')    
        self.assertEqual(len(lst2), 4)
        print('lst2 (no SELF links) = ' + str(len(lst2)))
        pprint.pprint(lst2)
        
        lst3 = obj5.data_to_links( 0, 2)    
        #print('lst3 (link by Job)= ' + str(len(lst3)))
        #pprint.pprint(lst3)
        self.assertEqual(len(lst3), 7)
        
        lst4 = obj5.data_to_links( 0, 2, include_links_self='N')    
        print('lst4 (link by Job, no SELF links)= ' + str(len(lst4)))
        pprint.pprint(lst4)
        self.assertEqual(len(lst4), 2)
        
 
    def test_06_data_to_links_CSV(self):
        """
        transpose a CSV file  into a cartesan product of links
        DATE	Project Code	Location	Contractor	 Job Colour	Balance

        """

        lst_raw = []
        with open('random_projects.csv', 'r') as f:
            for line in f:
                r = []
                cols = line.split(',')
                #print('cols = ', cols)
                for c in cols:
                    r.append(c.strip('\n').strip('"'))
                #print(r)
                lst_raw.append(r)
        
        print(lst_raw[0:10])
        obj6 = transpose.Transpose(lst_raw) 
        lst1 = obj6.data_to_links( 3, 1, include_links_self='N')    
        print('lst1 = ' + str(len(lst1)))
        pprint.pprint(lst1[0:10])


 
if __name__ == '__main__':
    unittest.main()
