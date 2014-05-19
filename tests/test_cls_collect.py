# test_cls_collect.py     written by Duncan Murray 19/5/2014
# unit testing for collection class

import unittest
import os
import sys
import csv
sys.path.append('..//AI')
	
class TestClassCollect(unittest.TestCase):
 
	def setUp(self):
		pass


	def test_collect(self):
		sys.path.append("..\\AI")
		import cls_collect_files as cl
		my_files = cl.clsCollectFiles(os.getcwd())
		my_files.collect_filelist()
		self.assertEqual(len(my_files.get_filelist()), 0)  # for dummy test, there are zero files
		
		
if __name__ == '__main__':
	unittest.main()