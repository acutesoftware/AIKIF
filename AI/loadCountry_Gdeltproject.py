# loadCountry_Gdeltproject.py   written by Duncan Murray 23/2/2014  (C) Acute Software
# script to manage GDELT Project files
#
		# CODE	LABEL
		#WSB	West Bank
		#BAG	Baghdad
		#GZS	Gaza Strip
		#AFR	Africa


# idea is to document where the datasets are coming from and how they are loaded into Tables
# and or python structures (preferably SQL tables)

 
import os
import sys
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
import AIKIF_utils as aikif
import fileMapping as filemap


srcURL = 'http://gdeltproject.org/data/lookups/CAMEO.country.txt'
tmpFile = filemap.GetDataPath() + '\CAMEO.country.txt'
location_fileList = filemap.GetFullFilename(filemap.FindType('location'), 'WORLD')   	

# Standard functions for all loading scripts to allow querying from file mapper and checker
def GetSrcURL(): return srcURL
def GetTempFile(): return tmpFile
def GetOutputFile(): return location_filelist

#print('sys.argv[0] = ' + sys.argv[0])
#print('sys.argv[1] = ' + sys.argv[1])
#print('sys.argv[2] = ' + sys.argv[2])

silent = 'N'
if len(sys.argv) == 2:
	if sys.argv[1] == 'Q':
		silent = 'Y'

		
def main():
	if silent == 'N':
		print('-----------------------------------')
		print('Loading DataSets from GDelt project')
		print('-----------------------------------')
	aikif.LogDataSource(srcURL)
	net.DownloadFile(srcURL, tmpFile)
	LoadCountryFile(tmpFile, location_fileList )
	#MapFilesToOntology(location_fileList, ??)
	
def MapFilesToOntology(fname, itm):
	pass
	return 'TODO'

def LoadCountryFile(ipFile, opFile):
	lst = fle.LoadFileToList(ipFile)
	if silent == 'N':
		print('Saving master country list to ' + opFile + ' from ' + ipFile)
		print(lst)
	for itm in lst:
		pass
		#print(itm)
	
if __name__ == '__main__':
    main()	
	
	
	