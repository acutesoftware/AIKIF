# coding: utf-8
# security.py	written by Duncan Murray 23/3/2014	(C) Acute Software
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

securityLevels = [
	'NONE', 	# anyone
	'NETWORK',  # all users on any device in the network
	'WORK',		# your work group (customise this - have as many as desired)
	'FAMILY',	# your family
	'PARTNER',	# your partner
	'SELF'		# yourself
	]
	

securityMappings = []
	
def MapSecurityLevel(files, security):   
	# call this function when adding sensitive data
	for file in files:
		securityMappings.append([file, security])

	
def ShowSecurity():
	num = 0
	print('map\tfile\t\t\t\tlevel')
	for map in securityMappings:
		num = num+ 1
		print(str(num) + '\t' + fle.GetShortFileName(map[0]) + '\t' + map[1])

		
def main():
	# main function 

	aikif.LogProcess('Starting Security',  'view.py') # sys.modules[self.__module__].__file__)
	print('--------------')
	print('AIKIF Security')
	print('--------------')	
	
	privateFiles = []
	privateFiles.append(filemap.GetFullFilename(filemap.FindType('thing'), filemap.FindOntology('shopping')[0]))
	privateFiles.append(filemap.GetFullFilename(filemap.FindType('event'), filemap.FindOntology('shopping')[0]))
	
	workFiles = []
	workFiles.append(filemap.GetFullFilename(filemap.FindType('location'), filemap.FindOntology('file')[0]))
	
	#print(privateFiles)
	MapSecurityLevel(workFiles, 'WORK')
	MapSecurityLevel(privateFiles, 'FAMILY')
	ShowSecurity()

	
if __name__ == '__main__':
    main()	
	
		
		