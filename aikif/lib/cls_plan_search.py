# cls_plan_search.py    written by Duncan Murray 10/1/2015

"""
Various algorithms to do searches
"""

import os
import sys
import heapq
import queue
PriorityQueue = queue.PriorityQueue
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
lib_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." +  os.sep + "toolbox" )
sys.path.append(lib_folder)
sys.path.append(root_folder)
import cls_grid
import data_structures as ds
import config as mod_cfg
import cls_log as mod_log

def TEST():
    # TODO later : environ = cls_grid.Grid(grid_height=8, grid_width=8, pieces=['X', 'O'], spacing=1) 
    environ = [[1,1],[3,3]]  # grid
    goal =  [1,2,3,4,5,6,7,8,0]
    start = [1,3,5,6,8,4,2,7,0] # hard
    start = [1,2,3,4,5,6,7,0,8] # easy
   # start =  [1,2,3,4,5,6,7,8,0]
    plan = PlanSearchAStar('8 Puzzle', environ, goal, start)
    print(plan)
    plan.search()    
    my_prob = Problem([1,2,3,4],[3,2,1,4], ['L:-1','R:+1'], 'test1', 'test of problem')
    print(my_prob)
    print('Goal test should pass with [1,2,3,4]: ', my_prob.goal_test([1,2,3,4]))
    print('Goal test should fail with [3,2,1,4]: ', my_prob.goal_test([3,2,1,4]))
    print('Goal test should fail with "BLAH": ', my_prob.goal_test('BLAH'))
    print('Goal test should fail with 3.14159265359: ', my_prob.goal_test(3.14159265359))
    
class Problem(object):
    """
    Defines the planning problem. Must contain:
    - goal state
    - start state
    - set of actions with outcomes
    - path cost function
    """
    def __init__(self, goal, start, actions, name, description):
        """
        The Search Problem is defined by an initial state, a successor function,
        and a goal state.  In lieu of a path cost function, a default one is
        provided that depends on the depth of the node in the tree.
        """
        self.name = name
        self.description = description
        self.actions = actions
        self.start = start
        self.goal = goal
        
    
    def __str__(self):
        res = ' --- Problem Definition ---' '\n'
        res += 'Problem Name : ' + self.name + '\n'
        res += 'Description  : ' + self.description + '\n'
        res += 'Start State  : ' + list_2_str(self.start) + '\n'
        res += 'Goal State   : ' + list_2_str(self.goal) + '\n'
        res += 'Actions List : ' + '\n'
        if self.actions:
            for num, action in enumerate(self.actions):
                res += '          ' + str(num+1).zfill(2) + ' : ' +  action + '\n'
        else:
            res += 'No actions specified\n'
        return res
    
    def path_cost(self):
        """
        return the cost of the function - this needs to be subclassed
        """
        return 1
        
    def goal_test(self, state_to_check):
        """
        Checks for success
        """
        if type(state_to_check) != type(self.goal):
            return False
            
        if state_to_check == self.goal:
            return True
        else:
            return False
 
    def get_successors(self):
        """
        expand the children on the node (or successors)
        to get the list of next nodes and their cost, 
        [[x1, 50], [x2, 24], [x3,545], [x5,32.1]]
        """
        return [[x1, 50], [x2, 24], [x3,545], [x5,32.1]]
        
    
class Plan(object):
    """ 
    base class for AI planners to implement standard logging
    """
    def __init__(self, nme, environ,  target, start):
        self.nme = nme
        self.start = start
        self.target = target
        self.method = 'No method defined'
        self.lg = mod_log.Log(mod_cfg.fldrs['log_folder']) #'T:\\user\\AIKIF')
        self.lg.record_command('CLS_PLAN_SEARCH - starting Plan', nme)


    def __str__(self):
        res =  'Plan   : ' + self.nme + '\n'
        res += 'Method : ' + self.method + '\n'
        res += 'Start  : ' + ', '.join(str(p) for p in self.start) + '\n'
        res += 'Target : ' + ', '.join(str(p) for p in self.target) + '\n'
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
        self.current = start
        self.method = 'A*'
        self.num_loops = 0
        self.lg.record_source(','.join(str(p) for p in self.start),  'CLS_PLAN_SEARCH : Source = ')
        self.lg.record_source(','.join(str(p) for p in self.target), 'CLS_PLAN_SEARCH : Target = ')

    def heuristic_cost(self, start, target):
        """ assumes start and target are an (x,y) grid """
        (x1, y1) = start
        (x2, y2) = target
        return abs(x1 - x2) + abs(y1 - y2)

    def get_min_f_score(self):
        return 1
        
    def search(self):
        print('searching...')
        self.lg.record_process('CLS_PLAN_SEARCH', 'running A* search')

        if self.target == self.current:
            print('starting point is target')
            self.lg.record_result('CLS_PLAN_SEARCH', 'Success - start == Target')
            return 0
        
        while self.opened:
            self.num_loops += 1

        self.lg.record_command('CLS_PLAN_SEARCH - Finished Plan', self.nme)

        
"""-----------------------------
Utilities and Search Algorithms 
(used by examples/ folder)

"""   

def list_2_str(lst): 
    return ', '.join(str(i) for i in lst) 

def find_path_BFS(Graph,n,m):
    """
    Breadth first search
    """
    if m not in Graph:
        return None
    if n == m:
        return [m]
    path = [[n]]
    searched = []
    while True:
        j = len(path)
        k = len(Graph[n])
        for i in range(j):
            node = path[i][-1]
            for neighbor in Graph[node]:
                if neighbor not in searched:                    
                    path.append(path[i]+[neighbor])  
                    searched.append(neighbor)
                    if neighbor==m:
                        return path[-1]
        for i in range(j):
            path.pop(0)
    return path



    
if __name__ == '__main__':
    TEST()	
    