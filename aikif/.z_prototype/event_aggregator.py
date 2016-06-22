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

    ev_man.save('Manual')
    #print(ev_man.get_filename('ManualTEST'))
    #ev_man.generate_diary()    

  

def add_screenshots(file_tag='Screenshot'):
    """
    add events based on screenshot creation
    """
    hdr = ['date', 'category', 'size', 'filename', 'path']
    ev = core_data.CoreTable(op_folder, tpe='Events', user=usr, header=hdr)
    op_file = ev.get_filename(file_tag)
    if os.path.exists(op_file):
        os.remove(op_file)
        
    
    # get collection of screenshots
    import aikif.lib.cls_filelist as fl 
    
    fldrs_to_search = []
    with open(os.path.join(data_folder,'screenshot.folders'), 'r') as f:
        for line in f:
            if line.strip('\n') != '':
                fldrs_to_search.append(line.strip('\n'))
    
    #print('fldrs_to_search = ', fldrs_to_search)
    fl_filename = os.path.join(op_folder,'filelist_screenshots.csv')
    fles = fl.FileList(fldrs_to_search, ['*.jpg', '*.png'], [], fl_filename)
    fles.save_filelist(fl_filename, ["name", "path", "size", "date"])
    files = fles.get_metadata()
    for file_dict in files:
        ev.add(core_data.CoreDataWhen('Screenshot', [file_dict["date"], 'Games', file_dict["size"], file_dict["name"],file_dict["path"] ]))

    lg.record_process('event_aggregator.py', 'created ' + str(len(files)) + ' events from screenshots')
    
        
    print(file_dict)
    ev.save(file_tag)


  
    
if __name__ == '__main__':
    main()

