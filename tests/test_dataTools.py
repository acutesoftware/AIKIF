# test_dataTools.py     written by Duncan Murray 20/6/2014
# unit testing for dataTools module

import unittest
import os
import sys
import csv
sys.path.append("..\\AI")
from dataTools import dataTools as cl
					
class TestClassCollect(unittest.TestCase):
 
	def setUp(self):
		pass

	def test_collect(self):
		self.assertEqual(cl.clean_column_heading('date'), 'DATE')  # should be one file (this one)
		self.assertEqual(cl.clean_column_heading('Country'), 'COUNTRY')  # should be one file (this one)
		self.assertEqual(cl.clean_column_heading('country of birth'), 'COUNTRY_OF_BIRTH')  # should be one file (this one)
		
		
if __name__ == '__main__':
	unittest.main()