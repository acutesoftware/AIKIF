#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_ontology_review.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'ontology' 
sys.path.append(pth)

import review_ontology

class TestToolboxClsGridLife(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        review_ontology.main()
        
    def test_02_file_samples(self):
        self.assertEqual(os.path.exists('review_file_samples.html'), True)
        
    def test_03_output_as_html(self):
        self.assertEqual(os.path.exists('review_ontology.html'), True)
        
    def test_04_output_as_text(self):
        self.assertEqual(os.path.exists('review_ontology.txt'), True)

    
    
if __name__ == '__main__':
    unittest.main()
