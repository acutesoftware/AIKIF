# coding: utf-8
# page_data.py	written by Duncan Murray 26/5/2014
# handles the data display page for AIKIF web interface

import sys, os
import web_utils as web

sys.path.append('..\\..\\AI')
import AIKIF_utils as aikif
import fileMapping as filemap

#from .AI import AIKIF_utils as aikif
#from ...AI import fileMapping as filemap

dataFolder = '..\\data\\core\\'  
dataFolder = 'T:\user\dev\src\python\AI\data\core'

def get_page(dataFile=''):
	txt = '<TABLE width=98% align=centre valign=top border=0><TR><TD width=40%>'
	txt += get_list_data_files()
	txt += '</TD><TD>'
	if dataFile:
		fullName = os.path.join(dataFolder , dataFile)
		print("\nREADING " + fullName + '\n')
		txt += showDataFile(fullName)
	else:
		txt += get_aikif_structure()
		#txt += get_ontology()   # no - this is the proposed file list
		
	txt += '</TD></TR></TABLE>\n'
	return txt
	
def showDataFile(fname):
	""" shows a data file in CSV format - all files live in CORE folder """
	txt = '<H2>' + fname + '</H2>'
	txt += web.read_csv_to_html_table(fname)
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
	
def get_list_data_files():
	txt = '<H3>Master File Mapping</H3>\n<TABLE width=100% border=0 align=centre>\n'
	pth = os.path.abspath('..\\data\\core\\')
	print( "get_list_data_files(): PTH = " + pth )
	lst = web.GetFileList(pth, '*.CSV')
	txt += web.filelist2html(lst, pth)
	return txt
	
def get_ontology():
	txt = '<H3>Master File Mapping</H3>\n<TABLE width=100% border=0 align=centre>\n'
	lst = filemap.BuildMasterFileMapping('N')
	txt += web.filelist2html(lst, '..\\..\\data\\')
	return txt
	