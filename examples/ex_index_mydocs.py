# coding: utf-8
# ex_index_mydocs.py	written by Duncan Murray 22/5/2014
# Example program to index all personal data for keyword searches using AIKIF.
# Source data is taken from Acute Softwares Diary and FileLister

import os
import sys
sys.path.append('..//..//aspytk')
import lib_file as fle

sys.path.append('..//AI')
import index as ndx

local_folder = 'T:\\user\\AIKIF\\diary\\'
diary_folder = 'C:\\APPS\\netDiary\\data'

manual_files_to_index = [
	local_folder + 'diary_Ent_duncan.txt',
	local_folder + 'lf_folders.csv',
	local_folder + 'lf_files.csv'
	]

delims = [' ', '\\', '/', '_']

ndxFile = 'T:\\user\\AIKIF\\pers_data\\ndx_temp.txt'
ndxFile_final = 'T:\\user\\AIKIF\\pers_data\\ndx_final.txt'

def main():
	try:
		os.remove(ndxFile)
	except:
		pass
	all_files = add_diary_files_to_list(manual_files_to_index, diary_folder)	
	numFiles = 0
	for f in all_files:
		try:
			#totWords, totLines, indexedWords = ndx.getWordList(f, delims)
			#print('words=', str(totWords), ',lines=', str(totLines), ',ndx=', str(len(indexedWords)), ' in ', f)
			numFiles += 1
			print('indexing ', str(numFiles) , ' of ', str(len(all_files)), ' : ', f)
			ndx.buildIndex(f, ndxFile, 'Y', 'N')	# run the index routine
		except:
			print('ERROR - cant index file ', f)

	print('consolidating.... ')		
	ndx.consolidate(ndxFile, ndxFile_final)	
	print('Done!')		

def add_diary_files_to_list(lst, fldr):
	""" adds all Diary files from folder to the lst   """
	fl = fle.GetFileList([fldr], ['D2014*.DAT'], ["__pycache__", ".git"], True)
	for f in fl:
		lst.append(f)
	return lst
	
if __name__ == '__main__':		
	main()
