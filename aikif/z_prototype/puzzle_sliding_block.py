# puzzle_sliding_block.py   written by Duncan Murray  10/1/2015

"""

8 block puzzle
===============
Goal State (multiples, eg 123 456 78
- 1 2
3 4 5
6 7 8

8 tiles, numbered 1 to 8
inital state is random configuration

Actions
- move a tile next to an empty space, INTO the empty space

Path Cost - all actions have equal cost

Notes and comments from forums
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


Define the problem as a states-graph: 
G=(V,E) where V=S={(x_1,x_2,...,x_9) | all possible states the board can be in} [each number is representing a single 'square' on the board]. 
and define E={(v1,v2)| it is possible to move from state v1 to state v2 with a single step} an alternative definition [identical] for E is by using the function successors(v): 
For each v in V: successors(v)={all possible boards you can get, with 1 step from v}

You will also need an admissible heuristic function, a pretty good one for this problem can be: h(state)=Sigma(manhattan_distance(x_i)) where i in range [1,9]) basically, it is the summation of manhattan distances for each number from its target.

Now, once we got this data, we can start running A* on the defined graph G, with the defined heuristic. And since our heuristic function is admissible [convince yourself why!], it is guaranteed that the solution A* finds will be optimal, due to admissibility and optimality of A*. 
Finding the actual path: A* will end when you develop the target state. [x_i=i in the terms we used earlier]. You will find your path to it by stepping back from the target to the source, using the parent field in each node.

"""

import os
import sys
import math
import heapq
import queue
PriorityQueue = queue.PriorityQueue

toolbox_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." +  os.sep + "toolbox" )
lib_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." +  os.sep + "lib" )
sys.path.append(lib_folder)
sys.path.append(toolbox_folder)

import cls_plan_search as mod_search
import data_structures as ds

def main():
    start_state = [1, 0, 2, 3, 5, 4, 6, 7, 8]
  #  start_state = [1, 5, 0, 2, 3, 8, 4, 6, 7]
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    puz = TilePuzzle(start_state, goal_state, 3, 3)

    """
    print('Heuristic = ', puz.heuristic(), 'Legal Moves = ', puz.legal_moves() )

    puz = puz.result('down')
    print('Heuristic = ', puz.heuristic(), 'Moved down  = ', puz.legal_moves() )
   
    puz = puz.result('right')
    print( 'Heuristic = ', puz.heuristic(), 'Moved right  = ', puz.legal_moves())
 
    puz = puz.result('down')
    print('Heuristic = ', puz.heuristic(), 'Moved down  = ', puz.legal_moves())
    """
    print(puz)
    
    
    result = puz.solve()
    print(result)
    
class TilePuzzle:
    """
    main class for tile puzzle 
    """
    def __init__( self, start_state, goal_state, rows=3, cols=3 ):
        """
        initialise the tile puzzle state
        """
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.start_state = start_state[:] # Make a copy to stop side-effects.
        self.goal_state = goal_state[:]
        start_state.reverse()
        for row in range( rows ):
            self.cells.append( [] )
            for col in range( cols ):
                self.cells[row].append( start_state.pop() )
                if self.cells[row][col] == 0:
                    self.blank_location = row, col

    def __str__(self):
    
        res = '['
        for cell in self.cells:
            res += str(cell) + ' ' 
        return res + ']'
    
    def current_state_as_grid(self):
        """ return the current state """
        res = []
        for cell in self.cells:
            res.append(cell)
        return res
    
    def current_state_as_list(self):
        """ return the current state """
        res = []
        for row in self.cells:
            for cell in row:
                res.append(cell)
        return res

    def legal_moves( self ):
        """
        Returns a list of legal moves from the current state.

        You can (at most, if not at edge) move the blank space 
        up, down, left or right.
        """
        moves = []
        row, col = self.blank_location
        if(row != 0):
            moves.append('up')
        if(row != 2):
            moves.append('down')
        if(col != 0):
            moves.append('left')
        if(col != 2):
            moves.append('right')
        return moves

    def result(self, move):
        """
        Returns a new eightPuzzle with the current state and blankLocation
        updated based on the provided move.

        The move should be a string drawn from a list returned by legalMoves.
        Illegal moves will raise an exception, which may be an array bounds
        exception.

        NOTE: This function *does not* change the current object.  Instead,
        it returns a new object.
        """
        row, col = self.blank_location
        if(move == 'up'):
            newrow = row - 1
            newcol = col
        elif(move == 'down'):
            newrow = row + 1
            newcol = col
        elif(move == 'left'):
            newrow = row
            newcol = col - 1
        elif(move == 'right'):
            newrow = row
            newcol = col + 1
        else:
            raise "Illegal Move"

        # Create a copy of the current eightPuzzle
        new_puzzle = TilePuzzle([0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0])
        new_puzzle.cells = [values[:] for values in self.cells]
        # And update it to reflect the move
        new_puzzle.cells[row][col] = self.cells[newrow][newcol]
        new_puzzle.cells[newrow][newcol] = self.cells[row][col]
        new_puzzle.blank_location = newrow, newcol
        return new_puzzle
        

    def heuristic(self):
        """ heuristic for 8 tile puzzle        |-----------|
            h1: number of misplaced tiles      | 7 | 2 | 4 | 
            h2: Manhattan block distance       |---|---|---|
            – example:                         | 5 |   | 6 |
            • h1 = 8                           |---|---|---| 
                    all 8 tiles are misplaced  | 8 | 3 | 1 |
            • h2 = 3+1+2+2+2+3+3+2 = 18        |-----------|
            
        curr_state = list of tiles (integers)
        target_state = goal tiles
        
        """
        h = 0
        cur_state = self.current_state_as_list()
        print('cur_state = ', cur_state)
        
        if len(cur_state) == 0:
            print('error - blank self.cells')
            return 0
        n = math.sqrt(len(cur_state))
        for i, tile in enumerate(cur_state):
            if tile > 0:
                h += int(abs(tile - 1 - i) / n) + (abs(tile - 1 - i) % n)
        return h

        
    def solve(self):
        """ 
        main function to solve the tile puzzle
        Notes on algorithm from AI planning course slides below:
            function aStarTreeSearch(problem, h)
            fringe <- priorityQueue(new searchNode(problem.initialState))
            allNodes <- hashTable(fringe)
            while (1)
                if empty(fringe) then return failure
                node <- selectFrom(fringe)
                if problem.goalTest(node.state) then
                    return pathTo(node)
                for successor in expand(problem, node)
                    if not allNodes.contains(successor) then
                        fringe <- fringe + successor @ f(successor)
                        allNodes.add(successor)
        
        """
        path = []
        visited = []
        if self.start_state == self.goal_state:
            path.append(self.goal_state)
            return path
        fringe = PriorityQueue(self.start_state)
        while fringe:
            cur_node = self.select_from(fringe)
            print(cur_node)
            if node == self.goal_state:
                print('SUCCESS!')
                path.append(self.goal_state)
                return path
            for successor in self.expand(node):
                if successor not in visited:
                    fringe.append(successor)
                    visited.append(successor)
        
        
        
        return []    # failed to find a path
        
        
        print('todo')

        
    def select_from(self, nodes):
        """ part of Astar - get the next node """
        return nodes.get()
    
    def expand(self, node):
        """ 
        part of Astar - expand the list of linked nodes in node
        """
        nodes = []
        print('expand : ')
        (x,y) = self.cur_node[row][col]
        moves = self.legal_moves()
        print('x,y  = ' , (x,y))
        for m in moves:
            if m == 'left':
                nodes.append(self.cells[x-1][y])
            if m == 'right':
                nodes.append(self.cells[x+1][y])
            if m == 'up':
                nodes.append(self.cells[x][y-1])
            if m == 'down':
                nodes.append(self.cells[x][y+1])
            
        return nodes
    
if __name__ == '__main__':
    main()
