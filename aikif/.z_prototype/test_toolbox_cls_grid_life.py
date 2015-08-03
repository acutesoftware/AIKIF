#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_cls_grid_life.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
toolbox_path = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
example_path = root_folder + os.sep + 'aikif' + os.sep + 'examples' 
sys.path.append(toolbox_path)
sys.path.append(example_path)

import cls_grid_life
import game_of_life_console as gol

class TestToolboxClsGridLife(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        gol.main()
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
