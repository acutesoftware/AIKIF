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
    
    def test_02_rebuild_list(self):
        
        page_programs.rebuild()
        pge = page_programs.get_page()
        self.assertTrue(os.path.exists('program_list.html'))
        #print(pge[0:1000])
        str_in_prog_list = '<TD>File Name</TD><TD>Size</TD><TD>Imports</TD><TD>List of Functions</TD>'
        self.assertEqual(str_in_prog_list in pge, True)
        self.assertEqual(len(pge) > 1000, True)

        os.remove('program_list.html')
        self.assertFalse(os.path.exists('program_list.html'))
                
    def test_03_get_page_empty(self):
        if os.path.exists('program_list.html'):
            os.remove('program_list.html')
        pge = page_programs.get_page()
        self.assertEqual('<a href="/programs/rebuild">Rebuild Program List</a><BR>' in pge, True)
        self.assertEqual(len(pge) < 100, True)


        
if __name__ == '__main__':
    unittest.main()
