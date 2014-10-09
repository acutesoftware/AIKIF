# test_bias.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)

import bias as mod_bias

class BiasTest(unittest.TestCase):

    def test_01_str(self):
        self.bias = mod_bias.Bias('gov.au', 'published_data', 'abs.gov.au', '')
        self.assertEqual(len(str(self.bias)), 130)

    def test_02_calc_bias(self):
        bias = mod_bias.Bias('gov.au', 'published_data', 'abs.gov.au', '')
        self.assertEqual(bias.get_bias_rating(), 0.863)

 
if __name__ == '__main__':
    unittest.main()