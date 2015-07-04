#!/usr/bin/python3
# coding: utf-8
# file_tools.py

import os
import aikif.lib.cls_filelist as mod_fl
import aikif.lib.cls_file as mod_file

def TEST():
    print('local testing of file_tools')
    download('http://test.com/a.txt', '~/downloads')
    print(''.join(sorted(set('the quick brown fox jumped over the lazy dog'))))

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
 
 

if __name__ == '__main__':
    TEST()    
