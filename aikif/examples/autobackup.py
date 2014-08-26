# -*- coding: utf-8 -*-
# autobackup.py    written by Duncan Murray 9/8/2014

import os
import shutil
import sys
import math
from random import randint 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)
print(root_folder)
#import aikif.environments.worlds as my_world
import agents.gather.agent_filelist as agt  # Note - when deployed, prefix with aikif.
import AIKIF_utils as aikif                 # Note - when deployed, prefix with aikif.

LOG_LEVEL = 2

def main():
    """
    autobackup program implemented using AIKIF agent.
    
{"name":"Documents", "fldr":"T:\\user\\docs\\business", "base_path_ignore":"T:\\user\\"},
{"name":"eBooks", "fldr":"Z:\\DATA\\eBooks\\000_Computer_Science", "base_path_ignore":"Z:\\DATA\\"},
    
    """
    log_folder    = aikif.localPath + 'log\\autobackup\\'
    ndx_file      = aikif.localPath + 'index\\files_autobackup.ndx'
    dest_folder   = "E:\\backup"

    backups = [
{"name":"AIKIF Code", "fldr":"T:\\user\\dev\\src\\python\\AI", "base_path_ignore":"T:\\user\\"},
{"name":"AIKIF logs", "fldr":"T:\\user\\AIKIF", "base_path_ignore":"T:\\user\\"},
{"name":"Documents", "fldr":"T:\\user\\docs\\articles", "base_path_ignore":"T:\\user\\"},
]
    
    
    aikif.LogResult("Started backup to " + dest_folder, "autobackup.py")
    for backup in backups:
        autobackup(backup["name"], backup["fldr"], backup["base_path_ignore"], dest_folder, log_folder, ndx_file)

def autobackup(nme, fldr, ignore_root, dest_folder, log_folder, ndx_file):
    aikif.LogCommand('autobackup - ' + nme, 'autobackup.py')
    print('Starting backup "' + nme + '" - ' +  fldr)
    fl = agt.FileListAgent(nme, fldr, True, 1, log_folder, ['name', 'size', 'date', 'path'])
    
    fl.lst.check_files_needing_synch(dest_folder, ignore_root)
    
    for file in fl.lst.get_dirty_filelist():
        if backup_file(file, dest_folder, ignore_root) != True:
            fl.lst.add_failed_file(file, dest_folder)
        
    bk_files = len(fl.lst.get_dirty_filelist())
    tot_files = len(fl.lst.get_list())
    aikif.LogResult("Backed up " + str(bk_files) + " / " + str(tot_files) + " files  for '" + nme + "'" , "autobackup.py")
    
    # optional - update indexes and log file usage
    fl.lst.save_file_usage(log_folder, nme)
    fl.lst.update_indexes(ndx_file)
        
        
def backup_file(fname, dest_root_folder, base_path_ignore):
    dest_folder =  os.path.join(dest_root_folder, os.path.dirname(fname)[len(base_path_ignore):])
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder) # create all directories, raise an error if it already exists
    try:
        shutil.copy2(fname, dest_folder)
        return True
    except: 
        return False

    
main()
