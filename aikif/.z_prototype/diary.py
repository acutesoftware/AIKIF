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
import sys
sys.path.append('..')

import cls_file_mapping as mod_filemap
import core_data as c

def main():
    """
    NOTE - don't try and parse command line and attempt
    NLP splitting as it is better to use the function 
    via script (and later with web service)
    """
    dataSubjectAreas = ['log events', 'reminders', 'todo']
    diary_file = mod_filemap.FileMap([],[]).get_full_filename('EVENT', 'INFO-PIM-DIARY')
    print('Diary file = ', diary_file)
    today = '20170418'
    add_event(diary_file, today, 'Testing aikif.examples.diary.py')
    add_event(diary_file, today, 'random diary entry')
    add_event(diary_file, '2016-06-04', 'deposit bank cheque for custom software', cat='tax')
    add_event(diary_file, '2013-11-12', 'Book car in for major service', remindme='20131111')
    #  add_event(diary_file, today, 'Remember to fix shelf', remindme='20150422')

def add_event(fname, dte, details, remindme='', cat='Diary'):
    """
    function to take a diary / calendar or reminder note and
    add to AIKIF raw data store.
    """
    print("Adding event:", dte, remindme, details)
    
    e = c.CoreDataWhen('Diary', [dte, cat, details])
    
    
    with open(fname, "a") as f:
        f.write(e.format_csv())


def parse_csv_file_to_events(fname, date_col_num, details_col_num):
    """
    read a CSV file and parse to diary events
    """
    with open(fname, 'r') as f:
        for line in f:
            print(line)
            # add_event ...
    


        
main()