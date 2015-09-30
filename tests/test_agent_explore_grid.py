#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_agent_explore_grid.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'agents' + os.sep + 'explore' 

sys.path.append(pth)


import agent_explore_grid as mod_agt
agt = mod_agt.ExploreAgent('TEST - exploring_agent',  os.getcwd(), 1, True)
agt.set_world( [], [3,4], [6,6])
class TestToolboxClsGridLife(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        print(agt.report())
        self.assertEqual(1,1)

    def test_02_show_status(self):
        agt.show_status()
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
