# test_puzzle_sliding_block.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "examples")
sys.path.append(lib_fldr)
import puzzle_sliding_block as mod_puz

puz_start = [1, 0, 2, 3, 4, 5, 6, 7, 8]
puz_goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
class PlanPuzzleSlidingBlock(unittest.TestCase):
    
    def test_01_print_puzzle(self):
        puz1 = mod_puz.TilePuzzle(puz_start, puz_goal, 3, 3)
        self.assertEqual(str(puz1), '[[1, 0, 2] [3, 4, 5] [6, 7, 8] ]' )
        
    def test_02_legal_moves_a(self):
        puz2 = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
        self.assertEqual(puz2.legal_moves(),['down', 'left', 'right'] )
        print('TODO - the passed parameter gets modified - fix this if you ever use this code')
        
    #def test_03_legal_moves_b(self):
    #    puz3 = mod_puz.TilePuzzle(puz_start, puz_goal, 3, 3)
    #    puz3_res = puz3.result('right')
    #    self.assertEqual(puz3_res.legal_moves(),['down', 'left'] )
        
    #def test_04_legal_moves_c(self):
    #    puz4 = mod_puz.TilePuzzle([1, 0, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 3)
    #     
    #    puz4_res = puz4.result('down')
    #    self.assertEqual(puz4_res.legal_moves(),['up', 'down', 'left', 'right'] )
        
 #   print("Legal Moves after moving down  = ", puz.result('down').legal_moves())
  #  print("Legal Moves after moving down  = ", puz.result('down').legal_moves())


        
if __name__ == '__main__':
    unittest.main()