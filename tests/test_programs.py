# test_programs.py	written by Duncan Murray 30/10/2014

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif' ) 
sys.path.append(root_folder) # TODO - remove this before publish to pypi
import programs as mod_prg
					
class TestPrograms(unittest.TestCase):
 
	def setUp(self):
		self.prg = mod_prg.Programs('test list', root_folder)

	def test_01_instantiate(self):
		#print(self.prg)
		self.assertEqual(len(str(self.prg)) > 2, True) 

		
		
if __name__ == '__main__':
	unittest.main()