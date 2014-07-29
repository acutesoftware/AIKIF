# -*- coding: utf-8 -*-
# search.py	written by Duncan Murray 20/3/2014	(C) Acute Software
# searches AIKIF

import os
import sys
import AIKIF_utils as aikif
import fileMapping as filemap
import config as cfg
print(len(sys.argv), sys.argv)
if len(sys.argv) == 1:   # nothing passes on command line
    searchString = ['swimming']	
else:
    searchString = []
    for i in range(0, len(sys.argv)):
        print(i)
        if i > 0:
            searchString.append(sys.argv[i])
        
def search(search_string = ''):
    """ main function to search using indexes """
    if search_string == '':
        search_string = searchString
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
                        print(line)
                        numResults = numResults + 1
            print(str(line_num) + " lines searched")
    print('Found ', str(numResults), 'results in', str(totLines), 'lines over', str(len(ndxFiles)), 'index files')
    
if __name__ == '__main__':
    search()	
    

    