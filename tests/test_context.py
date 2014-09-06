# test_context.py     written by Duncan Murray 6/9/2014
# unit testing for context class

import unittest
import os
import sys
import csv
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
print("in test_cls_file : root_folder = " + root_folder)
sys.path.append(root_folder)

import aikif.lib.cls_file as cl
					
class TestClassFile(unittest.TestCase):
 
	def test_01_instantiation(self):
		print('hello')
