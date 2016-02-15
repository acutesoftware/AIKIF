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

tool_folder = os.path.join(root_folder, 'aikif', 'toolbox')
sys.path.append(tool_folder)
import cls_grid as mod_grid
grd = mod_grid.Grid(grid_height=8, grid_width=8, pieces=['X', 'O'], spacing=1)   
grd.new_tile()
grd.new_tile()

agt.set_world( grd, [3,4], [6,6])
#agt.do_your_job()





       #    start_y, start_x = myWorld.grd.find_safe_starting_point()
            
#    ag.set_world(myWorld.grd, [start_y, start_x], [target_coords[0], target_coords[1]])
 



class TestAgentExploreGrid(unittest.TestCase):

    def test_01_instantiate_agent(self):
         self.assertEqual(agt.start_y, 3)
         self.assertEqual(agt.start_x, 4)
         self.assertEqual(agt.target_y, 6)
         self.assertEqual(agt.target_x, 6)
         self.assertEqual(agt.current_y, 3)
         self.assertEqual(agt.current_x, 4)


    def test_02_show_status(self):
        txt = agt.show_status()
        self.assertEqual(len(txt), 94)
        self.assertEqual(txt[0:14], 'Agent Status:\n')
        
    def test_03_report(self):
        res = agt.report()
        self.assertEqual(res,[])  # results should be empty list at start

    def test_04_do_your_job(self):
        txt_before = agt.show_status()
        for i in range(0,100):
            agt.do_your_job()
        txt_after = agt.show_status()
        self.assertFalse(agt.current_y == 3)  # we *assume* it manages to move
        self.assertFalse(agt.current_x == 4)

        
        #print(agt.grd)
        
    def test_08_clear_surroundings(self):
        #agt.show_status()
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
