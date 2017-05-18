#!/usr/bin/python3
# -*- coding: utf-8 -*-
# config.py     written by Duncan Murray 28/7/2014

import os
import sys
fldrs = {}
logs = {}
params = {}


"""
# path for personal data location  (TODO - you need to modify this line below!)
if sys.platform == 'linux':
    if os.path.exists('/home/duncan'):
        hme = '/home/duncan/'
        core_folder = '/home/duncan/dev/src/python/AIKIF'
        print('config.py : running locally on duncans PC!')
    else:
        hme = os.getcwd()        
        core_folder = os.getcwd()
        print('config.py : running on CI build!')
else:
    hme = 'T:\\user\\'
    core_folder = 'T:\\user\\dev\\src\\python\\AIKIF'
"""
 
def get_root_folder():
    """
    returns the home folder and program root depending on OS
    """
    locations = {
     'linux':{'hme':'/home/duncan/', 'core_folder':'/home/duncan/dev/src/python/AIKIF'},
     'win32':{'hme':'T:\\user\\',    'core_folder':'T:\\user\\dev\\src\\python\\AIKIF'},
     'cygwin':{'hme':os.getcwd() + os.sep,    'core_folder':os.getcwd()},
     'darwin':{'hme':os.getcwd() + os.sep,    'core_folder':os.getcwd()}
    }
    hme = locations[sys.platform]['hme']
    core_folder = locations[sys.platform]['core_folder']

    if not os.path.exists(core_folder):
        hme = os.getcwd()        
        core_folder = os.getcwd()
        print('config.py : running on CI build (or you need to modify the paths in config.py)')
    return hme, core_folder

 
hme, core_folder = get_root_folder()    

fldrs['localPath'] = hme + 'AIKIF' + os.sep
fldrs['log_folder'] = hme + 'AIKIF' + os.sep + 'log'
fldrs['pers_data'] = hme + 'AIKIF' + os.sep + 'pers_data'
fldrs['pers_credentials'] = hme + 'AIKIF'  + os.sep + 'pers_data' + os.sep + 'credentials' 


# FOR DEVELOPMENT
core_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
fldrs['root_path'] = core_folder
fldrs['public_data_path'] = core_folder + os.sep + 'aikif' + os.sep + 'data'
fldrs['program_path'] = os.path.abspath(core_folder + os.sep + 'aikif') 

# user defined parameters 
params['AIKIF_version'] = '0.1.9'
params['AIKIF_deploy'] = 'DEV'


# names of logfiles for AIKIF
logs['logFileProcess'] = fldrs['localPath'] + 'log' + os.sep + 'process.log'
logs['logFileSource'] = fldrs['localPath'] + 'log' + os.sep + 'source.log'
logs['logFileCommand'] = fldrs['localPath'] + 'log' + os.sep + 'command.log'
logs['logFileResult'] = fldrs['localPath'] + 'log' + os.sep + 'result.log'

# index files
#                         fldrs['public_data_path'] + os.sep  + 'index' + os.sep + 'ndxWordsToFilesLecture.txt',
#                         fldrs['localPath'] + 'diary' + os.sep + 'filelister2014.csv',

params['index_files'] = [fldrs['public_data_path'] + os.sep  + 'index' + os.sep + 'ndxAll.txt',
                         fldrs['localPath'] + 'pers_data' + os.sep + 'pers_index_final.txt',
                         fldrs['localPath'] + 'pers_data' + os.sep + 'ndx_PCusage.txt'
                        ]



def read_credentials(fname):
    """
    read a simple text file from a private location to get
    username and password
    """
    with open(fname, 'r') as f:
        username = f.readline().strip('\n')
        password = f.readline().strip('\n')
    return username, password

    
def show_config():
    """
    module intended to be imported in most AIKIF utils
    to manage folder paths, user settings, etc.
    Modify the parameters at the top of this file to suit
    """
    res = ''
    res += '\n---------- Folder Locations ---------\n'
    for k,v in list(fldrs.items()):
        res += str(k) + ' = ' + str(v) + '\n'
    
    res += '\n---------- Logfiles ---------\n'
    for k,v in list(logs.items()):
        res += str(k) + ' = ' + str(v) + '\n'
        
    res += '\n---------- Parameters ---------\n'
    for k,v in list(params.items()):
        res += str(k) + ' = ' + str(v) + '\n'
    print(("\nusage from other programs - returns " + fldr_root()))
    return res
    
def fldr_root():
    return fldrs['root_path']

if __name__ == '__main__':    
    show_config()
