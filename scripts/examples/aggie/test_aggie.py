#!/usr/bin/python3
# coding: utf-8
# test_bias.py

import unittest
import sys
import os

import aggie 

class TestAggie(unittest.TestCase):
    def test_01_hard_coded_answers(self):
        a = aggie.Aggie()
        self.assertEqual(a.answer('when is my dentist appointment'),'next week')
        self.assertEqual(a.answer('this is a contrived example'),'I dont'' know')
        self.assertEqual(a.answer('what is the weather in Spain'),'sunny')
        self.assertEqual(a.answer('where is the best picnic spot nearby'),'4km to the North')

if __name__ == '__main__':
    unittest.main()
