#!/usr/bin/python3
# coding: utf-8
# file_tools.py

import os
import glob
import shutil
import aikif.lib.cls_filelist as mod_fl

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "..") 
print('root_folder = ', root_folder)
fname = root_folder + os.sep + 'tests/test_results/cls_filelist_results1.csv'



def get_filelist(fldr):
    """
    extract a list of files from fldr
    """
    print('collecting filelist from ' + fldr)
    lst = mod_fl.FileList([fldr], ['*.*'], [os.sep + 'venv', os.sep + 'venv2', os.sep + '__pycache__', os.sep + 'htmlcov'],  '')
    return lst.get_list()

def delete_file(f, ignore_errors=False):
    """
    delete a single file
    """
    try:
        os.remove(f)
    except Exception as ex:
        if ignore_errors:
            return
        print('ERROR deleting ' + f + '\n' + str(ex))

def delete_files_in_folder(fldr):
    """
    delete all files in folder 'fldr'
    """
    print('delete_files_in_folder = ', fldr)
    fl = glob.glob(fldr + os.sep + '*.*')
    for f in fl:
        delete_file(f, True)
 
def copy_file(src, dest):
    """
    copy single file
    """
    try:
        shutil.copy2(src , dest)
    except Exception as ex:
        print('ERROR copying ' + src + '\n to ' + dest + str(ex))
    
def copy_files_to_folder(src, dest, xtn='*.txt'):
    """
    copies all the files from src to dest folder
    """
    print('copying files from ' + src + '\nto ' + dest)
    
    all_files = glob.glob(src + os.sep + xtn)
    for f in all_files:
        print(' ... copying ' + os.path.basename(f))
        copy_file(f, dest)
 
