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

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results")

test_list = [['col1','col2','col3'],['r1c1','r1c2','r1c3'],['r2c1','r2c2','r2c3'],['r3c1','r3c2','r3c3'],['r4c1','r4c2','r4c3']]

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
        
if __name__ == '__main__':
    unittest.main()
