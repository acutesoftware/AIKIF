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

        
    def test_02_load_skills(self):
        s = aggie.Skills()
        s.add_skill(['Get Weather', 'return weather for [City]'])
        print(s)
        self.assertTrue(len(str(s)) > 5)
        self.assertEqual(len(s.skills), 1)
        
    def test_03_load_info(self):
        i = aggie.Info()
        i.add_fact(['[Me]', 'Name', 'My name is Aggie'])
        i.add_fact(['[Me]', 'What', 'I am a piece of software'])
        i.add_fact(['City', 'Adelaide', 'Town in South Australia'])
        print(i)
        self.assertTrue(len(str(i)) > 5)
        self.assertEqual(len(i.facts), 3)
        
        
if __name__ == '__main__':
    unittest.main()
