#!/usr/bin/python3
# coding: utf-8
# test_bias.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)

import comms as mod_comms


dummy_comms = [
    {'key':'value'},
]


class CommsTest(unittest.TestCase):
    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_01_begin(self):
        #self.comms = mod_bias.Bias(test_metadata)
        mod_comms.TEST()
        self.assertEqual(1,1)



if __name__ == '__main__':
    unittest.main()
