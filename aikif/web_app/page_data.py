# coding: utf-8
# page_data.py	written by Duncan Murray 26/5/2014
# handles the data display page for AIKIF web interface

import os
import aikif.web_app.web_utils as web

cur_folder = os.path.dirname(os.path.abspath(__file__)) 
aikif_folder = os.path.abspath(cur_folder + os.sep + ".."  )
root_folder = os.path.abspath(aikif_folder + os.sep + '..')
data_folder = root_folder + os.sep + 'data' + os.sep + 'core'
print('page_data.py: root_folder = ', root_folder)

def get_page(dataFile=''):
	txt = '<div id="content">\n'
	txt += '<div id="table_list">\n'
	txt += get_list_data_files(data_folder)
	txt += '</div>\n'
	txt += '<div id="table_data">\n'
	if dataFile:
		fullName = os.path.join(data_folder , dataFile)
		print("\nREADING " + fullName + '\n')
		txt += show_data_file(fullName)
	else:
		txt += get_aikif_structure()
	txt += '</div>\n'
	txt += '</div>\n'
	return txt
	
def show_data_file(fname):
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
	txt += '<TR><TD>TODO</TD><TD>test</TD></TR>\n'
	txt += '</TABLE><BR><BR>'
	return txt
	
def get_list_data_files(fldr):
	txt = '<H3>Master File Mapping</H3>\n' # <TABLE width=100% border=0 align=centre>\n'
	print( "get_list_data_files(): fldr = " + fldr )
	lst = web.GetFileList(fldr, '*.csv')
    #print(lst)
	txt += web.filelist2html(lst, fldr)
	return txt
	
