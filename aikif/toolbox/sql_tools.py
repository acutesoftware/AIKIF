#!/usr/bin/python3
# coding: utf-8
# sql_tools.py

import os
import aikif.lib.cls_filelist as mod_fl

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
print(root_folder)


def count_lines_in_file(src_file ):
    """
    test function.
    """
    tot = 0
    res = ''
    try:
        with open(src_file, 'r') as f:
            for line in f:
                tot += 1
            res = str(tot) + ' recs read'       
    except:
        res = 'ERROR -couldnt open file'
    return res 

    
def load_txt_to_sql(tbl_name, src_file, op_folder ):
    """
    creates a SQL loader script to load a text file into a database
    and then executes it.
    """
    res = ''
    fname_create_script = op_folder + os.sep + 'CREATE_' + tbl_name + '.SQL'
    fname_backout_file  = op_folder + os.sep + 'BACKOUT_' + tbl_name + '.SQL'
    fname_control_file  = op_folder + os.sep + tbl_name + '.CTL'
    fname_batch_file    = op_folder + os.sep + 'LOAD_' + tbl_name + '.BAT'
    
    ctl_data_lines = []
    cols = get_cols(src_file)
    create_script_staging_table(fname_create_script, tbl_name, cols)    
    create_file(fname_backout_file, 'DROP TABLE ' + tbl_name + ' CASCADE CONSTRAINTS;\n')
    create_CTL(fname_control_file, tbl_name, src_file, cols, 'TRUNCATE')
    create_BAT(fname_batch_file, tbl_name, src_file)
    
    
######################################
# Internal Functions and Classes
######################################        
   
def create_script_staging_table(create_file, output_table, col_list):
        
    ddl_text = '---------------------------------------------\n'
    ddl_text += '-- CREATE Table - ' + output_table + '\n'
    ddl_text += '---------------------------------------------\n'
    ddl_text += ''
    ddl_text += 'CREATE TABLE ' + output_table + ' (\n  '
    ddl_text += '  '.join([col + ' VARCHAR2(200), \n' for col in col_list])
    ddl_text += '  REC_EXTRACT_DATE DATE \n' # + src_table + '; \n'
    ddl_text += ');\n'

    with open(create_file, "w") as f:
        f.write(ddl_text)
    

def create_BAT(fname, tbl_name, src_file):
    create_file(fname, 'REM Loads ' + tbl_name + ' from ' + src_file + '\n')
    
def create_CTL(fname, tbl_name, load_file, col_list, TRUNC_OR_APPEND): 
    with open(fname, 'w') as ct:
        ct.write('LOAD DATA\n')
        ct.write(TRUNC_OR_APPEND + '\n')
        ct.write('into table ' + tbl_name  + '\n')
        ct.write("fields terminated by '|'\n")
        #ct.write('Optionally Enclosed  by '"\'\n')
        ct.write('TRAILING NULLCOLS\n')
        ct.write('(\n')
        ct.write(',\n'.join(c for c in col_list ))    
        ct.write(')\n')

def get_CTL_log_string(tbl_name, fname, load_file):
    ctl_details = ''
    ctl_details += " log='logs" + os.sep + tbl_name  + ".log'"
    ctl_details += " bad='logs" + os.sep + tbl_name  + ".bad'"
    ctl_details += " discard='logs" + os.sep + tbl_name  + ".discard'"
    ctl_details += " control=" + load_file  
    ctl_details += " data='" + fname + "'\n"
    return ctl_details
   

            
def get_cols(fname):
    with open(fname, 'r') as f:
        cols = f.readline().strip('\n').split('|')
    return cols
    


def create_file(fname, txt): 
    with open(fname, 'w') as f:
        f.write(txt + '\n')

    
def append_to_file(fname, txt): 
    with open(fname, 'a') as f:
        f.write(txt + '\n')
    
