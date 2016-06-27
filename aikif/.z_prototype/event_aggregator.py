#!/usr/bin/python3
# -*- coding: utf-8 -*-
# event_aggregator.py

import os
import sys
import random

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, root_fldr)
root_path = root_fldr + os.sep + 'samples'

import config
import cls_log
import core_data
import aikif.lib.cls_filelist as fl 
 
password_folder = config.fldrs['pers_credentials']
log_folder = config.fldrs['log_folder'] 
data_folder = config.fldrs['pers_data']
#op_folder = os.path.join(config.fldrs['localPath'], '_PROD','data','core')
op_folder = os.path.join(config.fldrs['localPath'], '_DEV','data','core')

lg = cls_log.Log(log_folder)
usr = 'djm'     # file extenstions for all data files    

def main():
    """
    Generates selection of different events from various sources
    
    print('password_folder = ', password_folder)
    print('log_folder      = ', log_folder)
    print('data_folder     = ', data_folder)
    print('op_folder       = ', op_folder)
    
    Screenshot folder is a text file as follows:
        Minecraft|C:\\Users\\Duncan\AppData\Roaming\\.minecraft\\screenshots
        Steam|E:\\games\\Steam\\userdata    
    
    """
    if '_PROD' in op_folder:
        correct = random.choice(['y', '1', ' ', '#'])
        ans = input('Saving to PROD - press ' + correct + ' to continue')
        if ans != correct:
            lg.record_process('event_aggregator.py', 'abort process on startup')
            sys.exit()
            
    lg.record_command('event_aggregator.py', 'generating events to op_folder=' + op_folder)        
    add_manual_events()
    add_screenshots()
    create_diary(data_folder)
    

def create_diary(fldr):
    """
    find all created event files in folder and generate
    diary files (and display)
    
    """
    print('generating diary from files in ' + fldr)
    fles = fl.FileList([op_folder], ['*.' + usr], [], '')
    files = fles.get_metadata()
    for file_dict in files:
        print('  reading ' + str(file_dict['fullfilename'])) 
        with open(str(file_dict['fullfilename']), 'r') as f:
            hdr = f.readline().strip('"').split(',')
            print('hdr = ', hdr)
            
    
    
    
def add_manual_events():
    """
    add events manually from code, and sample text files
    """
    hdr = ['date', 'category', 'details']
    ev_man = core_data.CoreTable(op_folder, tpe='Events', user=usr, header=hdr)
    op_file = ev_man.get_filename('Manual')
    if os.path.exists(op_file):
        os.remove(op_file)
        
    lg.record_process('event_aggregator.py', 'loading manual events')
    ev_man.add(core_data.CoreDataWhen('Build Event Aggregator', ['2016-06-22', 'Dev', 'Started example to generate diary with AIKIF']))

    ev_man.save('Manual', add_header='Y')
    #print(ev_man.get_filename('ManualTEST'))
    #ev_man.generate_diary()    

  
def add_screenshots():
    with open(os.path.join(data_folder,'screenshot.folders'), 'r') as f:
        for line in f:
            if line.strip('\n') != '':
                cat, folder = line.strip('\n').split('|')
                collect_screenshots(cat, folder)

  

def collect_screenshots(cat, folder, file_tag='FileUsage' ):
    """
    add events based on screenshot creation
    """
    hdr = ['date', 'category', 'size', 'filename', 'path']
    ev = core_data.CoreTable(op_folder, tpe='Events', user=usr, header=hdr)
    op_file = ev.get_filename(file_tag + '-' + cat)
    if os.path.exists(op_file):
        os.remove(op_file)
        
    
    # get collection of screenshots
    fl_filename = os.path.join(op_folder,'filelist_screenshots.csv')
    fles = fl.FileList([folder], ['*.jpg', '*.png'], ['\\thumbnails\\'], fl_filename)
    fles.save_filelist(fl_filename, ["name", "path", "size", "date"])
    files = fles.get_metadata()
    for file_dict in files:
        ev.add(core_data.CoreDataWhen(cat, [file_dict["date"], file_tag, file_dict["size"], file_dict["name"],file_dict["path"] ]))

    lg.record_process('event_aggregator.py', 'created ' + str(len(files)) + ' events for ' + cat + '-' + file_tag)
    ev.save(file_tag, add_header='Y')


  
    
if __name__ == '__main__':
    main()

