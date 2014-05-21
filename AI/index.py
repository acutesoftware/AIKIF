# coding: utf-8
# index.py	written by Duncan Murray 19/3/2014	(C) Acute Software
# Indexes all the data in AIKIF for fast searching

import os
import sys
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
import AIKIF_utils as aikif
import fileMapping as filemap

silent = 'N'
if len(sys.argv) == 2:
	if sys.argv[1] == 'Q':
		silent = 'Y'

ndxPath = filemap.GetDataPath() + '\\index'
		
def index():
	# main function - outputs in following format BEFORE consolidation (which is TODO)
	# filename, word, linenumbers
	# T:\user\dev\src\python\AI\data\refAction.csv, ActionTypeName, 1
	# T:\user\dev\src\python\AI\data\refAction.csv, PhysicalType, 1
	# T:\user\dev\src\python\AI\data\refAction.csv, space, 2 3
	# T:\user\dev\src\python\AI\data\goals.csv, Cleanliness, 11
	# T:\user\dev\src\python\AI\data\goals.csv, Concept, 6 7 8 9 11

	
	aikif.LogProcess('Starting indexing',  'index.py') # sys.modules[self.__module__].__file__)
	if silent == 'N':
		print('------------------')
		print('Rebuilding Indexes')
		print('------------------')	

	ndxFile = ndxPath + '\\ndxFull.txt'
	opIndex = ndxPath + '\\ndxWordsToFiles.txt'
	with open(ndxFile, "w") as ndx:
		ndx.write('filename, word, linenumbers\n')

	files_to_index = fle.GetFileList([filemap.GetDataPath() + '\\core'], ['*.csv'], ["__pycache__", ".git"])
	for f in files_to_index:
		buildIndex(f, ndxFile, silent)
	#buildIndex('..//data//test-file.txt', ndxFile, silent)
	
	# now build the one big index file
	consolidate(ndxFile, opIndex )

	aikif.LogProcess('Finished indexing',  'index.py')   #, fle.GetModuleName())
	if silent == 'N':
		print('Done')


def buildIndex(ipFile, ndxFile, append='Y', silent='N', useShortFileName='Y'):
	# this creates an index of a text file specifically for use in AIKIF
	# separates the ontology descriptions highest followed by values and lastly
	# a final pass to get all delimited word parts.
	numWords = 0
	numWordParts = 0
	totWordCount = 0
	if silent == 'N':
		pass
	if append == 'N':
		fle.deleteFile(ndxFile)
		#print('indexing ' + ipFile)
	delims = [',', '$', '&', '"', '%', '/', '.', ';', ':', '!', '?', '-', '_', ' ', '\n', '*', '\'', '(', ')', '[', ']', '{', '}']
	# 1st pass - index the ontologies, including 2 depths up (later - TODO)
	#buildIndex(ipFile, ndxFile, ' ', 1, 'Y')

	# 2nd pass - use ALL delims to catch each word as part of hyphenated - eg AI Build py
	totWords, totLines, uniqueWords = getWordList(ipFile, delims)
	
	AppendIndexDictionaryToFile(uniqueWords, ndxFile, ipFile, useShortFileName)
	if silent == 'N':
		pass
		print(fle.GetShortFileName(ipFile).ljust(30) + ' ' + str(totLines).rjust(6) + ' lines ' + str(totWords).rjust(6) + ' words ' + str(len(uniqueWords)).rjust(6) + ' unique words')
	
		#show('uniqueWords', uniqueWords, 5)
	#print(uniqueWords)  # this is now a DICTIONARY with no key names - TODO - how to save properly
	#DisplayIndexAsDictionary(uniqueWords)

def AppendIndexDictionaryToFile(uniqueWords, ndxFile, ipFile, useShortFileName='Y'):
	#Save the list of unique words to the master list
	if useShortFileName == 'Y':
		f = fle.GetShortFileName(ipFile)
	else:
		f = ipFile
	with open(ndxFile, "a", encoding='utf8') as ndx:
		word_keys = uniqueWords.keys()
		#uniqueWords.sort()
		for word in sorted(word_keys):
			if word != '':
				line_nums = uniqueWords[word]
				ndx.write(f + ', ' + word + ', ')
				for line_num in line_nums:
					ndx.write(str(line_num))
				ndx.write('\n')
				
def DisplayIndexAsDictionary(word_occurrences):
	word_keys = word_occurrences.keys()
	for word in word_keys:
		line_nums = word_occurrences[word]
		print(word + " ")
		for line_num in line_nums:
			print(str(line_num) + " ")
		print("\n")

			
def show(title, lst, full=-1):
	# for testing, simply shows a list details
	txt = title + ' (' + str(len(lst)) + ') items :\n '
	num = 0
	for i in lst:
		if full == -1 or num < full:
			if type(i) is str:
				txt = txt + i + ',\n '
			else:
				txt = txt + i + ', ['
				for j in i:
					txt = txt + i + ', '
				txt = txt + ']\n'
		num = num + 1
	print(txt)
	
def getWordList(ipFile, delim, headersOnly='N'):
	# extract a unique list of words and have line numbers that word appears
	indexedWords = {}
	totWords = 0
	totLines = 0
	f = open(ipFile, 'r', encoding='utf8')
	for line in f:
		totLines = totLines + 1
		words = multi_split(line, delim)
		totWords = totWords + len(words)
		#show('orig words', words)
		for word in words:
			cleanedWord = word.lower().strip()
			if cleanedWord not in indexedWords:
				#indexedWords[cleanedWord] = cleanedWord + ' ' + str(totLines)
				indexedWords[cleanedWord] =  str(totLines)
			else:
				#indexedWords[cleanedWord] = indexedWords[cleanedWord] + ' ' + str(totLines)
				indexedWords[cleanedWord] = indexedWords[cleanedWord] + ' ' + str(totLines)
	f.close()
	#print ('total words = ' + str(len(indexedWords)))
	#show('indexedWords', indexedWords, 50)
	return totWords, totLines, indexedWords

def multi_split(txt, delims):
	res = [txt]
	for delimChar in delims:
		txt, res = res, []
		for word in txt:
			if len(word) > 1:
				res += word.split(delimChar)
	return res

	
def consolidate(ipFile, opFile):
	# make a single index file with 1 record per word which shows the word, file and linenums
		# storms, knowledge.csv - 3
		# string, rawData.csv - 1
		# structure, EVENT_SYSTEM-PC-FILE.CSV - 18, OBJECT_SYSTEM-PC-FILE.CSV - 4, sample-filelist-for-AIKIF.csv - 18 18
		# subgoal, goals.csv - 3 4 12 13 14, goal_types.csv - 8
		# subgoals, goal_types.csv - 9
		# subgoals;, goals.csv - 2
	curFile = ''
	curWord = ''
	curLineNums = ''
	indexedWords = {}
	with open(ipFile, "r", encoding='utf8') as ip:
		for line in ip:
			cols = line.split(',')
			curFile = cols[0]
			curWord = cols[1]
			curLineNums = cols[2].strip()
			#DebugIndexing(curFile, curWord, curLineNums, line)
			if curWord in indexedWords:
				indexedWords[curWord] =  indexedWords[curWord] + ', ' + curFile + ' - ' + curLineNums
			else:
				indexedWords[curWord] = curFile + ' - ' + curLineNums
	with open(opFile, "w", encoding='utf8') as op:
		op.write('word, filenames\n')  # this shows which words appear in which files
		word_keys = indexedWords.keys()
		for word in sorted(word_keys):
			if word != '':
				line_nums = indexedWords[word]
				op.write(word + ', ')
				for line_num in line_nums:
					op.write(str(line_num))
			op.write('\n')
	


	

def DebugIndexing(curFile, curWord, curLineNums, line):
	print('line = ' + line)
	print('curFile = ' + curFile)
	print('curWord = ' + curWord)
	print('curLineNums = ' + curLineNums)
	
		
if __name__ == '__main__':
    index()	
	

