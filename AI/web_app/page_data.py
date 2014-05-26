# page_data.py	written by Duncan Murray 26/5/2014
# handles the data display page for AIKIF web interface

import sys
import web_utils as web
sys.path.append('..\\..\\AI')
import AIKIF_utils as aikif
import fileMapping as filemap


def get_page():
	txt = ''
	txt += get_aikif_structure()
	txt += get_ontology()
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
	
def get_ontology():
	txt = '<H3>Master File Mapping</H3>\n<TABLE width=100% border=0 align=centre>\n'
	lst = filemap.BuildMasterFileMapping('N')
	txt += web.list2html(lst)
	return txt
	