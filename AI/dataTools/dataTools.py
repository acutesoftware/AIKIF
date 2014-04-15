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




def TEST():
	print('Data tools test...')
	testFile = 'test.csv'
	CreateRandomCSVFile(testFile)
	GenerateSQL(testFile, headerRow=1)
	

def CreateRandomCSVFile(fname):
	fle.deleteFile(fname)
	content = [['id', 'code', 'desc'], ['1', 'S', 'AAA'], ['2', 'B', 'BBB'], ['3', 'X', 'Long description']]
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


	
		
def GenerateSQL(csvFile, headerRow=1):
	# top level function
	tbl = os.path.basename(csvFile).split('.')[0]
	opFile = os.path.basename(csvFile).split('.')[0] + '.SQL'
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
	

