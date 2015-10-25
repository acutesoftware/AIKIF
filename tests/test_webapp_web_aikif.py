#!/usr/bin/python3
# coding: utf-8
# test_webapp_web_aikif.py

import unittest
import sys
import os
import time
import aikif.config as mod_cfg
import aikif.lib.cls_filelist as fl 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
web_app_path = root_folder + os.sep + 'aikif' + os.sep + 'web_app' 
sys.path.append(web_app_path)

import web_aikif

list_food = ['cheese', 'bread', 'butter', 'fritz']

csv_file = os.getcwd() + os.sep + 'csv_sample.csv'
with open(csv_file, 'w') as f:
    f.write('"name","score",\n"Fred",55\n"Jane",64\n')

class WebAppWebAikif(unittest.TestCase):
    def test_01_import(self):
        self.assertEqual(len(web_aikif.menu) > 4, True)

    def test_02_page_home(self):
        self.assertEqual(len(web_aikif.page_home()) > 4, True)
        
    def test_03_search_post(self):
        import page_search
        txt = page_search.get_page('test')
        self.assertEqual(len(txt) > 4, True)
        
    def test_04_page_todo(self):
        self.assertEqual(len(web_aikif.page_todo()) > 4, True)
        
    def test_05_page_projects(self):
        self.assertEqual(len(web_aikif.page_projects()) > 4, True)
        
        
        
    def test_06_page_agents(self):
        
        txt = web_aikif.page_agents()
        self.assertEqual(len(txt) > 4, True)
        
         
        
    def test_07_page_programs(self):
        txt = web_aikif.page_programs()
        self.assertEqual(len(txt) > 4, True)
        
    def test_07a_page_programs_rebuild(self):
        txt = web_aikif.page_programs_rebuild()
        print(txt)
        self.assertEqual(len(txt) > 4, True)
        
        
    def test_08_page_about(self):
        self.assertEqual(len(web_aikif.page_about()) > 4, True)
        
        
    def test_09_page_error(self):
        self.assertEqual(len(web_aikif.page_error('test')) > 4, True)
        
    def test_10_page_data(self):
        txt = web_aikif.page_data()
        self.assertEqual(len(txt) > 9, True)
        
        
    def test_11_page_data_show(self):
        txt = web_aikif.page_data_show(csv_file)
        #print(txt)
        self.assertEqual(len(txt) > 9, True)
        
    def test_12_escape_html(self):
        self.assertEqual(web_aikif.escape_html('<H1>TEST</H1>'), '&lt;H1&gt;TEST&lt;/H1&gt;')

    def test_13_format_list_as_html_table_row(self):
        self.assertEqual(web_aikif.format_list_as_html_table_row(['1','2']), '<TR><TD>1</TD><TD>2</TD></TR>')


        
if __name__ == '__main__':
	unittest.main()
