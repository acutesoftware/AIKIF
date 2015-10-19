# test_toolbox_gris.py     written by Duncan Murray 17/1/2015
# unit testing for grid class used for games, planning, AI


import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder)
import config as mod_cfg

tool_folder = root_folder + os.sep + 'toolbox' 
sys.path.append(tool_folder)
import cls_grid as mod_grid

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
        
            
    def test_05_clear(self):
        grd.clear()
        self.assertTrue(grd.is_empty(1,1))
        self.assertEqual(grd.count_filled_positions(),0)
        self.assertEqual(grd.count_blank_positions(),64)
        grd.new_tile()
        grd.new_tile()
        self.assertEqual(grd.count_blank_positions(),62)
        for i in range(50):
            grd.new_tile()
        self.assertEqual(grd.count_blank_positions(),12)
        print('\n', grd)
        
    def test_06_save_grid(self):
        good_file = 'my_grid.txt'
        crap_file = '/\/\_BAD_FILENAME.txt'
        grd.save(good_file)
        self.assertTrue(os.path.exists(good_file))    
        grd.save(crap_file)
        self.assertFalse(os.path.exists(crap_file))    
        
    def test_07_load_grid(self):
        """  test data includes blank lines which load should ignore """
        test_grid_data = """.XX.
X.X.
....
XXXX

"""
        with open('test_grid.txt', 'w') as f:
            f.write(test_grid_data)
        self.assertTrue(os.path.exists('test_grid.txt'))
        
        # load the grid
        grd.clear()
        grd.load('test_grid.txt')
        
        # grid should have changed from 8x8 to 4x4
        self.assertEqual(grd.get_grid_height(),4)
        self.assertEqual(grd.get_grid_width(),4)
        
        # spot check new values
        self.assertEqual(grd.count_blank_positions(),8)
        self.assertEqual(grd.get_tile(0,0),'.')
        self.assertEqual(grd.get_tile(0,1),'X')
        self.assertEqual(grd.get_tile(0,2),'X')
        self.assertEqual(grd.get_tile(0,3),'.')

        self.assertEqual(grd.get_tile(3,0),'X')
        self.assertEqual(grd.get_tile(3,1),'X')
        self.assertEqual(grd.get_tile(3,2),'X')
        self.assertEqual(grd.get_tile(3,3),'X')
    
    def test_08_set_tile_incorrectly(self):

        grd.clear()
        grd.set_tile(0, 0, 'X')
        self.assertEqual(grd.extract_row(0), ['X', '.', '.', '.'])
        
        grd.clear()
        grd.set_tile(-1, 0, 'X')
        self.assertEqual(grd.extract_row(0), ['X', '.', '.', '.'])
 
        grd.clear()
        grd.set_tile(0, -1, 'X')
        self.assertEqual(grd.extract_row(0), ['X', '.', '.', '.'])

        grd.clear()
        self.assertEqual(grd.get_tile(3,0),'.')
        grd.set_tile(0, 999, 'X')
        self.assertEqual(grd.get_tile(0,3),'X')
        self.assertEqual(grd.extract_row(3), ['.', '.', '.', '.'])
        
 
        grd.clear()
        grd.set_tile(999, 0, 'X')
        self.assertEqual(grd.extract_row(3), ['X', '.', '.', '.'])
 
       
        
        
            
if __name__ == '__main__':
    unittest.main()
