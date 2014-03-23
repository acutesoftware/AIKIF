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
	print('---------------------')
	print('AIKIF Data Structures')
	print('---------------------')	

	AIKIF_FileList = aikif.build_AIKIF_structure()
	#aikif.printFileList(AIKIF_FileList)
	aikif.showColumnStructures(AIKIF_FileList)
	#aikif.debugPrintFileStructures(AIKIF_FileList)
	filemap.ShowListOfPhysicalFiles()

	
if __name__ == '__main__':
    view()	
	

	