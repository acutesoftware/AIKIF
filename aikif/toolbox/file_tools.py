#!/usr/bin/python3
# coding: utf-8
# file_tools.py

import os
import glob
import shutil
import aikif.lib.cls_filelist as mod_fl

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
print(root_folder)
fname = root_folder + os.sep + 'tests/test_results/cls_filelist_results1.csv'



def get_filelist(fldr):
    """
    extract a list of files from fldr
    """
    print('collecting filelist from ' + fldr)
    lst = mod_fl.FileList([fldr], ['*.*'], [],  '')
    return lst.get_list()

def delete_files_in_folder(fldr):
    fl = glob.glob(fldr + os.sep + '*.*')
    for f in fl:
        os.remove(f)
 

def copy_files_to_folder(src, dest):
    """
    copies all the files from src to dest folder
    """
    print('copying files from ' + src + '\nto ' + dest)
    
    all_files = glob.glob(src + os.sep + '*.txt')
    for f in all_files:
        print(' ... copying ' + os.path.basename(f))
        try:
            shutil.copy2(f , dest)
        except Exception as ex:
            print('ERROR copying ' + f + '\n to ' + dest + str(ex))
 
