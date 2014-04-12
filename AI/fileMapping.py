# fileMapping.py   written by Duncan Murray 18/3/2014  (C) Acute Software
# information on the actual files used in AIKIF - this file contains both
# functions to access the files (data and source) for the application as 
# well as the manually listed and described set of files for each area.

# NOTE:
#		 the complete list of 'root' files lives in AIKIF_utils.py
#		 and this program shows how they are split into separate files
#		 to manage space (eg there will be thousands of email events but
#		 only a few PIM events and searching fast is important. So this
#		 verifies completeness and has functions to check the progress.

# USAGE: 
#	fileMapping.py	= displays all file lists
#	CheckFile(fname)	= checks to see if a file exists on disc and is defined
#	GetDataFolder()		= returns the folder of the data files
#	DoesFileExist(fname)= checks for physical presence of the file in the approp folder
#	IsFileMapped(fname)	= checks to see if file is mapped in master file structure
#	AppendData(dat, fname)	= this is the SAFE way to append data


import os
import sys
import csv
import time
from datetime import datetime
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
import AIKIF_utils as aikif

dataPath = r"T:\user\dev\src\python\AI\data"
# Use os.path.join(). Example: os.path.join(pathfile,"output","log.txt").
# In your code that would be: rootTree.write(os.path.join(pathfile,"output","log.txt")) 

dataFiles = []  # complete mapping of file types to physical CSV files
dataFileTypes = [
	'EVENT',    # when
	'LINK',     # how	'relationship', <- relationship is a TYPE of link
	'OBJECT',   # reference file lookup to get heirachy
	'THING',    # what
	'LOCATION', # where
	'PROCESS',  # another what?
	'ACTOR'     # who
	]
	
dataSubjectAreas = [
	'_TOP', 		# this is the top level ontology for all subject areas
	'INFO-COURSE', 
	'INFO-DATASET', 
	'INFO-PIM', 
	'INFO-PIM-SHOPPING', 
	'INFO-PIM-DIARY',
	'INFO-PIM-PROJECT',
	'INFO-PIM-TASK',
	'INFO-PIM-CONTACT',
	'INFO-PIM-NOTE',
	'INFO-PIM-PCUSAGE',
	'INFO-MESSAGE',
	'INFO-MESSAGE-EMAIL',
	'INFO-MESSAGE-SMS',
	'INFO-MESSAGE-PHONE',
	'INFO-MESSAGE-FORUM',
	'INFO-MESSAGE-LETTER',
	'INFO-SOCIAL-TWITTER',
	'INFO-SOCIAL-FACEBOOK',
	'INFO-SOCIAL-GOOGLE+',
	'INFO-SOCIAL-OTHER',
	'OBJECT-ASSET', 
	'OBJECT-ASSET-COMPUTER', 
	'OBJECT-ASSET-FURNITURE', 
	'OBJECT-ASSET-CAR', 
	'OBJECT-ASSET-RESOURCE', 
	'SYSTEM-PC-LOG', 
	'SYSTEM-PC-FILE', 
	'SYSTEM-PC-FILE-LECTURES', 
	]


def main():
	print('-----------------------------------------------------------')
	print('File Mapping information for AIKIF - last updated 18/3/2014')
	print('-----------------------------------------------------------')

	BuildMasterFileMapping('Y') # TOK

	ShowListOfProposedFiles('N') # TOK
	ShowListOfMappedFiles('N')   # TOK
	ShowListOfPhysicalFiles('N')	# TOK


def GetDataPath():
	return dataPath 
	
def ShowListOfProposedFiles(printList='Y'):
	# display a list of files which are defined in AIKIF_utils.py
	numFiles = 0
	
	fl_all = [['filename', 'exists', 'description']]
	fl_all.append(['EV_PIM', 'N', 'Diary events'])
	fl_all.append(['EV_EMAIL', 'N', 'Emails sent and recieved'])
	fl_all.append(['EV_SMS', 'N', 'Phone texts'])
	fl_all.append(['EV_SYS_REBOOTS', 'N', 'File system reboots all PCs'])
	fl_all.append(['ONT__TOP', 'N', 'Ontology Master file for top level hierachy'])
	fl_all.append(['ONT_WHO', 'N', 'Ontology heircahy for contacts'])
	fl_all.append(['ONT_WHAT', 'N', 'Ontology heircahy for Objects'])
	fl_all.append(['ONT_WHEN', 'N', 'Ontology heircahy for Time'])
	fl_all.append(['ONT_WHERE', 'N', 'Ontology heircahy for Locations'])
	fl_all.append(['ONT_WHY', 'N', 'Ontology heircahy for Reasoning'])
	if printList == 'Y':
		print('\nALL FILES (eventually):')
		for i in fl_all:
			print(i)
	if printList == 'HTML':
		dat.SaveListToFile(fl_all, 'file_list_required.csv')
		net.FormatCsvAsHtml('file_list_required.csv', 'file_list_required.html')
		fle.LaunchFile('file_list_required.html')
	numFiles = len(fl_all)
	print('Proposed Files =  ' + str(numFiles))
	return len(fl_all)
	

def ShowListOfMappedFiles(printList='Y'):
	# display a list of files which are defined in AIKIF_utils.py
	numFiles = 0
	AIKIF_FileList = aikif.build_AIKIF_structure()
	fl_defined = aikif.getFileList(AIKIF_FileList)
	if printList == 'Y':
		print('\nFILES MAPPED VIA AIKIF_utils.py:')
		aikif.showColumnStructures(AIKIF_FileList)
		#aikif.printFileList(AIKIF_FileList)
	if printList == 'HTML':
		dat.SaveListToFile(fl_defined, 'file_list_mapped.csv')
		net.FormatCsvAsHtml('file_list_mapped.csv', 'file_list_mapped.html')
		fle.LaunchFile('file_list_mapped.html')

	numFiles = len(fl_defined)	
	print('Mapped Files =  ' + str(numFiles))
	return numFiles
	

def ShowListOfPhysicalFiles(printList='Y'):
	# display a list of files which currently exist
	numFiles = 0
	
	fl_actual = fle.GetFileList([dataPath], ['*.csv'], ["__pycache__", ".git"])
	#fl_actual = fle.GetFileList([os.getcwd()], ['*.py'], ["__pycache__", ".git"])
	if printList == 'Y':
		print('\nACUAL LIST OF FILES IN AI\DATA FOLDER:')
		for i in fl_actual:
			print(i)
	if printList == 'HTML':
		fle.SaveFileList(fl_actual, 'file_list_actual.csv', ["name", "path", "size", "date"])
		net.FormatCsvAsHtml('file_list_actual.csv', 'file_list_actual.html')
		fle.LaunchFile('file_list_actual.html')
	numFiles = len(fl_actual)	
	print('Actual Files =  ' + str(numFiles))
	return numFiles
	
	
	
def BuildMasterFileMapping(printList='Y'):
	# function to create the complete list of files, though not all are required
	numFiles = 0
	dataFileList = []
	for a in dataFileTypes:
		for b in dataSubjectAreas:
			dataFileList.append([GetFilename(a,b)])
			numFiles = numFiles + 1
	numFiles = len(dataFileList)	
	print('Master Possible List of Files =  ' + str(numFiles))
			
	if printList == 'Y':
		for i in dataFileList:
			print(i)
	return dataFileList
	

def FindOntology(txt):
	# top level function used for new data processing which attempts
	# to find a level in a heirarchy and return the key and filename
	# usage res = FindOntology('file')  # returns 'SYSTEM-PC-FILE'
	totFound = 0
	searchString = txt.upper()
	#print(searchString)
	match = []
	if searchString != '':
		for i in dataSubjectAreas:
			#print(i)
			if searchString in i:
				totFound = totFound + 1
				match.append(i)
				#print(i)
	if len(match) == 0:
		match.append('_TOP')
	return match

def FindType(txt):
	# top level function used to simply return the ONE ACTUAL string used for data types
	searchString = txt.upper()
	#print(searchString)
	match = 'Unknown'
	for i in dataFileTypes:
		#print(i)
		if searchString in i:
			match = i
			#print(i)
	return match

	
def GetFullFilename(dataType, subjectArea):
	#print('a = ', dataType)
	#print('b = ', subjectArea)
	# use os.sep()
	return dataPath + '\\' + dataType + '_' + subjectArea + '.CSV'
	
	
def GetFilename(dataType, subjectArea):
	#print('a = ', dataType)
	#print('b = ', subjectArea)
	return dataType + '_' + subjectArea + '.CSV'
		
	
def AddFileToMappingList(fname, lst):
	# adds the name of the file to the list
	lst.append(fname)
	
	
	
if __name__ == '__main__':
    main()	