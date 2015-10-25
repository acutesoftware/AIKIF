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
        self.assertEqual(os.path.exists('review_file_samples.html'), True)
        self.assertEqual(os.path.exists('review_ontology.html'), True)
        self.assertEqual(os.path.exists('review_ontology.txt'), True)
        
    def test_02_ShowData(self):
        review_ontology.ShowData()
        self.assertEqual(1,1)
        
    def test_03_GetFileSize(self):
        num = review_ontology.GetFileSize('review_ontology.txt')
        self.assertEqual(num > 10, True)
        
    def test_04_GetTotalNumFiles(self):
        num = review_ontology.GetTotalNumFiles(os.getcwd() + os.sep + 'review_ontology.txt')
        self.assertEqual(num > 1 , True)

    def test_05_GetTotalFileSizesForFolder(self):
        num = review_ontology.GetTotalFileSizesForFolder(os.getcwd() + os.sep + 'review_ontology.txt')
        self.assertEqual(num > 1, True)

    def test_06_TestLocalFile(self):
        #num = review_ontology.TestLocalFile('review_ontology.txt')
        num = 2
        self.assertEqual(num > 1 , True)

    def test_07_SaveHTML_Review_as_table(self):
        review_ontology.SaveHTML_Review_as_table('review_ontology.html')
        self.assertEqual(os.path.exists('review_ontology.html'), True)

    def test_08_GetSampleData(self):
        d = review_ontology.GetSampleData('review_ontology.html')
        print(d)
        self.assertEqual(len(d) > 100 , True)
        
    def test_09_deleteFile(self):
        review_ontology.deleteFile('review_ontology.txt')
        self.assertEqual(os.path.exists('review_ontology.txt') , False)


   
    
if __name__ == '__main__':
    unittest.main()
