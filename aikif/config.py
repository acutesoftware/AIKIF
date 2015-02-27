# -*- coding: utf-8 -*-
# config.py     written by Duncan Murray 28/7/2014

import sys
import os

fldrs = {}
logs = {}
params = {}

# path for personal data location  (TODO - you need to modify this line below!)
fldrs['localPath'] = 'T:\\user\\AIKIF\\' 
fldrs['log_folder'] = 'T:\\user\\AIKIF\\log' 
fldrs['pers_data'] = 'T:\\user\\AIKIF\\pers_data' 

# user defined parameters 
params['AIKIF_version'] = '0.0.7'
params['AIKIF_deploy'] = 'DEV'


# names of logfiles for AIKIF
logs['logFileProcess'] = fldrs['localPath'] + 'log' + os.sep + 'process.log'
logs['logFileSource'] = fldrs['localPath'] + 'log' + os.sep + 'source.log'
logs['logFileCommand'] = fldrs['localPath'] + 'log' + os.sep + 'command.log'
logs['logFileResult'] = fldrs['localPath'] + 'log' + os.sep + 'result.log'


# useful folder locations used by programs - don't modify
fldrs['root_path'] = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
fldrs['program_path'] = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
fldrs['public_data_path'] = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'data') 

#print('DEBUG:NOTE - origi folder paths may NOT work after pip install - todo\n')
#print('DEBUG:config.py : fldrs[root_path] = ' + fldrs['root_path'])
if 'site-packages' in fldrs['root_path']:  
    fldrs['root_path'] = fldrs['localPath'] 
    fldrs['public_data_path'] = fldrs['log_folder']


# index files
#                         fldrs['public_data_path'] + os.sep  + 'index' + os.sep + 'ndxWordsToFilesLecture.txt',
#                         fldrs['localPath'] + 'diary' + os.sep + 'filelister2014.csv',

params['index_files'] = [fldrs['public_data_path'] + os.sep  + 'index' + os.sep + 'ndxAll.txt',
                         fldrs['localPath'] + 'pers_data' + os.sep + 'pers_index_final.txt',
                         fldrs['localPath'] + 'pers_data' + os.sep + 'ndx_PCusage.txt'
                        ]


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