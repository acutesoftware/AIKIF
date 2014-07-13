# world_generator.py    written by Duncan Murray 9/7/2014

import os
import sys
import math
from random import randint 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)
import AI.environments.worlds as my_world
import AI.agents.explore.agent_explore_grid as agt

log_folder = 'T:\\user\\AIKIF\\log\\agents\\world_gen_logs'
LOG_LEVEL = 5

def main():
    """
    generates a random world, sets terrain and runs agents in it
     TODO - need to change pieces in multiple places (see worlds.py, cls_grid, world_generator)
    """
    width       =  50   # grid width
    height      =  20   # grid height
    time_delay  = 0.3   # delay when printing on screen
    num_seeds   =   4   # number of seed points to start land generation
    perc_land   =  20   # % of world that is land
    perc_sea    =  80   # % of world that is sea
    perc_blocked=  10   # % of world that is blocked
    
    myWorld = my_world.World( height, width, ['.','X','#'])  # TODO - fix passing
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    myWorld.grd.save('test_world.txt')
    
    #Create some agents to walk the grid
    iterations  =   40   # how many simulations to run
    num_agents  =   3   # number of agents to enter the world
    years       = 100   # how many times to run each simulation
    target_coords = [math.floor(myWorld.grd.grid_height/2) + randint(1, math.floor(myWorld.grd.grid_height/2)) - 3, \
                     math.floor(myWorld.grd.grid_width /2) + randint(1, math.floor(myWorld.grd.grid_width/2)) - 5]
    agt_list = []
    for agt_num in range(0,num_agents):
        ag = agt.ExploreAgent( 'exploring_agent' + str(agt_num),  log_folder, False, LOG_LEVEL)
        ag.set_world(myWorld.grd, randint(2,myWorld.grd.grid_height-4), randint(2,myWorld.grd.grid_width-4), target_coords[0], target_coords[1])
        agt_list.append(ag)
    sim = my_world.WorldSimulation(myWorld, agt_list, LOG_LEVEL)
    sim.run(iterations, 'Y', log_folder + '\\agt_run')
    
    
main()
