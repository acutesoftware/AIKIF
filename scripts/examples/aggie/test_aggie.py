#!/usr/bin/python3
# coding: utf-8
# test_bias.py

import unittest
import sys
import os

import aggie 

class TestAggie(unittest.TestCase):
    def test_00_aggie_version(self):
        """ 
        make sure we are testing the same version 
        """
        self.assertEqual(aggie.aggie_version, '0.0.2')

    def test_01_hard_coded_answers(self):
        """
        hard coded test - will be removed once skills implemented
        """
        a = aggie.Aggie()
        self.assertEqual(a.process_input('when is my dentist appointment?'),'next week')
        self.assertEqual(a.process_input('this is a contrived example'),'Adding info..')
        self.assertEqual(a.process_input('what is the weather in Spain?'),'sunny')
        self.assertEqual(a.process_input('where is the best picnic spot nearby?'),'4km to the North')

        
    def test_02_load_skills(self):
        """
        check that adding skills works
        """
        s = aggie.Skills()
        s.add_skill(['Get Weather', 'return weather for [City]'])
        self.assertTrue(len(str(s)) > 5)
        self.assertEqual(len(s.skills), 1)
        
    def test_03_load_info(self):
        """
        count of facts added via add_fact
        """
        i = aggie.Info()
        i.add_fact(['[Me]', 'Name', 'My name is Aggie'])
        i.add_fact(['[Me]', 'What', 'I am a piece of software'])
        i.add_fact(['City', 'Adelaide', 'Town in South Australia'])
        self.assertTrue(len(str(i)) > 5)
        self.assertEqual(len(i.facts), 3)
        
         
    def test_05_add_info(self):
        """
        make sure raw_input list gets updated via process_input
        """
        h = aggie.Aggie()
        h.process_input('France is a country')
        h.process_input('Red is a colour')
        self.assertTrue(h.info.raw_input, ['France is a country', 'Red is a colour'])

    def test_06_find_answer(self):
        """
        test for answers via skills
        """
        h = aggie.Aggie()
        self.assertEqual(h.info.find_answer('when'), 'next week')
        
        
        
        
if __name__ == '__main__':
    unittest.main()
