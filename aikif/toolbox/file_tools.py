#!/usr/bin/python3
# coding: utf-8
# file_tools.py

import os
import aikif.lib.cls_filelist as mod_fl
import aikif.lib.cls_file as mod_file

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
print(root_folder)
fname = root_folder + os.sep + 'tests/test_results/cls_filelist_results1.csv'

def TEST():
    print('local testing of file_tools')
    download('http://test.com/a.txt', '~/downloads')
    #print(''.join(sorted(set('the quick brown fox jumped over the lazy dog'))))
    lst = get_filelist(root_folder + os.sep + 'toolbox')
    #print(lst)
    #lst1 = mod_fl.FileList([root_folder + os.sep + 'toolbox'], ['*.py'], [],  fname)
    #print(lst1.get_list())
    
def download(url, dest_file):
    """
    downloads the file at url to dest_file 
    """
    print('downloading ' + url + ' to ' + dest_file)
    
def get_filelist(fldr):
    """
    extract a list of files from fldr
    """
    print('collecting filelist from ' + fldr)
    lst = mod_fl.FileList([fldr], ['*.*'], [],  '')
    return lst.get_list()
 

if __name__ == '__main__':
    TEST()    
