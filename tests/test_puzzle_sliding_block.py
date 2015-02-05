# test_puzzle_sliding_block.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "examples")
sys.path.append(lib_fldr)
import puzzle_sliding_block as mod_puz

goal =  [1,2,3,4,5,6,7,8,0]
start = [1,2,3,4,5,6,7,0,8]

class PlanPuzzleSlidingBlock(unittest.TestCase):
    
    def test_01_print_puzzle(self):
        puz = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
        self.assertEqual(str(puz), '[[1, 0, 2] [3, 4, 5] [6, 7, 8] ]' )
        
    def test_02_legal_moves_a(self):
        puz = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
        self.assertEqual(puz.legal_moves(),['down', 'left', 'right'] )
        
    
if __name__ == '__main__':
    unittest.main()