# test_plan_search.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "lib")
sys.path.append(lib_fldr)
import cls_plan_search as mod_plan

goal =  [1,2,3,4,5,6,7,8,0]
start = [1,2,3,4,5,6,7,0,8]

class PlanSearchTest(unittest.TestCase):
    
    def setUp(self):
        """ Note, this gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.myplan = mod_plan.Plan('8 Puzzle', [], goal, start)
        

    """ 
    tests for plans go below - use myplan instantiated object
    """
    def test_01_new_plan(self):
        self.assertEqual(self.myplan.nme, '8 Puzzle')

    def test_02_check_none_method(self):
        self.assertEqual(self.myplan.nme, '8 Puzzle')
        self.assertEqual(self.myplan.method, 'No method defined')
 
    def test_03_astar_new(self):
        myplan2 = mod_plan.PlanSearchAStar('8 Puzzle', [], goal, start)
        self.assertEqual(myplan2.method, 'A*')
 
    def test_10_util_BFS(self):
        graph = {
                'A': ['B', 'E'],
                'B': ['H', 'C', 'D'],
                'E': ['M'],
                'H': ['J', 'M', 'F'],
                'F': [ 'I'],
                'M': [ 'J'],
                'J': ['Z']
                 }
        self.assertEqual(mod_plan.find_path_BFS(graph, 'A', 'B'), ['A', 'B'])
        self.assertEqual(mod_plan.find_path_BFS(graph, 'A', 'F'), ['A', 'B', 'H', 'F'])
        self.assertEqual(mod_plan.find_path_BFS(graph, 'B', 'H'), ['B', 'H'])
        self.assertEqual(mod_plan.find_path_BFS(graph, 'E', 'J'), ['E', 'M', 'J'])


    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        print(str(self.myplan))
        pass
    
if __name__ == '__main__':
    unittest.main()