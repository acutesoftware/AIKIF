# -*- coding: utf-8 -*-
# dataTools.py		written by Duncan Murray  9/4/2014
# Module to manage and process datasets - basically a wrapper
# around existing lists, with added documentation and logging
# for AIKIF and commonly used functions for simple data processing
#
#
# Functions
#	Transform columns to new tables
#	Generate SQL for imports
# 	Import and convert CSV to XLS
#	uses (?replaces?) most of aspytk data.py
 
# Usage:
	# from AIKIF import dataTools as ds
	# ds = dat.DataSet(‘C_COUNTRY.XLS’)   		  #existing table (your source file)
	# dsOutput = dat.DataSet(‘FACT_FILE.XLS’)   #output table after processing
	# cols = ds.IntentifyColumns()   # returns a dict with detailed estimates of col types
	# mapping = ds.MapTo(dsOutput)
	# mapping.col(‘country code’, ‘FACT_COUNTRY_ID’)
	# mapping.col(‘country name’, ‘FACT_COUNTRY_DESC’)
	# countryRules = bus.DatasetRules(ds)	# define rules for this dataset
	# countryRules.Add(‘China (excl Mongolia)’, ‘China’)
	# countryRules.Add(‘AUSTRALIA’, ‘Australia’)

	# mapping.Process()	# does the work moving data from file 1 to file 2 with column mappings
	# countryRules.Apply(dsOutput)  # apply rules on which file you want 
	# dsOutput.Export()

import os
import sys
import csv
import string
sys.path.append('..//..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
try:
	import lib_excel as xl
except:
	print('you need to install xlrd')

fldr = '..//..//data//temp//'

def TEST():
	print('Data tools test...')
	url = 'http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&standard australian classification of countries, 2011, version 2.2.xls&1269.0&Data Cubes&EE21444EE8F2C99CCA257BF30012B66F&0&2011&01.10.2013&Latest'
	fname = fldr + 'test.xlsx'
	DownloadFile(url, fname)
	#xl.csv_from_excel(fname , os.getcwd())
	testFile = fldr + 'test.csv'
	CreateRandomCSVFile(testFile)
	GenerateSQL(testFile, headerRow=1)

	CreateRandomIndentedCSVFile(fldr + 'indented.csv')
#	ExtractTable(f, tmpFile, extractList[1]['colList'], 8, 1, 52, 9)
	AutoFillCSV(fldr + 'indented.csv', fldr + 'indented-fixed.csv', ['grouping', 'code', 'desc'],  ['grouping'])   # autofill FIRST col based on prev values
	RemoveBlankRecs(fldr + 'indented-fixed.csv', fldr + 'indented-fixed-and-no-blanks.csv', 2)

	

def DownloadFile(url, fname):
	# bug here - you need to wait for download to finish
	net.DownloadFile(url, fname)
	
	
def CreateRandomCSVFile(fname):
	fle.deleteFile(fname)
	content = [['id', 'code', 'desc'], ['1', 'S', 'AAA'], ['2', 'B', 'BBB'], ['3', 'X', 'Long description']]
	for row in content:
		dat.addSampleData(fname, row)
			
	
def CreateRandomIndentedCSVFile(fname):
	fle.deleteFile(fname)
	content = [['grouping', 'code', 'desc'], ['1', 'S', 'AAA'], [' ', 'T', 'BBB'], ['3', 'X', 'Long description'], ['', 'Y', 'Long description']]
	for row in content:
		dat.addSampleData(fname, row)
			
def IntentifyColumns(fname):
	# returns a dict with detailed estimates of col types
	print('IntentifyColumns(' + fname + '):')
	
def DataSet(fname):
	# defines a dataset
	print('dataset defined = ' + fname)

def MapTo(opFile):
	pass


def AnalyseCSV(fname):
	print('dataTools.py - AnalyseCSV("' + fname + '")')

def ExtractTable(fname, opFile, opCols, startRow=1, startCol=1, endRow=5, endCol=5):			
	print('Extracting ' + os.path.basename(fname) + ' to ' + opFile)
	curRow = 1
	curCol = 1
	cols = collections.Counter()
	
	csv_file = open(opFile, 'wb')
	#wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
	
	with open(fname) as input_file:
	
		for hdr in opCols:
			csv_file.write('"' + hdr + '",')
		csv_file.write('\n')
		for row in csv.reader(input_file, delimiter=','):
			if curRow >= startRow:
				if curRow <= endRow:
					curCol = 0
					for col in row:
						curCol = curCol + 1
						if curCol >= startCol:
							if curCol <= endCol:
								colText = "".join(map(str,col)).strip('"').strip()    #prints JUST the column name in the list item
								csv_file.write('"' + colText + '",')
					#wr.writerow(row)
					csv_file.write('\n')
			curRow = curRow + 1
	csv_file.close()
	

def AutoFillCSV(fname, opFile, colList, autoFillCols):
	# Converts sub total style data to a flat list, e.g. changes:
		# 3	HEADING	
			# 31	data 1
			# 32	data 2

	print('\nAutoFilling ' + os.path.basename(fname) + ' to ' + opFile)
	curCol = 1
	lastValues = []
	for c in colList:
		lastValues.append(c)
	print(lastValues)	
	csv_file = open(opFile, 'w')
	with open(fname) as input_file:
		for row in csv.reader(input_file, delimiter=','):
			for curCol, col in enumerate(row):
				colText = "".join(map(str,col)).strip('"').strip()    #prints JUST the column name in the list item
				if curCol in autoFillCols:
					if colText == "":
						colText = lastValues[curCol]
					else:
						lastValues[curCol] = colText
				csv_file.write('"' + colText + '",')
			csv_file.write('\n')
	csv_file.close()
	
	
def RemoveBlankRecs(fname, opFile, masterCol):
	# removes lines where col number 'masterCol' is blank
	print('cleaning ' + os.path.basename(fname) )
	curCol = 1
	rowText = ''
	csv_file = open(opFile, 'w')
	with open(fname) as input_file:
		for row in csv.reader(input_file, delimiter=','):
			keepRow = True
			rowText = ''
			for curCol, col in enumerate(row):
				colText = "".join(map(str,col)).strip('"').strip()    #prints JUST the column name in the list item
				if curCol == masterCol:
					if colText == "":
						keepRow = False
				rowText = rowText + '"' + colText + '",'
			rowText = rowText + '\n'
			if keepRow:
				csv_file.write(rowText)
	csv_file.close()


	
		
def GenerateSQL(csvFile, headerRow=1):
	# top level function
	tbl = os.path.basename(csvFile).split('.')[0]
	opFile = fldr + os.path.basename(csvFile).split('.')[0] + '.SQL'
	# read in the CSV file header
	cols = []
	txt = ''
	SQL_file = open(opFile, 'w')
	with open(csvFile) as input_file:
		rowNum = 0
		for row in csv.reader(input_file, delimiter=','):
			rowNum = rowNum + 1
			if rowNum == headerRow:
				for col in row:
					# Format column name to remove unwanted chars
					#txt = col.replace(' ', '_')
					cols.append(col)
		txt = GenerateSQL_CreateTable(tbl, cols)
		print ( txt)
		#dat.appendToFile(opFile, txt)
		SQL_file.write(txt)
		
	# now generate the inserts
	with open(csvFile) as input_file:
		for row in csv.reader(input_file, delimiter=','):
			SQL_file.write(GenerateSQL_Insert(tbl, row, cols))
		SQL_file.write('COMMIT;')
	
		
def GenerateSQL_CreateTable(tbl, cols):
	txt = 'DROP TABLE ' + tbl + ' CASCADE CONSTRAINTS;\n'
	txt = txt + 'CREATE TABLE ' + tbl + ' ( \n'
	for c in cols:
		if c != '':
			txt = txt + '    ' + c + ' VARCHAR2(200), \n'
	txt = txt + '    REC_EXTRACT_DATE DATE\n);\n\n'
	return txt

def GenerateSQL_Insert(tbl, row, cols):
	txt = 'INSERT INTO ' + tbl + ' ('
	for c in cols:
		if c != '':
			txt = txt + c + ', '
	txt = txt + 'REC_EXTRACT_DATE) VALUES (\n'
	for d in row:
		if d != '':
			txt = txt + '\'' + d.strip().replace('\'','\'\'') + '\'' + ', '
	txt = txt + ' sysdate ); \n'
	return txt

	
if __name__ == '__main__':
    TEST()	
	

