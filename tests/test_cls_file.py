# test_cls_file.py     written by Duncan Murray 22/6/2014
# unit testing for collection class

import unittest
import os
import sys
import csv
sys.path.append("..\\AI\\lib")
import cls_file as cl
					
class TestClassFile(unittest.TestCase):
 
	def setUp(self):
		self.fname = 'test_results/cls_file_test_data.txt'

	def test_file_create(self):
		self.assertEqual(1, 1)  # dummy
		f = cl.File(self.fname)
		f.delete()
		f.append_text('# test file for cls_file\n')
		f.append_text('this is the 2nd line\n')
		f.append_text('this is the last line\n')
		
	def test_file_print(self):
		f = cl.File(self.fname)
		print(f)

	def test_file_load_string(self):
		f = cl.File(self.fname)
		txt = f.load_file_to_string()
		self.assertEqual(len(txt), 68) 

	def test_file_load_list(self):
		f = cl.File(self.fname)
		lst = f.load_file_to_list()
		self.assertEqual(len(lst), 3) 
		
	
	def test_file_delete(self):
		f = cl.File(self.fname)
		
		#f.delete()
		
		
if __name__ == '__main__':
	unittest.main()