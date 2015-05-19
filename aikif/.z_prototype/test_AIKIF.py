# test_AIKIF.py     written by Duncan Murray 9/2/2014
# unit testing for AIKIF

import unittest
import os
import sys
import csv
sys.path.append('..//..//_AS_LIB')
sys.path.append('..//AI')

import AIKIF_utils as aikif

class TestAIKIF(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( 3*4, 12)
 
    def test_build_AIKIF_structure(self):
        self.assertEqual( len(aikif.build_AIKIF_structure()), 10)
 
if __name__ == '__main__':
    unittest.main()