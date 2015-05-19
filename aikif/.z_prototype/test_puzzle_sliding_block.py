# test_puzzle_sliding_block.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "examples")
sys.path.append(lib_fldr)
import puzzle_sliding_block as mod_puz

class PlanPuzzleSlidingBlock(unittest.TestCase):
    
    def test_01_print_puzzle(self):
        puz = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
        self.assertEqual(str(puz), '[[1, 0, 2] [3, 4, 5] [6, 7, 8] ]' )
        
    def test_02_legal_moves_a(self):
        puz = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
        self.assertEqual(puz.legal_moves(),['down', 'left', 'right'] )
        
    def test_03_legal_moves_b(self):
        puz = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
        puz2 = puz.result('right')
        self.assertEqual(puz2.legal_moves(),['down', 'left'] )
        
    def test_03_legal_moves_c(self):
        puz = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
         
        puz3 = puz.result('down')
        self.assertEqual(puz3.legal_moves(),['up', 'down', 'left', 'right'] )
        
 #   print("Legal Moves after moving down  = ", puz.result('down').legal_moves())
  #  print("Legal Moves after moving down  = ", puz.result('down').legal_moves())


        
if __name__ == '__main__':
    unittest.main()