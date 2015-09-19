# test_knowledge.py

import unittest
import sys
import os
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' )

import knowledge

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")

class KnowledgeTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.k = knowledge.Knowledge('test') 
        self.r = knowledge.RawData('test')
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    def test_01_instantiate(self):
        self.assertEqual(len(str(self.k)) , 134) 
 
    def test_02_rawdata(self):
        self.assertEqual(str(self.r) , 'raw_data: test (0 entries)\n') 
        self.r.add('the dog chases the cat')
        self.r.add('the cat eats the fish')
        self.r.add('the fish is out of luck')
        #print(self.r)
        self.assertEqual(len(self.r.data) , 3) 
        self.assertEqual(self.r.find('cat') , ['the dog chases the cat', 'the cat eats the fish']) 
        self.assertEqual(self.r.find('dog') , ['the dog chases the cat']) 
    
    def test_03_fact(self):
        f = knowledge.Fact()
        self.assertEqual(f.process(self.r) , True) 
        self.assertEqual(f.verify() , True) 
 

    
        
if __name__ == '__main__':
    unittest.main()