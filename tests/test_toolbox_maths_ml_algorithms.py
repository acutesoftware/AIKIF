# test_toolbox_maths_ml_algorithms.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif"  )
sys.path.append(root_fldr)
import toolbox.maths_ml_algorithms as ml

class LogTest(unittest.TestCase):

    def test_01_entropy(self):
        self.assertEquals(ml.ml_entropy([3,3]), 1)
        self.assertEquals(ml.ml_entropy([2,0]), 0)
        self.assertEquals(ml.ml_entropy([1,3]), 0.811278)
        self.assertEquals(ml.ml_entropy([16,0,0,0,0,0,0,0,0]), 0)
        self.assertEquals(ml.ml_entropy([546,314]), 0.946848)
        self.assertEquals(ml.ml_entropy([184,11]), 0.313027)
        self.assertEquals(ml.ml_entropy([100,50]), 0.918296)
        self.assertEquals(ml.ml_entropy([80,15]), 0.629249)
        self.assertEquals(ml.ml_entropy([20,35]), 0.94566)

      
if __name__ == '__main__':
    unittest.main()