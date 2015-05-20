# world_generator.py    written by Duncan Murray 9/7/2014

import math
from random import randint 
import aikif.environments.worlds as my_world
import aikif.agents.explore.agent_explore_grid as agt

log_folder = 'T:\\user\\AIKIF\\log\\agents\\worlds'

def main():
    """
    generates a random world, sets terrain and runs agents in it
     TODO - need to change pieces in multiple places (see worlds.py, cls_grid, world_generator)
     (takes about 5 minutes to make 500x400 grid with 8% blockages)
    """
    width       =  40   # grid width 
    height      =  30   # grid height
    iterations  =  200   # how many simulations to run
    num_agents  =   8   # number of agents to enter the world
    
    w = build_world(width, height)
    a = create_random_agents(w, num_agents)
    sim = my_world.WorldSimulation(w, a, 1)
    sim.run(iterations, 'Y', log_folder + '\\agt_run')
    sim.world.grd.save('test_world_traversed.txt')
    
    
def build_world(width, height):    
    time_delay  = 0.3   # delay when printing on screen
    num_seeds   =   6   # number of seed points to start land generation
    perc_land   =  20   # % of world that is land
    perc_sea    =  80   # % of world that is sea
    perc_blocked=   4   # % of world that is blocked
    
    myWorld = my_world.World( height, width, ['.','X','#'])  # TODO - fix passing
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    myWorld.grd.save('test_world.txt')
    return myWorld

def create_random_agents(myWorld, num_agents):    
    #Create some agents to walk the grid
    target_coords = [math.floor(myWorld.grd.grid_height/2) + randint(1, math.floor(myWorld.grd.grid_height/2)) - 3, \
                     math.floor(myWorld.grd.grid_width /2) + randint(1, math.floor(myWorld.grd.grid_width/2)) - 5]
    agt_list = []
    for agt_num in range(0,num_agents):
        ag = agt.ExploreAgent( 'exploring_agent' + str(agt_num),  log_folder, False,1)
        start_y, start_x = myWorld.grd.find_safe_starting_point()
        ag.set_world(myWorld.grd, start_y, start_x, target_coords[0], target_coords[1])
        agt_list.append(ag)
    return agt_list
    
 
main()
