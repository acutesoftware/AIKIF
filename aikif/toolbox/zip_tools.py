#!/usr/bin/python3
# coding: utf-8
# zip_tools.py

import os

def TEST():
    print('local testing of zip_tools')
    extract_all('test.zip', os.getcwd())

def extract_all(zipfile, dest_folder):
    """
    reads the zip file, determines compression
    and unzips recursively until source files 
    are extracted 
    """
    z = ZipFile(zipfile)
    print(z)
    z.extract(os.getcwd() + os.sep + 'unzipped')
    
    
    
class ZipFile(object):
    def __init__(self, fname):
        self.fname = fname
        self.type = self._determine_zip_type()
    
    def __str__(self):
        return self.fname + ' is type ' + self.type
        
    def _determine_zip_type(self):
        return 'ZIP'
    
    def extract(self, dest_fldr):
        """
        unzip the file contents to the dest_folder
        (create if it doesn't exist)
        and then return the list of files extracted
        """
        print('extracting to ' + dest_fldr)
        return [dest_fldr + os.sep + 'test.gz']
    
if __name__ == '__main__':
    TEST()    
