# coding: utf-8
# page_data.py	written by Duncan Murray 26/5/2014
# handles the data display page for AIKIF web interface

import sys, os
import web_utils as web

cur_folder = os.path.dirname(os.path.abspath(__file__)) 
aikif_folder = os.path.abspath(cur_folder + os.sep + ".."  )
root_folder = os.path.abspath(aikif_folder + os.sep + '..')
print('page_data.py: root_folder = ', root_folder)
sys.path.append(aikif_folder)
import AIKIF_utils as ai

import aikif.AIKIF_utils as aikif
import aikif.fileMapping as filemap

#from .AI import AIKIF_utils as aikif
#from ...AI import fileMapping as filemap

dataFolder = root_folder + os.sep + 'data' + os.sep + 'core'

def get_page(dataFile=''):
	txt = '<div id="content">\n'
	txt += '<div id="table_list">\n'
	txt += get_list_data_files()
	txt += '</div>\n'
	txt += '<div id="table_data">\n'
	if dataFile:
		fullName = os.path.join(dataFolder , dataFile)
		print("\nREADING " + fullName + '\n')
		txt += showDataFile(fullName)
	else:
		txt += get_aikif_structure()
		#txt += get_ontology()   # no - this is the proposed file list
	txt += '</div>\n'
	txt += '</div>\n'
	return txt
	
def showDataFile(fname):
	""" shows a data file in CSV format - all files live in CORE folder """
	txt = '<H2>' + fname + '</H2>'
	print (fname)
	#try:
	txt += web.read_csv_to_html_table(fname, 'Y')  # it is ok to use a table for actual table data
	#except:
	#	txt += '<H2>ERROR - cant read file</H2>'
	#txt += web.read_csv_to_html_list(fname)  # only use this for single column lists
	
	txt += '</div>\n'
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
	txt = '<H3>Master File Mapping</H3>\n' # <TABLE width=100% border=0 align=centre>\n'
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
	