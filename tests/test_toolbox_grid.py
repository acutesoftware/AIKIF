# test_toolbox_gris.py     written by Duncan Murray 17/1/2015
# unit testing for grid class used for games, planning, AI


import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder)
import config as mod_cfg

import toolbox.cls_grid as mod_grid
grd = mod_grid.Grid(grid_height=8, grid_width=8, pieces=['X', 'O'], spacing=1)   
grd.new_tile()
grd.new_tile()

class ToolboxGridTest(unittest.TestCase):

    def test_01_print(self):
        print(grd)
        self.assertEqual(len(str(grd)),73)
    
    def test_02_grid_width(self):
        self.assertEqual(grd.get_grid_width(),8)

    def test_03_grid_height(self):
        self.assertEqual(grd.get_grid_height(),8)

    def test_04_count_blank_cells(self):
        self.assertEqual(grd.count_blank_positions(),62)
        grd.new_tile()
        grd.new_tile()
        self.assertEqual(grd.count_blank_positions(),60)
        for i in range(50):
            grd.new_tile()
        self.assertEqual(grd.count_blank_positions(),10)
        print('\n', grd)
            
if __name__ == '__main__':
    unittest.main()