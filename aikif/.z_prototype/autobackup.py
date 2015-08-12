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

{"name":"rawdata", "fldr":"T:\\user\\dev\\src\\python\\rawdata", "base_path_ignore":"T:\\user\\"},
{"name":"AIKIF logs", "fldr":"T:\\user\\AIKIF", "base_path_ignore":"T:\\user\\"},
{"name":"Documents", "fldr":"T:\\user\\docs\\articles", "base_path_ignore":"T:\\user\\"},
 
USE THIS FOR EVERYTHING = 2015 Aug


{"name":"test-rawdata", "fldr":"R:\\", "base_path_ignore":"R:\\", "dest_folder": root_dest + "r_back"},
    """
    log_folder    = aikif.localPath + 'log\\autobackup\\'
    ndx_file      = aikif.localPath + 'index\\files_autobackup.ndx'
    root_dest   = "F:\\_home_BK\\"

    backups = [
{"name":"user", "fldr":"S:\\", "base_path_ignore":"S:\\", "dest_folder": root_dest + "user_bk"},
{"name":"photo", "fldr":"P:\\", "base_path_ignore":"P:\\", "dest_folder": root_dest + "photo_bk"},
{"name":"music", "fldr":"M:\\", "base_path_ignore":"M:\\", "dest_folder": root_dest + "music_bk"},
 ]
    
    
    aikif.LogResult("Started autobackup.py")
    for backup in backups:
        autobackup(backup["name"], backup["fldr"], backup["base_path_ignore"], backup["dest_folder"], log_folder, ndx_file)

def autobackup(nme, fldr, ignore_root, dest_folder, log_folder, ndx_file):
    aikif.LogCommand('autobackup - ' + nme, 'autobackup.py')
    print('Starting backup "' + nme + '" - ' +  fldr)
    fl = agt.FileListAgent(nme, fldr, True, log_folder ) # ['name', 'size', 'date', 'path'])
    # , name,  fldr, running,  log_folder):
    
    fl.lst.check_files_needing_synch(dest_folder, ignore_root)
    
    for file in fl.lst.get_dirty_filelist():
        if backup_file(file, dest_folder, ignore_root) != True:
            #fl.lst.add_failed_file(file, dest_folder)
            fl.lst.add_failed_file(file)
        
    bk_files = len(fl.lst.get_dirty_filelist())
    tot_files = len(fl.lst.get_list())
    aikif.LogResult("Backed up " + str(bk_files) + " / " + str(tot_files) + " files  for '" + nme + "'" , "autobackup.py")
    
    # optional - update indexes and log file usage
    fl.lst.save_file_usage(log_folder, nme)
    fl.lst.update_indexes(ndx_file)
        
        
def backup_file(fname, dest_root_folder, base_path_ignore):
    final_folder =  os.path.join(dest_root_folder, os.path.dirname(fname)[len(base_path_ignore):])
    if not os.path.exists(final_folder):
        try:
            os.makedirs(final_folder) # create all directories, raise an error if it already exists
        except:
            print('Error - cant create directory')
            
    try:
        shutil.copy2(fname, final_folder)
        return True
    except: 
        return False

    
main()
