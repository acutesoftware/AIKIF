#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_webapp_page_data.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
web_app_path = root_folder + os.sep + 'aikif' + os.sep + 'web_app' 
  
sys.path.append(web_app_path)

import page_data


class TestWebAppPageData(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_get_list_of_files(self):
        fles = page_data.get_list_data_files(page_data.data_folder)
        #print(t)
        self.assertEqual('<TR><TD>' in fles, True)

    def test_02_show_data_file(self):
        print(('test02 = page_data.data_folder = ', page_data.data_folder))
        fles = page_data.show_data_file(page_data.data_folder + os.sep + 'LOCATION_WORLD.csv')
        #print(fles)
        self.assertEqual('<TR><TD>153</TD><TD>MDG</TD><TD>Madagascar</TD><TD>' in fles, True)
    
    
    def test_08_get_page_with_datafile(self):
        pge = page_data.get_page(page_data.data_folder + os.sep + 'LOCATION_WORLD.csv')
        #print(pge[0:2000])
        self.assertEqual('<H3>Master File Mapping</H3>' in pge, True)
    
    def test_09_get_page(self):
        pge = page_data.get_page()
        #print(pge)
        self.assertEqual('<H3>Master File Mapping</H3>' in pge, True)


if __name__ == '__main__':
    unittest.main()
