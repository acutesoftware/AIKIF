# -*- coding: utf-8 -*-
# config.py     written by Duncan Murray 28/7/2014

import sys
import os

fldrs = {}
logs = {}
params = {}

# path for personal data location
fldrs['localPath'] = 'T:\\user\\AIKIF\\' 

# user defined parameters 
params['AIKIF_version'] = '0.1'
params['AIKIF_deploy'] = 'DEV'


# names of logfiles for AIKIF
logs['logFileProcess'] = fldrs['localPath'] + 'log' + os.sep + 'process.log'
logs['logFileSource'] = fldrs['localPath'] + 'log' + os.sep + 'source.log'
logs['logFileCommand'] = fldrs['localPath'] + 'log' + os.sep + 'command.log'
logs['logFileResult'] = fldrs['localPath'] + 'log' + os.sep + 'result.log'

# useful folder locations used by programs - don't modify
fldrs['root_path'] = os.path.dirname(os.path.abspath(__file__))
fldrs['program_path'] = fldrs['root_path'] + os.sep + "AI"
fldrs['public_data_path'] = fldrs['root_path'] + os.sep + "data"

def show_config():
    """
    module intended to be imported in most AIKIF utils
    to manage folder paths, user settings, etc.
    Modify the parameters at the top of this file to suit
    """
    
    print("\n---------- Folder Locations ---------")
    for k,v in fldrs.items():
        print(k,v)
    
    print("\n---------- Logfiles ---------")
    for k,v in logs.items():
        print(k,v)
        
    print("\n---------- Parameters ---------")
    for k,v in params.items():
        print(k,v)
    print("\nusage from other programs - returns " + fldr_root())
    
def fldr_root():
    return fldrs['root_path']

if __name__ == '__main__':    
    show_config()