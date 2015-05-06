# test_knowledge.py

import unittest
import sys
import os
import aikif.knowledge as knowledge

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")

class KnowledgeTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.k = knowledge.Knowledge('test') 
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    def test_01_instantiate(self):
        self.assertEqual(len(str(self.k)) , 134) 
 
 
        
if __name__ == '__main__':
    unittest.main()