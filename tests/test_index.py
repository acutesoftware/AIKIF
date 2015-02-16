# test_index.py     written by Duncan Murray 20/3/2014
# unit testing for AIKIF - test the indexing

import unittest
import os
import sys
import csv
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' )
import index as ndx

ip_file_normal = 'test_results//index_normal_source.txt'
op_file_normal = 'test_results//index_normal_results.txt'
ip_file_odd_chars = 'test_results//index_odd_chars_source.txt'
op_file_odd_chars = 'test_results//index_odd_chars_results.txt'

class TestIndex(unittest.TestCase):
 
        
	def test_01_index_normal_text(self):
		# test.txt, file, 1 2
		# test.txt, has, 2
		# test.txt, is, 1
		# test.txt, lines, 2
		# test.txt, normal, 1
		# test.txt, particular, 2
		# test.txt, text, 1 2
		# test.txt, this, 1 2
		# test.txt, two, 2	
		with open(ip_file_normal, "w") as myfile:
			myfile.write('This is a normal text file\nThis particular text file has two lines\n')
		ndx.buildIndex(ip_file_normal, op_file_normal, 'N', 'N')	# run the index routine
		self.assertEqual( CountLines(op_file_normal), 9)	# make sure there are 9 lines in index

	def test_02_index_odd_characters(self):
		# test.txt, aaa, 1 2 3 3
		# test.txt, bbb, 1 3 3 3
		# test.txt, ccc, 2 3 3 3 3
		with open(ip_file_odd_chars, "w") as myfile:
			myfile.write('AAA_BBB\n ccc-AaA \nBbB CCC*cCc%ccC   aaa&bbb&ccc  ---AAa-$%#%$BBB')
		ndx.buildIndex(ip_file_odd_chars, op_file_odd_chars, 'N', 'N')	# run the index routine
		self.assertEqual( CountLines(op_file_odd_chars), 3)	# make sure there are 3 lines in index

	def test_03_wordList_function(self):
		totWords, totLines, indexedWords = ndx.getWordList(ip_file_odd_chars, [' '])
		self.assertEqual( totWords, 11)	# make sure there are  11 words in odd chars file
		self.assertEqual( totLines, 3)	# make sure there are 3 lines in index file
		self.assertEqual( len(indexedWords), 7)	# make sure there are 7 indexed words (not sure why it isnt 3 - TODO - check)

def CountLines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
		
if __name__ == '__main__':
	unittest.main()