#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_text_tools.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
sys.path.append(pth)

import text_tools


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_parse_text_to_table(self):
        t1 = text_tools.parse_text_to_table('aaa,bdsdsbb,cfe\nAAA,BB,C\na,bb,ccc\n')
        self.assertEqual(t1,[['aaa', 'bdsdsbb', 'cfe'], ['AAA', 'BB', 'C'], ['a', 'bb', 'ccc']])


    def test_02_parse_text_to_table(self):
        tab_data = """animal	bird	dove		
animal	bird	duck		
animal	fish	salmon		
life	plant	vegetable	pea		
life	plant	vegetable	potato		"""
        t2 = text_tools.parse_text_to_table(tab_data)
        #print(t2)
        self.assertEqual(len(t2),5)
        self.assertEqual(t2[0], ['animal', 'bird', 'dove', '', ''])
        self.assertEqual(t2[4], ['life', 'plant', 'vegetable', 'potato', '', ''])
        text_tools.save_tbl_as_csv(t2, 'text_tools_sample.csv')
        self.assertEqual(os.path.exists('text_tools_sample.csv'), True)
        
    def test_03_parse_text_by_col_pos_wrong(self):
        t3 = text_tools.parse_text_by_col_pos('aaa,bdsdsbb,cfe\nAAA,BB,C\na,bb,ccc\n', [3,3,3])   
        self.assertEqual(t3[0], ['aaa', '', '', ',bdsdsbb,cfe'])
        self.assertEqual(t3[1], ['AAA', '', '', ',BB,C'])
        self.assertEqual(t3[2], ['a,b', '', '', 'b,ccc'])
        
     
        
if __name__ == '__main__':
    unittest.main()
