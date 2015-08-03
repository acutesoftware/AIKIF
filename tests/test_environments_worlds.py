#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_environments_worlds.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'environments' 

sys.path.append(pth)

import worlds
import world_generator

class TestToolboxClsGridLife(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_run_all(self):
        pass
        world_generator.main()
        self.assertEqual(os.path.exists(os.getcwd() + os.sep + 'test_world_traversed.txt'), True)
        self.assertEqual(os.path.exists(os.getcwd() + os.sep + 'test_world.txt'), True)

    def test_02_world_init(self):
        
        num_seeds   =   6   # number of seed points to start land generation
        perc_land   =  20   # % of world that is land
        perc_sea    =  80   # % of world that is sea
        perc_blocked=   4   # % of world that is blocked
        
        myWorld = worlds.World( 22, 44, ['O','P','@'])  # TODO - fix passing
        self.assertEqual(str(myWorld.grd)[0:44], '............................................')
        self.assertEqual('.' in str(myWorld.grd), True)
        self.assertEqual('X' in str(myWorld.grd), False)  # should be all blank before we build 
        self.assertEqual('#' in str(myWorld.grd), False)  # the world using build random
        
        myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
        #print(myWorld.grd)
        self.assertEqual(myWorld.grd.get_grid_width(), 44)
        self.assertEqual(myWorld.grd.get_grid_height(), 22)
        
        self.assertEqual('.' in str(myWorld.grd), True)
        self.assertEqual('X' in str(myWorld.grd), True)
        self.assertEqual('#' in str(myWorld.grd), True)
               
if __name__ == '__main__':
    unittest.main()
