# coding: utf-8
# load_ABS_data.py   written by Duncan Murray 16/4/2014  (C) Acute Software
# script to load multiple ABS data files
#

# http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_poa_2011_aust_csv.zip&1270.0.55.003&Data%20Cubes&7A0CD4B1AD71C814CA2578D40012D4B2&0&July%202011&22.07.2011&Previous
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

downloads = [
    {'name': 'Australian and New Zealand Standard Commodity Classification (ANZSCC), 1997 (cat no. 1254.0)',
	'pageURL': 'http://www.abs.gov.au/AUSSTATS/abs@.nsf/ViewContent?readform&view=ProductsbyTopic&Action=Expand&Num=7.1.5',
	'downloadURL': 'http://www.abs.gov.au/AUSSTATS/abs@.nsf/ProductsbyTopic/F1B37227B80E36F6CA25722E0017B274?OpenDocument',
	'zipFile': 'PDF.zip',
	'localFile': 'this.PDF',
	'comment': ''},
    {'name': 'Postcodes',
	'pageURL': 'https://index.okfn.org/country/Australia/postcodes/',
	'downloadURL': 'http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_poa_2011_aust_shape.zip&1270.0.55.003&Data%20Cubes&71B4572D909B934ECA2578D40012FE0D&0&July%202011&22.07.2011&Previous',
	'zipFile': '1270055003_poa_2011_aust_shape.zip',
	'localFolder': 'S:\\DATA\\opendata\\datasets\\ABS\\postcodes',
	'localFile': 'AAA.csv',
	'comment': ''},
    {'name': 'ABS Suburbs (not joined)',
	'pageURL': '',
	'downloadURL': 'http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_ssc_2011_aust_csv.zip&1270.0.55.003&Data%20Cubes&414A81A24C3049A8CA2578D40012D50C&0&July%202011&22.07.2011&Previous',
	'zipFile': '1270055003_poa_2011_aust_csv.zip',
	'localFile': 'BBB.csv',
	'comment': ''},
    {'name': 'Names list from Princeton',
	'pageURL': '',
	'downloadURL': 'http://www.cs.princeton.edu/introcs/data/names.csv',
	'zipFile': 'names.csv',
	'localFolder': 'S:\\DATA\\opendata\\datasets\\',
	'localFile': 'names.csv',
	'comment': ''}
	]
	
	
	
# weather datasets = http://data.gov.au/dataset/precis-forecast-south-australia
# weather (XML) = http://data.gov.au/dataset/precis-forecast-south-australia/resource/fb1793f4-e3b8-4a26-b805-7a9a48a09b35

srcDataFolder = 'S:\\DATA\\opendata\\datasets\\ABS'

silent = 'N'
if len(sys.argv) == 2:
	if sys.argv[1] == 'Q':
		silent = 'Y'

def extractZip(ip, op):
	print('extracting ' + ip + ' to ' + op)
	
		
def main():
	if silent == 'N':
		print('---------------------------')
		print('Loading Australian Datasets')
		print('---------------------------')
	
	for d in downloads:
		aikif.LogDataSource(d['name'], fle.GetModuleName())
		try:
			loc_fldr = d['localFile']
		except:
			loc_fldr = srcDataFolder + '\\'
		net.DownloadFile(d['downloadURL'], loc_fldr + d['zipFile'])
		extractZip(d['zipFile'], d['localFile'])
	#locations = LoadAustPostcodeFile(tmpFile, location_fileList )
	#MapFilesToOntology(location_fileList, ??)
	#aikif.SaveFileDataToFile(locations, location_fileList)

def MapFilesToOntology(fname, itm):
	pass
	return 'TODO'

def LoadAustPostcodeFile(ipFile, opFile):
	locations = [[0, 'country_code', 'country_desc']]
	location_key = 0
	country_code = ''
	country_desc = ''
	f = open(ipFile, 'r')
	
	if silent == 'N':
		print('Saving master country list to ' + opFile + ' from ' + ipFile)
		
	for line in f:
		if len(line) > 0:
			#cols = line.split('\t')
			country_code = line[0:3].strip()
			country_desc = line[4:].strip()
			#print('line = ' + line + ', country_code = ' + country_code + ' country_desc = ' + country_desc)
			location_key = location_key + 1
			locations.append([location_key, country_code, country_desc])
			#print(itm)
	f.close()
	return locations
	
if __name__ == '__main__':
    main()	
	
	
	