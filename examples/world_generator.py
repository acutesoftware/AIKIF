# world_generator.py    written by Duncan Murray 9/7/2014

import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder)
import AI.environments.worlds as my_world

def main():
    """
    generates a random world, sets terrain and runs agents in it
    """
    iterations  =  10   # how many simulations to run
    years       = 100   # how many times to run each simulation
    width       =  40   # grid width
    height      =  20   # grid height
    time_delay  = 0.3   # delay when printing on screen
    num_seeds   =   4   # number of seed points to start land generation
    perc_land   =  50   # % of world that is land
    perc_sea    =  35   # % of world that is sea
    perc_blocked=  30   # % of world that is blocked
    myWorld = my_world.World( height, width, [0,1,2])
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    #print(myWorld)
    myWorld.denoise_grid(my_world.TERRAIN_LAND, 1)
    print(myWorld)
    myWorld.grd.save('test_world.txt')
main()
