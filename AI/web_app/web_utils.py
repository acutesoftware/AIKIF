# coding: utf-8
# web_utils.py	written by Duncan Murray 26/5/2014
# functions to convert data to HTML, etc for web dev
import csv
import os
import glob
import fnmatch
from flask import request

def list2html(lst):
	txt = '<TABLE width=100% border=0>'
	for l in lst:
		txt += '<TR>\n'
		if type(l) is str:
			txt+= '<TD>' + l + '</TD>\n'
		elif type(l) is list:
			txt+= '<TD>'
			for i in l:
				txt+= i + ', '
			txt+= '</TD>'
		else:
			txt+= '<TD>' + str(l) + '</TD>\n'
		txt += '</TR>\n'
	txt += '</TABLE><BR>\n'
	return txt

def GetFileList(rootPath, lstXtn, shortNameOnly='Y'):
	# written by Duncan Murray 7/8/2013 (C) Acute Software
	# builds a list of files and returns as a list 
	numFiles = 0    
	opFileList = []
	for root, dirs, files in os.walk(rootPath):
		for basename in files:
			for xtn in lstXtn:
				if fnmatch.fnmatch(basename, xtn):
					filename = os.path.join(root, basename)
					numFiles = numFiles + 1
					if shortNameOnly == 'Y':
						opFileList.append( os.path.basename(filename))
					else:
						opFileList.append(filename)
	return opFileList

	
	
def filelist2html(lst, fldr):
	txt = '<TABLE width=100% border=0>'
	for l in lst:
		txt += '<TR>'
		if type(l) is str:
			txt+= '<TD>' + link_file(l, fldr) + '</TD>\n'
		elif type(l) is list:
			txt+= '<TD>'
			for i in l:
				txt+= link_file(i, fldr) + ', '
			txt+= '</TD>'
		else:
			txt+= '<TD>' + str(l) + '</TD>\n'
		txt += '</TR>\n'
	txt += '</TABLE><BR>\n'
	return txt

def link_file(f, fldr):
	""" creates a html link for a file using folder fldr """
	fname = os.path.join(fldr,f)
	#print('\nf = ', f, fname)
	if os.path.isfile(fname):
		#if f.startswith('data/'):
		if 'data/' in request.path:
			return '<a href="' + f + '">' + f + '</a>'
		else:
			return '<a href="data/' + f + '">' + f + '</a>'
			#return '<a href="' + f + '">' + f + '</a>'
	else:
		return f
	#return '<a href="?' + f + '">' + f + '</a>'
	
def dict_to_htmlrow(d):
	res = "<TR>\n"
	for k, v in d.iteritems():
		if type(v) == str:
			res = res + '<TD>' + k + ':</TD><TD>' + v + '</TD>\n'
		else:
			res = res + '<TD>' + k + ':</TD><TD>' + str(v) + '</TD>\n'
	#print res
	res += '</TR>\n'
	return res

def read_csv_to_html_table(csvFile):
	txt = '<TABLE width=100% border=1>'
	with open(csvFile) as csv_file:
		for row in csv.reader(csv_file, delimiter=','):
			txt += "<TR>"
			for col in row:
				txt += "<TD>"
				try:
					txt += col
				except:
					txt += 'Error'
				txt += "</TD>"
			txt += "</TR>"
		txt += "</TABLE>"
	return txt
	