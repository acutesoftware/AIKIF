# test_dataTools.py     written by Duncan Murray 20/6/2014
# unit testing for dataTools module

import unittest
import os
import sys
import csv
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)

from aikif.dataTools import dataTools as cl
					
class TestClassDataTools(unittest.TestCase):
 
	def setUp(self):
		pass

	def test_clean_col_upper(self):
		self.assertEqual(cl.clean_column_heading('date'), 'DATE') 
		self.assertEqual(cl.clean_column_heading('Date'), 'DATE') 
		
	def test_clean_col_bad_chars(self):
		self.assertEqual(cl.clean_column_heading('__Country_@@@_'), 'COUNTRY') 
		self.assertEqual(cl.clean_column_heading('phone$%#$'), 'PHONE') 
		self.assertEqual(cl.clean_column_heading('_First_name?*__'), 'FIRST_NAME') 
		
	def test_clean_col_spaces(self):
		self.assertEqual(cl.clean_column_heading('country of birth'), 'COUNTRY_OF_BIRTH') 
		self.assertEqual(cl.clean_column_heading('country of birth '), 'COUNTRY_OF_BIRTH')  
		self.assertEqual(cl.clean_column_heading(' country of birth'), 'COUNTRY_OF_BIRTH')  
		
		
if __name__ == '__main__':
	unittest.main()