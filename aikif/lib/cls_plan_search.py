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
    plan.search()    
    print(plan)
    
    g = Graph({'1': ['2','3','4'], '2':['6','7']})
    print('raw graph = ', g)
    mat = g.get_adjacency_matrix(True)
    
    
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
    """    
    def __str__(self):
        #print(str(Plan))        # Prints <class '__main__.Plan'>
        #print(super(PlanSearchAStar, self).__str__())  # works
        #print(str(Plan.super())
        #return str(super(PlanSearchAStar, self))  # fails - returns <super: <class 'PlanSearchAStar'>, <PlanSearchAStar object>>
        #return 'Method : A*\n' + super(PlanSearchAStar, self).__str__()  # works, but only if Plan class NOT inherited from object
        return 'Method : ' + self.method + '\n' + str(Plan.__str__(self))  # works, but clunky
    """
    def heuristic_cost(self, start, target):
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

        
        
"""------------------------
Classes for Data Structures
"""   
 
class Graph(object):
    def __init__(self, graph):
        """ takes a graph as input 
        e.g. the following tree is encoded as follows:
        
                 A 
               /   \ 
              B     E 
            / | \    \
           H  C  D    M
        
        would be entered as 
        { 'A': ['B', 'E'],
          'B': ['H', 'C', 'D'],
          'E': ['M']  }
        """
        self.graph = graph
        self.nodes = []
        self.links = []
        self.adj_matrix = []

    def __str__(self):
        """ display as raw data """
        return str(self.graph)
        
    def get_adjacency_matrix(self, show_in_console=False):
        """ return the matrix as a list of lists 
        raw graph =  {'1': ['2', '3', '4'], '2': ['6', '7']}
        6 nodes: ['1', '2', '3', '4', '6', '7']
        5 links: [['1', '2'], ['1', '3'], ['1', '4'], ['2', '6'], ['2', '7']]
        [0, 1, 1, 1, 0, 0]
        [1, 0, 0, 0, 1, 1]
        [1, 0, 0, 0, 0, 0]
        [1, 0, 0, 0, 0, 0]
        [0, 1, 0, 0, 0, 0]
        [0, 1, 0, 0, 0, 0]
        """
        self.links = [[i,j] for i in self.graph for j in self.graph[i]]
        all_nodes = []
        op = [] # 0 for i in self.graph for j in self.graph[i]]
        for node in self.graph:
            all_nodes.append(node)  # to get the root node
            for connection in self.graph[node]:
                all_nodes.append(connection)
        self.nodes = sorted(list(set(all_nodes)))
        if show_in_console != False:
            print (len(self.nodes), 'nodes:', self.nodes)
            print (len(self.links), 'links:', self.links)
        
        for y in range(len(self.nodes)):
            row = []
            for x in range(len(self.nodes)):
                match = False
                for l in self.links:
                    if self.nodes[x] == l[0] and self.nodes[y] == l[1]:
                        match = True
                    if self.nodes[x] == l[1] and self.nodes[y] == l[0]:
                        match = True
                        
                if match == True:
                    row.append(1)
                else:
                    row.append(0)
                
            op.append(row)
            
        if show_in_console != False:
            for row in op:
                print(row)
            
        return op
        
"""-----------------------------
Utilities and Search Algorithms 
(used by examples/ folder)

"""   

    

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
    