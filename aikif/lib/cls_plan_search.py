# cls_plan_search.py    written by Duncan Murray 10/1/2015

"""
Various algorithms to do searches

"""
import os
import sys
import heapq
lib_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." +  os.sep + "toolbox" )
sys.path.append(lib_folder)
import cls_grid


def TEST():
    # TODO later : environ = cls_grid.Grid(grid_height=8, grid_width=8, pieces=['X', 'O'], spacing=1) 
    environ = [[1,1],[3,3]]  # grid
    goal =  ['1','2','3','4','5','6','7','8','0']
    start = ['2','7','1','3','5','0','6','8','4']
    plan = PlanSearchAStar('8 Puzzle', environ, goal, start)
    plan.search()    
    print(plan)

class Plan(object):
    """ 
    base class 
    """
    def __init__(self, nme, environ,  target, start):
        self.nme = nme
        self.start = start
        self.target = target

    def __str__(self):
        res =  'Plan   : ' + self.nme + '\n'
        res += 'Start  : ' + ', '.join(str(p) for p in self.start) + '\n'
        res += 'Target : ' + ', '.join(str(p) for p in self.target)
        return res
    
class PlanSearchAStar(Plan):    
    """
    Search algorithm using AStar.
    """
    def __init__(self, nme, environ, target, start):
        Plan.__init__(self, nme, environ, target, start)
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.came_from = []

        
    def __str__(self):
        #print(str(Plan))        # Prints <class '__main__.Plan'>
        #print(super(PlanSearchAStar, self).__str__())  # works
        #print(str(Plan.super())
        #return str(super(PlanSearchAStar, self))  # fails - returns <super: <class 'PlanSearchAStar'>, <PlanSearchAStar object>>
        #return 'Method : A*\n' + super(PlanSearchAStar, self).__str__()  # works, but only if Plan class NOT inherited from object
        return 'Method : A*\n' + str(Plan.__str__(self))  # works, but clunky
    
    def heuristic_cost(self, start, target):
        (x1, y1) = start
        (x2, y2) = target
        return abs(x1 - x2) + abs(y1 - y2)

    def get_min_f_score(self):
        return 1
        
    def search(self):
        print('searching...')

    
if __name__ == '__main__':
    TEST()	
    