# coding: utf-8
# page_programs.py	written by Duncan Murray 28/5/2014
# handles the programs display page for AIKIF web interface

import sys, os
import web_utils as web
sys.path.append('..\\..\\AI')


def get_page():
	txt = '<a href="/programs/rebuild">Rebuild Program List</a><BR>'
	txt += show_program_list()
	return txt

def show_program_list():
	with open('program_list.html', 'r') as f:
		return f.read()

def rebuild():
	""" rebuilds the list of programs to file  """
	with open('program_list.html', 'w') as f:
		f.write(get_program_list())
	
def get_program_list():
	#colList = ['FullName', 'Path', 'FileName','FileSize','Functions', 'Imports']
	colList = ['FileName','FileSize','Functions', 'Imports']

	txt = '<TABLE width=90% border=0>'
	txt += format_file_table_header(colList)
	fl = web.GetFileList('..\\..\\AI', ['*.py'], 'N')
	for f in fl:
		txt += format_file_to_html_row(f, colList)
	txt += '</TABLE>\n\n'
	return txt

	
def format_file_table_header(lstCols):
	txt = '<TR>'
	if 'FullName' in lstCols: 
		txt += '<TD>Full Path and Filename</TD>' 
	if 'FileName' in lstCols: 
		txt += '<TD>File Name</TD>' 
	if 'Path' in lstCols: 
		txt += '<TD>Path</TD>' 
	if 'FileSize' in lstCols: 
		txt += '<TD>Size</TD>' 
	if 'Imports' in lstCols:	
		txt += '<TD>Imports</TD>' 
	if 'Functions' in lstCols: 
		txt += '<TD>List of Functions</TD>' 
	txt += '</TR>\n'
	return txt

	
def format_file_to_html_row(fname, lstCols):
	txt = '<TR>'
	if 'FullName' in lstCols: 
		txt += '<TD>' + fname + '</TD>' 
	if 'FileName' in lstCols: 
		txt += '<TD>' + os.path.basename(fname) + '</TD>' 
	if 'Path' in lstCols: 
		txt += '<TD>' + os.path.abspath(fname) + '</TD>' 
	if 'FileSize' in lstCols: 	
		txt += '<TD>' + format(os.path.getsize(fname), ",d") + '</TD>' 
	if 'Imports' in lstCols:
		txt += '<TD>' + get_imports(fname) + '</TD>' 
	if 'Functions' in lstCols:
		txt += '<TD>' + get_functions(fname) + '</TD>' 
	txt += '</TR>\n'
	return txt

def get_functions(fname):
	""" get a list of functions from a Python program """
	txt = '' # os.path.abspath(fname)
	numLines = 0
	with open(fname, 'r') as f:
		for line in f:
			numLines += 1
			#if numLines < 15:
			#	txt += line + '<BR>\n' 
			
			if line.strip()[0:4] == 'def ':
				txt += '<PRE>' + strip_text_after_string(strip_text_after_string(line, '#')[4:], ':') + '</PRE>\n'
			if line[0:5] == 'class':
				txt += '<PRE>' + strip_text_after_string(strip_text_after_string(line, '#'), ':') + '</PRE>\n'
	return txt + '<BR>'

def strip_text_after_string(txt, junk):
	""" used to strip any poorly documented comments at the end of function defs """
	if junk in txt:
		return txt[:txt.find(junk)]
	else:
		return txt
	
def get_imports(fname):
	""" get a list of imports from a Python program """
	txt = ''
	with open(fname, 'r') as f:
		for line in f:
			if line[0:6] == 'import':
				txt += '<PRE>' + strip_text_after_string(line[7:], ' as ') + '</PRE>\n'
	return txt + '<BR>'


	
	
	