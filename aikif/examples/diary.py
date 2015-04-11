# diary.py

"""
Example of using AIKIF to record diary events.

1. setup data structures

2. define mappings such as what to record from command line
   apps and optionally what columns to import from external
   sources such as outlook calendars
   
3. implement simple script to do manual adds (this program)

4. optionally implement processes to auto load info from
   external sources.
   
"""
import os
import sys
import aikif.config as mod_cfg
import aikif.cls_log as mod_log
import aikif.cls_file_mapping as mod_filemap

def main():
    """
    NOTE - dont try and parse command line and attempt
    NLP splitting as it is better to use the function 
    via script (and later with web service)
    """
    diary_file = mod_filemap.FileMap('.').get_full_filename('EVENT', 'INFO-PIM-DIARY')
    print('Diary file = ', diary_file)
    today = '20150411'
    add_event(diary_file, today, 'Testing aikif.examples.diary.py')
    add_event(diary_file, today, 'Remember to fix shelf', remindme='20150422')
    
    
def add_event(fname, dte, details, remindme='', cat='', url=''):
    """
    function to take a diary / calendar or reminder note and
    add to AIKIF raw data store.
    """
    print("Adding event:", dte, details)
    with open(fname, "a") as f:
        f.write('"' + dte + '","' + details + '"\n')
    
main()