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
        
    def test_04_parse_text_fixed_delim(self):
        t4 = text_tools.parse_text_to_table('Hi\nLo\n')   
        self.assertEqual(t4, [['Hi'], ['Lo']])
  
    def test_05_identify_col_pos(self):
        col_splits = text_tools.identify_col_pos('Name Address Phone very_long_col_name')
        self.assertEqual(col_splits, [5, 13, 19, 36])
    
    def test_06_parse_text_to_table(self):
        test_hdr = 'Name,Address,zip,,,,'
        delim = text_tools.identify_delim(test_hdr)
        self.assertEqual(delim, ',')
        t3 = text_tools.parse_text_to_table(test_hdr)   
        self.assertEqual(t3, [['Name', 'Address', 'zip', '', '', '', '']])
 

    def test_07_fingerprint(self):
        print('test fingerprint')
        self.assertEqual(text_tools.fingerprint('hi\n there\n'), 'HITHERE')
        self.assertEqual(text_tools.fingerprint(' FRANK JOHNSON\n\n'), 'FRANKJOHNSON')
        self.assertEqual(text_tools.fingerprint('Johnson, Frank 2 1!!!!'), 'FRANKJOHNSON')
        self.assertTrue(text_tools.is_match('Johnson, Frank', 'FRANK JOHNSON'))
        self.assertTrue(text_tools.is_match('Jane6959494', 'JANE'))
        self.assertFalse(text_tools.is_match('Jane', 'J@NE'))
 
if __name__ == '__main__':
    unittest.main()
