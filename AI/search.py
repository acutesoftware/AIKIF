# coding: utf-8
# search.py	written by Duncan Murray 20/3/2014	(C) Acute Software
# searches AIKIF

import os
import sys
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
import AIKIF_utils as aikif
import fileMapping as filemap

silent = 'N'
if len(sys.argv) == 2:
	if sys.argv[1] == 'Q':
		silent = 'Y'

searchString = 'confounders'		
		
def search():
	# main function 

	aikif.LogProcess('Starting search',  'search.py') # sys.modules[self.__module__].__file__)
	if silent == 'N':
		print('-------------------')
		print('Searching for ' + searchString)
		print('-------------------')	

	ndxFiles = ['..\\data\\index\\ndxAll.txt', '..\\data\\index\\ndxFullLecture.txt']
	ndxFiles = ['..\\data\\index\\ndxAll.txt', '..\\data\\index\\ndxWordsToFilesLecture.txt']
	numResults = 0
	totLines = 0
	for fname in ndxFiles:
		with open(fname, 'r') as f:
			for line in f:
				totLines = totLines + 1
				if searchString in line:
					print(line)
					numResults = numResults + 1

	print('Found ', str(numResults), 'results in', str(totLines), 'lines over', str(len(ndxFiles)), 'index files')
	
if __name__ == '__main__':
    search()	
	

	