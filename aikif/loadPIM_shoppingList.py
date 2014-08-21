# coding: utf-8
# loadPIM_shoppingList.py   written by Duncan Murray 23//2014  (C) Acute Software3
# Manually adds and maps Personal Information data
# This script loads shopping list items
		#--Shopping--
		#Milk
		#Lettuce
		#Bread
		#Apples


import os
import sys
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
import AIKIF_utils as aikif
import fileMapping as filemap


srcURL = filemap.GetDataPath() + '\\raw\\shoppingList.txt'

subjectArea = filemap.FindOntology('shopping') # should return 'INFO-PIM-SHOPPING'
#print ( 'subjectArea = ' + subjectArea[0])

shopping_fileList = filemap.GetFullFilename(filemap.FindType('thing'), subjectArea[0])   


# Standard functions for all loading scripts to allow querying from file mapper and checker
def GetSrcURL(): return srcURL
def GetTempFile(): return tmpFile
def GetOutputFile(): return shopping_fileList

#print('sys.argv[0] = ' + sys.argv[0])
#print('sys.argv[1] = ' + sys.argv[1])
#print('sys.argv[2] = ' + sys.argv[2])

silent = 'N'
if len(sys.argv) == 2:
	if sys.argv[1] == 'Q':
		silent = 'Y'

		
def main():
	if silent == 'N':
		print('---------------------')
		print('Loading Shopping List')
		print('---------------------')
	aikif.LogDataSource(srcURL, fle.GetModuleName())
	CreateSampleShoppingList(srcURL)  # this should go to your live shopping list (diary, amazon wishlist, etc)
	shopping = LoadShoppingList(srcURL, shopping_fileList )
	#MapFilesToOntology(shopping_fileList, ??)
	#dat.SaveListToFile(shopping, shopping_fileList)  # was SaveFileDataToFile now SaveFileList
	aikif.SaveFileDataToFile(shopping, shopping_fileList)
	
def CreateSampleShoppingList(fname):
	shopping = [[ 'shopping_item', 'quant']]
	shopping.append([ 'Milk', '1L'])
	shopping.append([ 'Bread', '1 loaf'])
	shopping.append([ 'Apples', 'bag'])
	shopping.append([ 'Lettuce', '1'])
	aikif.SaveFileDataToFile(shopping, fname)
		
def LoadShoppingList(ipFile, opFile):
	shopping = [['key', 'item', 'quant']]
	shopping_key = 0
	f = open(ipFile, 'r')
	if silent == 'N':
		print('Saving shopping list to ' + opFile + ' from ' + ipFile)
		
	for line in f:
		if len(line) > 0:
			if '","' in line:
				flds = line.split('","')  
			else:
				flds = line.split(',')
			shopping_key = shopping_key + 1
			shopping.append([shopping_key, flds[0].strip().strip('"'), flds[1].strip().strip('"')])
	f.close()
	
	if silent == 'N':
		print('Loaded ' + str(len(shopping)-1) + ' shopping list items')
		print(shopping)
	return shopping
	
if __name__ == '__main__':
    main()	
	
	
	