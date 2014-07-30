# -*- coding: utf-8 -*-
# search.py	written by Duncan Murray 20/3/2014	(C) Acute Software
# searches AIKIF

import os
import sys
import AIKIF_utils as aikif
import fileMapping as filemap
import config as cfg

import argparse

print("NOTE - you need to call python to get args passed, e.g.\n")
print("python search.py database\n")


  
def search(search_string):
    """ main function to search using indexes """
    aikif.LogProcess('Starting search',  'search.py') # sys.modules[self.__module__].__file__)
    print('-------------------')
    print('Searching for ', search_string)
    print('-------------------')	

#	ndxFiles = ['..\\data\\index\\ndxAll.txt', '..\\data\\index\\ndxWordsToFilesLecture.txt']
    ndxFiles = cfg.params['index_files']
    numResults = 0
    totLines = 0
    for fname in ndxFiles:
        print("Searching " + fname)
        with open(fname, 'r') as f:
            for line_num, line in enumerate(f):
                totLines = totLines + 1
                for src in search_string:
                    if src in line:
                        try:
                            print(line)   # gives error with some encoding
                        except:
                            print("Cant print search result")
                        numResults = numResults + 1
            print(str(line_num) + " lines searched")
    print('Found ', str(numResults), 'results in', str(totLines), 'lines over', str(len(ndxFiles)), 'index files')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search.py looks in AIKIF index files for strings')
    parser.add_argument('-s', '--search', help='enter a search string, enclosed with quotes if multiple words needed')
    parser.add_argument('-i', '--index', help='choose an index file to search')
    args = parser.parse_args()
    # ... do something with args.search ...
    # ... do something with args.verbose ..
    print(args.search)
    search([args.search])	
    

    