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
    autobackup program implemented using AIKIF agent.

    TODO :
    the cls_filelist (or agent_filelist) needs to
    have a class called FileListGroup which takes an autobackup
    name and set of files AS WELL AS a destination folder.
    This way every file has TWO locations - a master and a backup.
    
    The filelist will manage collecting the metadata of files and 
    also checking the backup version and put a flag DIRTY/CLEAN 
    against each file in the list.
    
    You then need to have an iterate method in the class which iterates
    not only the filename but other metadata parameters (multi methods)
    
    Then, all the autobackup.py program needs to do is iterate 
    through the list of files in each filelistgroup and backup
    the dirty files.
    
    Also, new apps fileList server can use this collection for 
    quick viewing.
    
{"name":"Documents", "fldr":"T:\\user\\docs\\business", "base_path_ignore":"T:\\user\\"},
{"name":"eBooks", "fldr":"Z:\\DATA\\eBooks\\000_Computer_Science", "base_path_ignore":"Z:\\DATA\\"},
    
    """
    log_folder      = "T:\\user\\AIKIF\\log\\agents"
    dest_folder     = "E:\\backup"

    backups = [
{"name":"AIKIF Code", "fldr":"T:\\user\\dev\\src\\python\\AI\\examples", "base_path_ignore":"T:\\user\\"},
{"name":"AIKIF logs", "fldr":"T:\\user\\AIKIF", "base_path_ignore":"T:\\user\\"},
{"name":"Documents", "fldr":"T:\\user\\docs\\articles", "base_path_ignore":"T:\\user\\"},
]
    
    for backup in backups:
        autobackup(backup["name"], backup["fldr"], backup["base_path_ignore"], dest_folder)

def autobackup(nme, fldr, ignore_root, dest_folder):
    aikif.LogCommand('autobackup - ' + nme, 'autobackup.py')
    print('Starting backup "' + nme + '" - ' +  fldr)
    fl = agt.FileListAgent(nme, fldr, True, 1, [])
    
    
    """ code below works with backup for orig version PRIOR to FileListGroups
    for num, file in enumerate(fl.lst.get_list()):
        backup_file(file, dest_folder, ignore_root)
    print("Backed up " + "{0:,d}".format(num) + " files \t[" + nme + "]")
    """

        
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
