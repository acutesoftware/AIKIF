# coding: utf-8
# view.py	written by Duncan Murray 22/3/2014	(C) Acute Software
# searches AIKIF

import os
import sys
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
import AIKIF_utils as aikif
import fileMapping as filemap


if len(sys.argv) == 2:
	viewStructure = sys.argv[1]

def view():
	# main function 
	aikif.LogProcess('Starting view',  'view.py') # sys.modules[self.__module__].__file__)
	AIKIF_FileList = aikif.build_AIKIF_structure()
		
	command = ''
	ShowMenu()
	while True:
		command = input('Enter command: (m=menu, q=quit, [string]=view entries for string ')
		if command.upper() == 'Q': 
			quit()
		if command.upper() == 'M': 
			ShowMenu()
		if command.upper() == 'S':
			ShowStatistics()
		if command == '1':
			aikif.printFileList(AIKIF_FileList)
		if command == '2':
			aikif.showColumnStructures(AIKIF_FileList)
		if command == '3':
			aikif.debugPrintFileStructures(AIKIF_FileList)
		if command == '4':
			filemap.ShowListOfPhysicalFiles()

def ShowMenu():
	print('---------------------')
	print('AIKIF Data Structures')
	print('---------------------')	
	print('1 - aikif.printFileList(AIKIF_FileList)')
	print('2 - aikif.showColumnStructures(AIKIF_FileList)')
	print('3 - aikif.debugPrintFileStructures(AIKIF_FileList)')
	print('4 - filemap.ShowListOfPhysicalFiles()')
	print('m - show this menu')
	print('s - statistics')
	print('q - quit')
	
	
def ShowStatistics():
	print(' ----=== Statistics for AIKIF ===----')
	
	
if __name__ == '__main__':
    view()	
	

	