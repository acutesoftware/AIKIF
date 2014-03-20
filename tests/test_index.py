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
		self.assertEqual( len(open(opTestFile).readlines()), 9)	# make sure there are 9 lines in index

	def test_index_odd_characters(self):
		# test.txt, aaa, 1 2 3 3
		# test.txt, bbb, 1 3 3 3
		# test.txt, ccc, 2 3 3 3 3
		with open('test.txt', "w") as myfile:
			myfile.write('AAA_BBB\n ccc-AaA \nBbB CCC*cCc%ccC   aaa&bbb&ccc  ---AAa-$%#%$BBB')
		ndx.buildIndex(ipTestFile, opTestFile, 'N', 'N')	# run the index routine
		self.assertEqual( len(open(opTestFile).readlines()), 3)	# make sure there are 3 lines in index


		
if __name__ == '__main__':
	unittest.main()