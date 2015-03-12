# coding: utf-8
# web_utils.py	written by Duncan Murray 26/5/2014
# functions to convert data to HTML, etc for web dev
import csv
import os
import glob
import fnmatch
from flask import request
import sys


def list2html(lst):
    """ 
    convert a list to html using table formatting 
    """
    txt = '<TABLE width=100% border=0>'
    for l in lst:
        txt += '<TR>\n'
        if type(l) is str:
            txt+= '<TD>' + l + '</TD>\n'
        elif type(l) is list:
            txt+= '<TD>'
            for i in l:
                txt += i + ', '
            txt+= '</TD>'
        else:
            txt+= '<TD>' + str(l) + '</TD>\n'
        txt += '</TR>\n'
    txt += '</TABLE><BR>\n'
    return txt

def GetFileList(rootPath, lstXtn, shortNameOnly='Y'):
    """ 
    builds a list of files and returns as a list 
    """
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
                        
    return sorted(opFileList)

  
def filelist2html_div(lst, fldr):
    """ 
    convert a list to html using DIV formatting 
    """
    txt = ''
    for l in lst:
        if type(l) is str:
            txt+= ' ' + link_file(l, fldr) + '\n'
        elif type(l) is list:
            for i in l:
                txt+= link_file(i, fldr) + ', '
            txt+= '\n'
        else:
            txt+= ' ' + str(l) + '\n'
        txt += '<BR>\n'
    txt += '\n'
    return txt

def build_search_form():
    """ 
    returns the html for a simple search form 
    """
    txt = '<form action="." method="POST">\n'
    txt += '  <input type="text" name="search_text">\n'
    txt += '  <input type="submit" name="my-form" value="Search">\n'
    txt += '</form>\n'
    return txt
    
def filelist2html(lst, fldr, hasHeader='N'):
    """ 
    formats a standard filelist to htmk using table formats 
    """
    txt = '<TABLE width=100% border=0>'
    numRows = 1
    if lst:
        for l in lst:
            if hasHeader == 'Y':
                if numRows == 1:
                    td_begin = '<TH>'
                    td_end = '</TH>'
                else:
                    td_begin = '<TD>'
                    td_end = '</TD>'
            else:
                td_begin = '<TD>'
                td_end = '</TD>'
            numRows += 1
            txt += '<TR>'
            if type(l) is str:
                txt += td_begin + link_file(l, fldr) + td_end
            elif type(l) is list:
                txt += td_begin
                for i in l:
                    txt+= link_file(i, fldr) + '; '
                txt += td_end
            else:
                txt += td_begin + str(l) + td_end
            txt += '</TR>\n'
    txt += '</TABLE><BR>\n'
    return txt

def link_file(f, fldr):
    """ 
    creates a html link for a file using folder fldr 
    """
    fname = os.path.join(fldr,f)
    if os.path.isfile(fname):
        if 'data/' in request.path:
            return '<a href="' + f + '">' + f + '</a>'
        else:
            return '<a href="data/' + f + '">' + f + '</a>'
    else:
        return f
    
def dict_to_htmlrow(d):
    """
    converts a dictionary to a HTML table row
    """
    res = "<TR>\n"
    for k, v in d.items():
        if type(v) == str:
            res = res + '<TD><p>' + k + ':</p></TD><TD><p>' + v + '</p></TD>'
        else:
            res = res + '<TD><p>' + k + ':</p></TD><TD><p>' + str(v) + '</p></TD>'
    res += '</TR>\n'
    return res

def read_csv_to_html_table(csvFile, hasHeader='N'):
    """
    reads a CSV file and converts it to HTML
    """
    txt = '<table class="as-table as-table-zebra as-table-horizontal">'
    with open(csvFile, "r") as file:  # 
        numRows = 1
        for row in file:
            if hasHeader == 'Y':
                if numRows == 1:
                    td_begin = '<TH>'
                    td_end = '</TH>'
                else:
                    td_begin = '<TD>'
                    td_end = '</TD>'
            else:
                td_begin = '<TD>'
                td_end = '</TD>'
            cols = row.split(',')
            numRows += 1

            txt += "<TR>"
            for col in cols:
                txt += td_begin
                try:
                    colString = col
                except:
                    colString = '<font color=red>Error decoding column data</font>'
                txt += colString.strip('"')	
                txt += td_end
            txt += "</TR>\n"
        txt += "</TABLE>\n\n"
    return txt
    

def read_csv_to_html_table_using_CSV_module_OLD(csvFile, hasHeader='N'):
    txt = '<TABLE width=100% border=1>'
    with open(csvFile, "rb") as csv_file:  # , encoding='utf-8'
        numRows = 1
        for row in csv.reader(csv_file, delimiter=','):
            if hasHeader == 'Y':
                if numRows == 1:
                    td_begin = '<TH>'
                    td_end = '</TH>'
                else:
                    td_begin = '<TD>'
                    td_end = '</TD>'
            else:
                td_begin = '<TD>'
                td_end = '</TD>'
            numRows += 1

            txt += "<TR>"
            for col in row:
                txt += td_begin
                try:
                    txt += col
                except:
                    txt += 'Error'
                txt += td_end
            txt += "</TR>\n"
        txt += "</TABLE>\n\n"
    return txt
    
def read_csv_to_html_list(csvFile):
    txt = ''
    with open(csvFile) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            txt += '<div id="table_row">'
            for col in row:
                txt += " "
                try:
                    txt += col
                except:
                    txt += 'Error'
                txt += " "
            txt += "</div>\n"
    return txt
    