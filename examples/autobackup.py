# -*- coding: utf-8 -*-
# autobackup.py    written by Duncan Murray 9/8/2014

import os
import shutil
import sys
import math
from random import randint 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)
#import AI.environments.worlds as my_world
import AI.agents.gather.agent_filelist as agt
import AI.AIKIF_utils as aikif

LOG_LEVEL = 2

def main():
    """
    autobackup program implemented using AIKIF agent
    """
    log_folder      = "T:\\user\\AIKIF\\log\\agents"
    dest_folder     = "E:\\backup"

    backups = [
{"name":"AIKIF Code", "fldr":"T:\\user\\dev\\src\\python\\AI", "base_path_ignore":"T:\\user\\"},
{"name":"AIKIF logs", "fldr":"T:\\user\\AIKIF", "base_path_ignore":"T:\\user\\"},
{"name":"Documents", "fldr":"T:\\user\\docs\\business", "base_path_ignore":"T:\\user\\"},
{"name":"eBooks", "fldr":"Z:\\DATA\\eBooks\\000_Computer_Science", "base_path_ignore":"Z:\\DATA\\"},
]
    
    for backup in backups:
        autobackup(backup["name"], backup["fldr"], backup["base_path_ignore"], dest_folder)

def autobackup(nme, fldr, ignore_root, dest_folder):
    aikif.LogCommand('autobackup - ' + nme, 'autobackup.py')
    print('Starting backup "' + nme + '" - ' +  fldr)
    fl = agt.FileListAgent(nme, fldr, True, 1, [])
    for num, file in enumerate(fl.lst.get_list()):
        backup_file(file, dest_folder, ignore_root)
    print("Backed up " + "{0:,d}".format(num) + " files \t[" + nme + "]")


        
def backup_file(fname, dest_root_folder, base_path_ignore):
    #assert not os.path.isabs(fname)
    #print("dest_root_folder = " + dest_root_folder)
    dest_folder =  os.path.join(dest_root_folder, os.path.dirname(fname)[len(base_path_ignore):])
    #print("copying " + fname + " to " + dest_folder)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder) # create all directories, raise an error if it already exists
    try:
        shutil.copy2(fname, dest_folder)    
        print("Backed up ", fname)
    except: 
        print("ERROR - cant backup up ")
        try:
            print(fname)
        except:
            print("Wow - that filename really cant be printed!")
    

    
main()
