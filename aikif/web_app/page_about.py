# page_about.py	written by Duncan Murray 31/5/2014
# handles the about page for AIKIF web interface

import sys, os
import web_utils as web

sys.path.append('..\\..\\AI')
import AIKIF_utils as aikif
import fileMapping as filemap

#from .AI import AIKIF_utils as aikif
#from ...AI import fileMapping as filemap

dataFolder = '..\\data\\core\\'  
dataFolder = 'T:\\user\\dev\\src\\python\\AI\\data\\core'

def get_page(dataFile=''):
	txt = ''
	txt += "This is an example framework to capture the flow of information initially "
	txt += "for personal data management, but ultimately useful for AI applications.<BR>"
	txt += "Initially it will be populated and tested for human use, but includes tests "
	txt += "and verification process for future 'General AI's.<BR>"

	txt += get_aikif_structure()
	return txt
	
		
	
def get_aikif_structure():
	txt = '<H3>AIKIF Data Structure</H3>\n<TABLE width=100% border=0 align=centre>\n'
	AIKIF_FileList = aikif.build_AIKIF_structure()
	nme = ''
	flds = ''
	for j in range(len(AIKIF_FileList)):
		txt += '<TR>\n'
		for key in AIKIF_FileList[j]: 
			if key == 'fname':
				nme = AIKIF_FileList[j][key]
			if key == 'fields':
				flds = ''
				for fld in AIKIF_FileList[j][key]:
					flds +=  fld + ', '
		txt += '<TR><TD>' + nme + '</TD><TD>' + flds + '</TD></TR>\n'
	txt += '</TABLE><BR><BR>'
	return txt
	

	