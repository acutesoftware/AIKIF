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

    
def load_txt_to_sql(tbl_name, src_file_and_path, src_file, op_folder):
    """
    creates a SQL loader script to load a text file into a database
    and then executes it.
    Note that src_file is 
    """
    res = ''
    if op_folder == '':
        pth = ''
    else:
        pth = op_folder + os.sep
    
    fname_create_script = pth + 'CREATE_' + tbl_name + '.SQL'
    fname_backout_file  = pth + 'BACKOUT_' + tbl_name + '.SQL'
    fname_control_file  = pth + tbl_name + '.CTL'
    fname_batch_file    = pth + 'LOAD_' + tbl_name + '.BAT'
    
    ctl_data_lines = []
    cols = read_csv_cols_to_table_cols(src_file)
    create_script_staging_table(fname_create_script, tbl_name, cols)    
    create_file(fname_backout_file, 'DROP TABLE ' + tbl_name + ' CASCADE CONSTRAINTS;\n')
    create_CTL(fname_control_file, tbl_name, src_file, cols, 'TRUNCATE')
    
def create_BAT_file(fname_batch_file, tbl_name, src_file_and_path, src_file, par_file):
    with open(fname_batch_file, 'w') as f:
        f.write('REM Loads ' + tbl_name + ' from ' + src_file + '\n')
        f.write("sqlldr parfile='" + par_file + "'" + get_CTL_log_string(tbl_name, src_file_and_path))

       
    
######################################
# Internal Functions and Classes
######################################        
   

def create_script_staging_table(fname_create, output_table, col_list):
        
    ddl_text = '---------------------------------------------\n'
    ddl_text += '-- CREATE Table - ' + output_table + '\n'
    ddl_text += '---------------------------------------------\n'
    ddl_text += ''
    ddl_text += 'CREATE TABLE ' + output_table + ' (\n  '
    ddl_text += '  '.join([col + ' VARCHAR2(200), \n' for col in col_list])
    ddl_text += '  REC_EXTRACT_DATE DATE \n' # + src_table + '; \n'
    ddl_text += ');\n'

    with open(fname_create, "w") as f:
        f.write(ddl_text)

def create_CTL(fname, tbl_name, load_file, col_list, TRUNC_OR_APPEND, delim=','): 
    with open(fname, 'w') as ct:
        ct.write('LOAD DATA\n')
        ct.write(TRUNC_OR_APPEND + '\n')
        ct.write('into table ' + tbl_name  + '\n')
        ct.write("fields terminated by '" + delim + "'\n")
        #ct.write('Optionally Enclosed  by '"\'\n')
        ct.write('TRAILING NULLCOLS\n')
        ct.write('(\n')
        ct.write(',\n'.join(c for c in col_list ))    
        ct.write(')\n')

def get_CTL_log_string(tbl_name, fname):
    ctl_details = ''
    ctl_details += " log='" + tbl_name  + ".log'"
    ctl_details += " bad='" + tbl_name  + ".bad'"
    ctl_details += " discard='" + tbl_name  + ".discard'"
    ctl_details += " control=" + tbl_name + '.CTL'  
    ctl_details += " data='" + fname + "'\n"
    return ctl_details
   

            
def get_cols(fname):
    with open(fname, 'r') as f:
        cols = f.readline().strip('\n').split('|')
    return cols
    
def read_csv_cols_to_table_cols(fname):
    with open(fname, 'r') as f:
        cols = f.readline().strip('\n').split(',')
    return [c.upper().strip(' ').replace(' ', '_') for c in cols ]
    

def create_file(fname, txt): 
    with open(fname, 'w') as f:
        f.write(txt + '\n')
