#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run_tests.py

import os
import glob
import time
import unittest as unittest

# List of temp files to wipe after tests run

files_to_wipe = [
'dfgkljdfgkljdflkgjdlfkgj.sdfsdf',  # make sure a fake file doesnt break things
'_sessions.txt',
'agent.txt',
'BACKOUT_tbl_testload.SQL',
'chr31_delimited_data_file.csv',
'chr31_delimited_data_file.dat',
'cls_file_test_data.txt',
'command.log',
'config_credentials.txt',
'CREATE_TABLE_test07.SQL',
'CREATE_tbl_testload.SQL',
'CREATE_TEST01.SQL',
'csv_sample.csv',
'data.txt',
'datatable_calcs.csv',
'datatable_output.csv',
'datatable_sample.csv',
'file_to_copy.txt',
'filelist_image_metadata.csv',
'filelist_images.csv',
'image_metadata.csv',
'index_normal_results.txt',
'index_normal_source.txt',
'index_odd_chars_results.txt',
'index_odd_chars_source.txt',
'LOAD_tbl_testload.BAT',
'local_test_agent.py',
'my_grid.txt',
'plan_test.txt',
'process.log',
'program_list.html',
'programs_test_folder.csv',
'programs_test_folder.csv',
'programs_test_folder.md',
'result.log',
'review_file_samples.html',
'review_ontology.html',
'review_ontology.txt',
'rules_saved.txt',
'sample_big.xml',
'sample_big1.xml',
'sample_med.xml',
'sample_med1.xml',
'sample_small.xml',
'sample_small1.xml',
'screenshot.png',
'small_image.jpg',
'summary_diary.dat',
'task.blah',
'task.html',
'task.md',
'task.rst',
'tbl_testload.CTL',
'temp.tar',
'test.gz',
'test.tar',
'test_bias.log',
'test_country.txt',
'test_full_sql_generation.sql',
'test_grid.txt',
'test_map.csv',
'test_nested.zip',
'test_output.txt',
'test_output_win.txt',
'test_sql_code_agg_multiple_cols.sql',
'test_sql_code_agg_single_col.sql',
'test_sql_code_test_rev_piv.sql',
'test_sql_code_test_rev_piv_simple.sql',
'test_src_file.csv',
'test_world.txt',
'test_world_traversed.txt',
'test2.zip',
'text_tools_sample.csv',
'tool_list.txt',
'toolbox_network_download_proxy.html',
'toolbox_network_password_protected.html',
'toolbox_network_protected_page.html',
'tools.txt',
'UNDO.SQL'
]

# run all tests in tests folder
all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)    

def wipe_file(fname):
    """
    removes test file left behind without worrying if they cant be 
    deleted. Used only to make a git status look clean.
    """
    try:
        os.remove(fname)
        print('deleted ' + fname)
    except Exception as ex:
        print('ERROR - cant delete ' + fname + ' : ' + str(ex))
        
print('Did the tests fail.... DID YOU TURN ON VIRTUALENV!   ". ~/p von"')
print('WIPING ALL TEST RESULTS - PRESS CTRL C TO STOP')

time.sleep(5)

for f in files_to_wipe:
    wipe_file(f)    



