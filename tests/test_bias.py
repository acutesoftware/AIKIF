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

    def test_01_str(self):
        self.bias = mod_bias.Bias(test_metadata)
        self.assertEqual(len(str(self.bias)), 153)
        #print(self.bias)

    def test_02_calc_bias(self):
        bias = mod_bias.Bias(test_metadata)
        self.assertEqual(bias.get_bias_rating(),  5.9457650345124735e-09)


        
    def test_07_sample_data(self):
        dat = ['website:twitter,sender:@random,text:"Really love the new Star Wars film"',
               'website:wikipedia,page:https://en.wikipedia.org/wiki/Exilioidea, text:"Exilioidea is a genus of sea snails, marine gastropod mollusks in the family Ptychatractidae"',
               'source:person,actor:self,text:"I like cheese"',
               ]
        for d in dat:
            #bias = mod_bias.Bias(d[0],d[1],d[2])
            #print(d)
            pass
 
 
 
if __name__ == '__main__':
    unittest.main()