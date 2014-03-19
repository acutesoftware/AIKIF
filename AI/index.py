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

	ndxFile = 'ndxAll.txt'
	with open(ndxFile, "w") as ndx:
		ndx.write('filename, word, linenumbers\n')

	files_to_index = fle.GetFileList([filemap.GetDataPath()], ['*.csv'], ["__pycache__", ".git"])
	for f in files_to_index:
		buildIndex(f, ndxFile, silent)
	#buildIndex('..//data//test-file.txt', ndxFile, silent)
	
	# now build the one big index file
	consolidate(ndxFile)

	aikif.LogProcess('Finished indexing',  'index.py')   #, fle.GetModuleName())
	if silent == 'N':
		print('Done')


def buildIndex(ipFile, ndxFile, append='Y', silent='N'):
	# this creates an index of a text file specifically for use in AIKIF
	# separates the ontology descriptions highest followed by values and lastly
	# a final pass to get all delimited word parts.
	numWords = 0
	numWordParts = 0
	totWordCount = 0
	if silent == 'N':
		pass
		#print('indexing ' + ipFile)
	delims = [',', '"', '/', '.', ':', '!', '?', '-', '_', ' ', '\n']
	# 1st pass - index the ontologies, including 2 depths up (later - TODO)
	#buildIndex(ipFile, ndxFile, ' ', 1, 'Y')

	# 2nd pass - use ALL delims to catch each word as part of hyphenated - eg AI Build py
	totWords, totLines, uniqueWords = getWordList(ipFile, delims)
	
	AppendIndexDictionaryToFile(uniqueWords, ndxFile, ipFile)
	print(ipFile + ' has ' + str(totLines) + ' lines, ' + str(totWords) + ' words (' + str(len(uniqueWords)) + ' unique words)')
	if silent == 'N':
		pass
		#show('uniqueWords', uniqueWords, 5)
	#print(uniqueWords)  # this is now a DICTIONARY with no key names - TODO - how to save properly
	#DisplayIndexAsDictionary(uniqueWords)

def AppendIndexDictionaryToFile(uniqueWords, ndxFile, ipFile):
	#Save the list of unique words to the master list
	with open(ndxFile, "a") as ndx:
		word_keys = uniqueWords.keys()
		#uniqueWords.sort()
		for word in sorted(word_keys):
			if word != '':
				line_nums = uniqueWords[word]
				ndx.write(ipFile + ', ' + word + ', ')
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
	f = open(ipFile, 'r')
	for line in f:
		totLines = totLines + 1
		words = multi_split(line, delim)
		totWords = totWords + len(words)
		#show('orig words', words)
		for cleanedWord in words:
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
			if word != '':
				res += word.split(delimChar)
	return res

	
def consolidate(fname):
	print('TODO - you now need to consolidate the indexes by unique words')
	pass
		
if __name__ == '__main__':
    index()	
	

