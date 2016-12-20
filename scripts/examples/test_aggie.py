#!/usr/bin/python3
# coding: utf-8
# test_bias.py

import unittest
import sys
import os

import aggie 

class TestAggie(unittest.TestCase):
    def test_01_import(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
