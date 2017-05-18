# agent_explore_grid.py     written by Duncan Murray    9/7/2014


import os
import sys
import random
agent_root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(agent_root_folder)

import agent as agt


class ExploreAgent(agt.Agent):
    """
    agent that explores a world (2D grid)
    """
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        #agt.Agent.__init__(self, *arg)
        agt.Agent.__init__(self, name,  fldr, running)
        self.LOG_LEVEL = LOG_LEVEL
        self.num_steps = 0
        self.num_climbs = 0
        
    def set_world(self, grd, start_y_x, y_x):
        """
        tell the agent to move to location y,x 
        Why is there another grd object in the agent? Because 
        this is NOT the main grid, rather a copy for the agent
        to overwrite with planning routes, etc.
        The real grid is initialised in World.__init__() class
        """
        self.grd = grd
        self.start_y = start_y_x[0]
        self.start_x = start_y_x[1]
        self.current_y = start_y_x[0]
        self.current_x = start_y_x[1]
        self.target_y = y_x[0]
        self.target_x = y_x[1]
        self.backtrack = [0,0]   # set only if blocked and agent needs to go back
        self.prefer_x = 0        # set only if backtracked as preferred direction x
        self.prefer_y = 0        # set only if backtracked as preferred direction y
        
    def do_your_job(self):
        """
        the goal of the explore agent is to move to the 
        target while avoiding blockages on the grid.
        This function is messy and needs to be looked at.
        It currently has a bug in that the backtrack oscillates
        so need a new method of doing this - probably checking if
        previously backtracked in that direction for those coords, ie
        keep track of cells visited and number of times visited?
        """
        y,x = self.get_intended_direction()  # first find out where we should go
        if self.target_x == self.current_x and self.target_y == self.current_y:
            #print(self.name + " : TARGET ACQUIRED")
            if len(self.results) == 0:
                self.results.append("TARGET ACQUIRED")
                self.lg_mv(2, self.name + ": TARGET ACQUIRED" )
            
            return
        
        self.num_steps += 1   
        # first try is to move on the x axis in a simple greedy search
        accessible = ['\\', '-', '|', '/', '.']
        
        # randomly move in Y direction instead of X if all paths clear
        if y != 0 and x != 0 and self.backtrack == [0,0]:
            if random.randint(1,10) > 6:
                if self.grd.get_tile(self.current_y + y, self.current_x) in accessible:
                    self.current_y += y
                    self.lg_mv(3, self.name + ": randomly moving Y axis " + str(self.num_steps)  )
                    return
        if x == 1:
            if self.grd.get_tile(self.current_y, self.current_x + 1) in accessible:
                self.current_x += 1
                self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - moving West" )
                return
        elif x == -1:
            if self.grd.get_tile(self.current_y, self.current_x - 1) in accessible:
                self.current_x -= 1
                self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - moving East" )
                return
        elif y == 1:
            if self.grd.get_tile(self.current_y + 1, self.current_x) in accessible:
                self.current_y += 1
                self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - moving South" )
                return
        elif y == -1:
            if self.grd.get_tile(self.current_y - 1, self.current_x) in accessible:
                self.current_y -= 1
                self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - moving North")
                return
        
        self.grd.set_tile(self.start_y, self.start_x, 'A')
        self.grd.save(os.path.join(os.getcwd(), 'agent.txt'))
        

    def lg_mv(self, log_lvl, txt):
        """
        wrapper for debugging print and log methods
        """
        if log_lvl <= self.LOG_LEVEL:
            print(txt + str(self.current_y) + "," + str(self.current_x))
        
    def get_intended_direction(self):
        """
        returns a Y,X value showing which direction the
        agent should move in order to get to the target
        """
        x = 0
        y = 0
        if self.target_x == self.current_x and self.target_y == self.current_y:
            return y,x  # target already acquired
        if self.target_y > self.current_y:
            y = 1
        elif self.target_y < self.current_y:
            y = -1
        if self.target_x > self.current_x:
            x = 1
        elif self.target_x < self.current_x:
            x = -1
        return y,x
        
        
    def clear_surroundings(self):
        """
        clears the cells immediately around the grid of the agent
        (just to make it find to see on the screen)
        """
        cells_to_clear = self.grd.eight_neighbors(self.current_y, self.current_x)
        for cell in cells_to_clear:
            self.grd.set_tile(cell[0], cell[1], ' ')
            

    def show_status(self):
        """
        dumps the status of the agent
        """
        txt = 'Agent Status:\n'
        print(txt)
        txt += "start_x  = " + str(self.start_x) + "\n"
        txt += "start_y  = " + str(self.start_y) + "\n"
        txt += "target_x = " + str(self.target_x) + "\n"
        txt += "target_y = " + str(self.target_y) + "\n"
        txt += "current_x = " + str(self.current_x) + "\n"
        txt += "current_y = " + str(self.current_y) + "\n"
       
        
        print(self.grd)
        return txt
