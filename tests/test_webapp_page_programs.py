#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_webapp_page_programs.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
web_app_path = root_folder + os.sep + 'aikif' + os.sep + 'web_app' 
  
sys.path.append(web_app_path)

import page_programs


class TestWebAppPageData(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    
    def test_01_get_page_empty(self):
        if os.path.exists('program_list.html'):
            try:
                os.remove('program_list.html')
            except Exception:
                pass
    
        pge = page_programs.get_page()
        #print(pge)
        self.assertEqual('<a href="/programs/rebuild">Rebuild Program List</a><BR>' in pge, True)
        self.assertEqual(len(pge) < 100, True)

    def test_02_rebuild_list(self):
        page_programs.rebuild()
        pge = page_programs.get_page()
        #print(pge[0:1000])
        str_in_prog_list = '<TD>File Name</TD><TD>Size</TD><TD>Imports</TD><TD>List of Functions</TD>'
        self.assertEqual(str_in_prog_list in pge, True)
        self.assertEqual(len(pge) > 1000, True)

if __name__ == '__main__':
    unittest.main()
