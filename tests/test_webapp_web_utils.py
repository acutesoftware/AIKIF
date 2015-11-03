#!/usr/bin/python3
# coding: utf-8
# test_webapp_web_utils.py

import unittest
import sys
import os
import time
import aikif.config as mod_cfg
import aikif.lib.cls_filelist as fl 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
web_app_path = root_folder + os.sep + 'aikif' + os.sep + 'web_app' 
sys.path.append(web_app_path)

import web_utils

list_food = ['cheese', 'bread', 'butter', 'fritz']

csv_file = os.getcwd() + os.sep + 'csv_sample.csv'
with open(csv_file, 'w') as f:
    f.write('"name","score",\n"Fred",55\n"Jane",64\n')

class WebAppWebUtilsTest(unittest.TestCase):
    def test_01_lst_to_html(self):
        htm = web_utils.list2html(list_food)
        self.assertEqual(htm, """<TABLE width=100% border=0><TR>
<TD>cheese</TD>
</TR>
<TR>
<TD>bread</TD>
</TR>
<TR>
<TD>butter</TD>
</TR>
<TR>
<TD>fritz</TD>
</TR>
</TABLE><BR>
""" ) 

    def test_02_GetFileList(self):
        fl = web_utils.GetFileList(web_app_path, '*.py', shortNameOnly='Y')
        self.assertEqual(os.sep in fl[0], False)  # this is a short list of files
        self.assertEqual(len(fl[0]) < 15, True)
        self.assertEqual(len(fl) > 12, True)   # at least 12 files
        self.assertEqual('.htaccess' in fl, True)
        self.assertEqual('web_utils.py' in fl, True)
        
        fl2= web_utils.GetFileList(web_app_path, '*.py', shortNameOnly='N')
        self.assertEqual(len(fl2) > 12, True)
        self.assertEqual(os.sep in fl2[0], True)  # this is a short list of files
        self.assertEqual(len(fl2[0]) > 15, True)
        self.assertEqual(len(fl2), len(fl))   # short filelist should match long list
        #print(fl2)

    def test_03_filelist2html(self):
        fl = web_utils.GetFileList(web_app_path, '*.py', shortNameOnly='Y')
        htm = web_utils.filelist2html(fl, web_app_path, hasHeader='N')
        self.assertEqual(len(htm) > 10, True) 
        print(htm)
        self.assertEqual(htm[0:43], '<TABLE width=100% border=0><TR><TD><a href=')  
        
    def test_04_build_search_form(self):
        txt = web_utils.build_search_form()
        self.assertEqual(txt[0:31], '<form action="." method="POST">')
        self.assertEqual(txt[-8:],'</form>\n')
        #print(txt)
 
    def test_05_dict_to_htmlrow(self):
        dct = {'name':'duncan', 'email':'djmurray@acutesoftware.com.au'}
        htm = web_utils.dict_to_htmlrow(dct)
        self.assertEqual(len(htm), 121) 
        self.assertEqual(htm[0:12], '<TR>\n<TD><p>')
        self.assertEqual(htm[-15:], '</p></TD></TR>\n')

        
    def test_06_read_csv_to_html_table(self):
        dct = {'name':'duncan', 'email':'djmurray@acutesoftware.com.au'}
        htm = web_utils.read_csv_to_html_table(csv_file, 'Y')
        htm2 = web_utils.read_csv_to_html_table(csv_file, 'N')
        #print(htm)
        self.assertEqual(len(htm), 186) 
        self.assertEqual('<TR><TH>name</TH>' in htm, True) 

        self.assertEqual(len(htm2), 186) 
        self.assertEqual('<TR><TH>name</TH>' in htm2, False) 
        self.assertEqual(htm[0:13], '<table class=')
        
    def test_07_read_csv_to_html_list(self):
        dct = {'name':'duncan', 'email':'djmurray@acutesoftware.com.au'}
        htm = web_utils.read_csv_to_html_list(csv_file)
        self.assertEqual(len(htm), 116) 
        self.assertEqual(htm[0:41], '<div id="table_row"> name  score   </div>')
 
    def test_08_list_to_html(self):
        res = web_utils.list2html(['1',2,['3','4','5']])
        self.assertEqual('<TD>3, 4, 5, </TD></TR>' in res, True)
        self.assertEqual('<TD>2</TD>' in res, True)
        
if __name__ == '__main__':
	unittest.main()
