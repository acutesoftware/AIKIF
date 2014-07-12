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
    def __init__(self, *arg):
        agt.Agent.__init__(self, *arg)

    def set_world(self, grd, start_x, start_y, y, x):
        """
        tell the agent to move to location y,x 
        """
        self.grd = grd
        self.start_x = start_x
        self.start_y = start_y
        self.current_x = start_x
        self.current_y = start_y
        self.target_x = x
        self.target_y = y

        
    def do_your_job(self, *arg):
        print(' ---- your agents code goes here ---- ')
        if self.target_y > self.current_y:
            direction = 'S'
            self.current_y += 1
        elif self.target_y < self.current_y:
            direction = 'N'
            self.current_y -= 1
        if self.target_x > self.current_x:
            direction += 'E'
            self.current_x += 1
        elif self.target_x < self.current_x:
            direction += 'W'
            self.current_x -= 1
        
        self.results.append('do_your_job: moving ' + direction)
        print("Setting agent to ", self.current_y, self.current_x)
        self.grd.set_tile(self.start_y, self.start_x, 'A')
        self.grd.save('agent.txt')

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
	
	