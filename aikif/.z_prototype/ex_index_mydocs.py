#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ex_index_mydocs.py
# Example program to index all personal data for keyword searches using AIKIF.
# Source data is taken from Acute Softwares Diary and FileLister

import os
import sys
import aikif.config as mod_cfg
import aikif.lib.cls_filelist as mod_fl

  
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder)  
import index as ndx
  
  
local_folder = mod_cfg.fldrs['pers_data'] + os.sep + 'diary' + os.sep
diary_folder = os.path.join('T:\\','user','AIKIF','diary','netDiary_backup')

print('diary_folder = ', diary_folder)
print('local_folder = ', local_folder)

manual_files_to_index = []

diary_range_filter = 'D*.DAT'

ndxFile = 'T:\\user\\AIKIF\\pers_data\\ndx_temp.txt'
ndxFile_final = 'T:\\user\\AIKIF\\pers_data\\ndx_final.txt'

acute_diary_file = os.path.join(local_folder, 'acute_diary.txt')

def main():
    try:
        os.remove(ndxFile)
    except Exception:
        pass

    #convert_acute_diary_files_to_text(diary_folder, acute_diary_file)
    #ndx.buildIndex(acute_diary_file, ndxFile, 'Y', 'N')	# run the index routine

    
    
    all_files = add_diary_files_to_list(manual_files_to_index, diary_folder)	
    numFiles = 0
    for f in all_files:
        try:
            numFiles += 1
            print('indexing ', str(numFiles) , ' of ', str(len(all_files)), ' : ', f)
            ndx.buildIndex(f, ndxFile, 'Y', 'N')	# run the index routine
        except Exception:
            print('ERROR - cant index file ', f)
    
    
    print('consolidating.... ')		
    ndx.consolidate(ndxFile, ndxFile_final)	
    print('Done!')		


def add_diary_files_to_list(lst, fldr):
    """ 
    adds all Diary files from folder to the lst   
    """
    fl = mod_fl.FileList([fldr], [diary_range_filter], ["__pycache__", ".git"], "temp.csv")
 
    for f in fl.get_list():
        lst.append(f)
    return lst
       

def convert_acute_diary_files_to_text(fldr, opfolder):
    """
    Takes a folder of Acute Software Diary files and
    parses them to a single file of DATE, TIME, DETAILS
    """
    
    txt = ''
    cols = []
    
    try:
        os.remove(opfile)
    except Exception:
        pass

    fl = mod_fl.FileList([fldr], ['D2013*.DAT'], ["__pycache__", ".git"], "temp.csv")
 
    with open(opfile, 'w') as fop:
        for f in fl.get_list():
            print(f)
            with open(f, 'r') as fip:
                for line in fip:
                    if line != '':
                        try:
                            cols = line.split(chr(31))
                            fop.write(cols[1] + ', ' + cols[2] + ', ' + cols[14] + '\n')
                        except Exception as ex:
                            print("Error - ", str(ex))
    


   
if __name__ == '__main__':		
    main()
