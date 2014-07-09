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
        self.target_x = x
        self.target_y = y
        self.target_x = x
        self.target_y = y
        
    def do_your_job(self, *arg):
        print(' ---- your agents code goes here ---- ')
        if self.target_y > self.start_y:
            direction = 'S'
        elif self.target_y < self.start_y:
            direction = 'N'
        if self.target_x > self.start_x:
            direction += 'E'
        elif self.target_x < self.start_x:
            direction += 'W'
        
        self.results.append('do_your_job: moving ' + direction)
        
    
        

    def show_status(self):
        """
        dumps the status of the agent
        """
        print("Agent Status:")
        print("start_x  = ", self.start_x)
        print("start_y  = ", self.start_y)
        print("target_x = ", self.target_x)
        print("target_y = ", self.target_y)
        
    
def main():
	agt = ExploreAgent('exploring_agent',  'T:\\user\\AIKIF', True)
	print(agt.report())

 		
		
if __name__ == '__main__':
	main()
	
	