# test_index.py     written by Duncan Murray 20/3/2014
# unit testing for AIKIF - test the indexing

import unittest
import os
import sys
import csv
sys.path.append('..//AI')
import AIKIF_utils as aikif
import index as ndx

ipTestFile = 'test.txt'
opTestFile = 'index.txt'

class TestAIKIF(unittest.TestCase):
 
	def setUp(self):
		pass
 
	def test_index_normal_text(self):
		# test.txt, file, 1 2
		# test.txt, has, 2
		# test.txt, is, 1
		# test.txt, lines, 2
		# test.txt, normal, 1
		# test.txt, particular, 2
		# test.txt, text, 1 2
		# test.txt, this, 1 2
		# test.txt, two, 2	
		with open('test.txt', "w") as myfile:
			myfile.write('This is a normal text file\nThis particular text file has two lines\n')
		ndx.buildIndex(ipTestFile, opTestFile, 'N', 'N')	# run the index routine
		self.assertEqual( CountLines(opTestFile), 9)	# make sure there are 9 lines in index

	def test_index_odd_characters(self):
		# test.txt, aaa, 1 2 3 3
		# test.txt, bbb, 1 3 3 3
		# test.txt, ccc, 2 3 3 3 3
		with open('test.txt', "w") as myfile:
			myfile.write('AAA_BBB\n ccc-AaA \nBbB CCC*cCc%ccC   aaa&bbb&ccc  ---AAa-$%#%$BBB')
		ndx.buildIndex(ipTestFile, opTestFile, 'N', 'N')	# run the index routine
		self.assertEqual( CountLines(opTestFile), 3)	# make sure there are 3 lines in index

	def test_wordList_function(self):
		totWords, totLines, indexedWords = ndx.getWordList(ipTestFile, [' '])
		self.assertEqual( totWords, 11)	# make sure there are  11 words in original file
		self.assertEqual( totLines, 3)	# make sure there are 3 lines in index file
		self.assertEqual( len(indexedWords), 7)	# make sure there are 7 indexed words (not sure why it isnt 3 - TODO - check)

def CountLines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
		
if __name__ == '__main__':
	unittest.main()