# world_generator.py    written by Duncan Murray 9/7/2014

import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)
import AI.environments.worlds as my_world
import AI.agents.explore.agent_explore_grid as agt

def main():
    """
    generates a random world, sets terrain and runs agents in it
     TODO - need to change pieces in multiple places (see worlds.py, cls_grid, world_generator)
    """
    iterations  =  10   # how many simulations to run
    years       = 100   # how many times to run each simulation
    width       =  55   # grid width
    height      =  15   # grid height
    time_delay  = 0.3   # delay when printing on screen
    num_seeds   =   4   # number of seed points to start land generation
    perc_land   =  40   # % of world that is land
    perc_sea    =  50   # % of world that is sea
    perc_blocked=  10   # % of world that is blocked
    myWorld = my_world.World( height, width, ['.','X','#'])  # TODO - fix passing
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    #print(myWorld)
    myWorld.grd.save('test_world.txt')
    
    #Create some agents to walk the grid
    target_coords = [myWorld.grd.grid_height - 4, myWorld.grd.grid_width - 3]
    ag1 = agt.ExploreAgent( 'exploring_agent1',  'T:\\user\\AIKIF', False)
    ag1.set_world(myWorld.grd, 4,4, target_coords[0], target_coords[1])
    ag2 = agt.ExploreAgent( 'exploring_agent2',  'T:\\user\\AIKIF', False)
    ag2.set_world(myWorld.grd, 8,3, target_coords[0], target_coords[1])
    sim = my_world.WorldSimulation(myWorld, [ag1, ag2])
    sim.run(4, 'T:\\user\\AIKIF\\log\\agents\\agt_run')
    print("TODO - agents run , but grid save is saving the agents copy of grid without movement")
    
    
main()
