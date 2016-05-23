#!/usr/bin/python3
# coding: utf-8
# test_bias.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)

import bias as mod_bias

test_metadata = [
    {'label':'collection-method', 'value': 'website'},
    {'label':'website', 'value': 'abs.gov.au'},
    {'label':'source-type', 'value': 'published-data'},
    {'label':'person-relationship', 'value': 'unknown'},
]

dummy_metadata = [  # source_area, source_type, source_website, source_person
    {'label':'collection-method', 'value': 'AAA'},
    {'label':'source-type', 'value': 'BBB'},
    {'label':'website', 'value': 'CCC'},
    {'label':'person-relationship', 'value': 'DDD'},
]


class BiasTest(unittest.TestCase):
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        

    def test_01_str(self):
        self.bias = mod_bias.Bias(test_metadata)
        self.assertEqual(len(str(self.bias)), 149)

    def test_02_calc_bias(self):
        bias = mod_bias.Bias(test_metadata)
        self.assertEqual(bias.get_bias_rating(), 14.848288519170794) # 5.9457650345124735e-09)

    def test_03_controversy_low(self):
        low_cont = mod_bias.Controversy('maths')
        self.assertTrue(low_cont.get_controversy() < 0.2)
        self.assertEqual(str(low_cont), 'Controversy: maths controversy=0.01 noise=0.1\n')

    def test_04_controversy_high(self):
        high_cont = mod_bias.Controversy('religion')
        self.assertTrue(high_cont.get_controversy() > 0.8)
        self.assertEqual(str(high_cont), 'Controversy: religion controversy=0.95 noise=0.9\n')

    def test_05_controversy_wrong_data(self):
        unknown_cont = mod_bias.Controversy('JujdfjrtigdFF')
        self.assertEqual(unknown_cont.get_controversy(), 0)
        self.assertEqual(unknown_cont.get_noise(), 0)
        self.assertEqual(str(unknown_cont), 'Controversy: JujdfjrtigdFF controversy=0 noise=0\n')
        
    def test_06_get_bias_details(self):
        bias5 = mod_bias.Bias(test_metadata)
        self.assertEqual(bias5.get_bias_details()[0:17], 'Bias File Details')
        self.assertTrue(len(bias5.get_bias_details()) > 200)
    
    def test_07_sample_data(self):
        dat = ['website:twitter,sender:@random,text:"Really love the new Star Wars film"',
               'website:wikipedia,page:https://en.wikipedia.org/wiki/Exilioidea, text:"Exilioidea is a genus of sea snails, marine gastropod mollusks in the family Ptychatractidae"',
               'source:person,actor:self,text:"I like cheese"',
               ]
               
        more_metadata = [
            {'label':'test_label', 'value': 'test_value'},
        ]
        bias = mod_bias.Bias(more_metadata)
        self.assertEqual(str(bias), """Bias
test_label = test_value
BIAS Rating    = 1
""")
        
        
        for d in dat:
            print(d)
            pass
 
 
 
if __name__ == '__main__':
    unittest.main()