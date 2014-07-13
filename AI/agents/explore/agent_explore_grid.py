# agent_explore_grid.py		written by Duncan Murray	9/7/2014


import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "..") 
sys.path.append(root_folder)
print(root_folder)
import AI.agents.agent as agt

		

class ExploreAgent(agt.Agent):
    """
    agent that explores a world (2D grid)
    """
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        #agt.Agent.__init__(self, *arg)
        agt.Agent.__init__(self, name,  fldr, running)
        self.LOG_LEVEL = LOG_LEVEL
        self.num_steps = 0
        
    def set_world(self, grd, start_y, start_x, y, x):
        """
        tell the agent to move to location y,x 
        Why is there another grd object in the agent? Because 
        this is NOT the main grid, rather a copy for the agent
        to overwrite with planning routes, etc.
        The real grid is initialised in World.__init__() class
        """
        self.grd = grd
        self.start_x = start_x
        self.start_y = start_y
        self.current_x = start_x
        self.current_y = start_y
        self.target_x = x
        self.target_y = y

        
    def do_your_job(self, *arg):
        """
        the goal of the explore agent is to move to the 
        target while avoiding blockages on the grid
        """
        direction = ''
            
        y,x = self.get_intended_direction()  # first find out where we should go
        if self.target_x == self.current_x and self.target_y == self.current_y:
            print(self.name + " : TARGET ACQUIRED")
            self.lg_mv(2, self.name + ": TARGET ACQUIRED" )
                    
            return
        
        self.num_steps += 1   
        
        # first try is to move on the x axis in a simple greedy search
        accessible = ['\\', '-', '|', '/', '.']
        blocked = '#'
        if x != 0:
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

        # if movement was not successful or needed along x, then try y
        if y != 0:
            if y == 1:
                if self.grd.get_tile(self.current_y + 1, self.current_x) in accessible:
                    self.current_y += 1
                    self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - moving South" )
                    return
            elif y == -1:
                if self.grd.get_tile(self.current_y - 1, self.current_x) in accessible:
                    self.current_y -= 1
                    self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - moving North")
                    return

        # damn - we are still here, so there are no simple paths in both directions
        # Repeat by going over mountains (takes double time)
        if x != 0:
            if x == 1:
                if self.grd.get_tile(self.current_y, self.current_x + 1) not in blocked:
                    self.current_x += 1
                    self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - climbing West" )
                    return
                else:
                    self.lg_mv(4, "The way East is shut")
            elif x == -1:
                if self.grd.get_tile(self.current_y, self.current_x - 1) not in blocked:
                    self.current_x -= 1
                    self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - climbing East" )
                    return
                else:
                    self.lg_mv(4, "The way West is shut")
        # if movement was not successful or needed along x, then try y
        if y != 0:
            if y == 1:
                if self.grd.get_tile(self.current_y + 1, self.current_x) not in blocked:
                    self.current_y += 1
                    self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - climbing South" )
                    return
                else:
                    self.lg_mv(4, "The way South is shut")
            elif y == -1:
                if self.grd.get_tile(self.current_y - 1, self.current_x) not in blocked:
                    self.current_y -= 1
                    self.lg_mv(3, self.name + ": move# " + str(self.num_steps) + " - climbing North")
                    return
                else:
                    self.lg_mv(4, "The way North is shut")        
        
        
        
        self.lg_mv(4, "damn - blocked in both directions - need to backtrack (TODO)")
        # damn - we are still here, so there are no simple paths in both directions
        # Repeat by going over mountains (takes double time)
        
        
        self.grd.set_tile(self.start_y, self.start_x, 'A')
        self.grd.save('agent.txt')

        
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
        print("Agent Status:")
        print("start_x  = ", self.start_x)
        print("start_y  = ", self.start_y)
        print("target_x = ", self.target_x)
        print("target_y = ", self.target_y)
       
        
        print(self.grd)
    
def main():
	agt = ExploreAgent('exploring_agent',  'T:\\user\\AIKIF', True)
	print(agt.report())

 		
		
if __name__ == '__main__':
	main()
	
	