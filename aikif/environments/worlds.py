# worlds.py     written by Duncan Murray 9/7/2014

from random import randint
import math

import aikif.toolbox.cls_grid as grd

TERRAIN_SEA = '.'  # TODO - need to change this in multiple places (see worlds.py, cls_grid, world_generator)
TERRAIN_LAND = 'X'
TERRAIN_BLOCKED = '#'

class World(object):
    """
    base class for a simple virtual environment
    
    TODO = derive this on the Environment class and fix the rubbish functions
    
    """
    def __init__(self, height, width, terrain):
        self.grd = grd.Grid(height, width, terrain, 1)
        self.refresh_stats()
        print(self.grd)
    
    def __str__(self):
        txt_summary = '\nWorld'
        txt_summary += ', w=' + str(self.grd.grid_width)
        txt_summary += ', h=' + str(self.grd.grid_height)
        
        return txt_summary + '\n' + str(self.grd) + self.show_grid_stats()
    
    def show_grid_stats(self):
        self.refresh_stats()
        txt_summary =" "
        txt_summary += str(self.grd.grid_width) + "w " 
        txt_summary += str(self.grd.grid_height) + "h = " 
        
        txt_summary += str(self.tot_pix) + " cells: " 
        txt_summary += str(self.tot_sea) + "(" + str(math.floor(self.tot_sea*100/self.tot_pix)) + '%) sea + '
        txt_summary += str(self.tot_land) + "(" + str(math.floor(self.tot_land*100/self.tot_pix)) + '%) land + '
        txt_summary += str(self.tot_blocked) + "(" + str(math.floor(self.tot_blocked*100/self.tot_pix)) + '%) blocked'
        return txt_summary
    
    def refresh_stats(self):
        """
        only need this when generating terrain (sea = 100 - perc_land at start).
        This function forces a recount, otherwise just call the variables
        """
        self.tot_pix = 0
        self.tot_sea = 0
        self.tot_land = 0
        self.tot_blocked = 0
        for row in range(self.grd.grid_height):
            for col in range(self.grd.grid_width):
                self.tot_pix += 1
                val = self.grd.get_tile(row, col)
                if val == TERRAIN_SEA: 
                    self.tot_sea += 1
                elif val == TERRAIN_LAND: 
                    self.tot_land += 1
                else:
                    self.tot_blocked += 1
        
    
    def build_random(self, num_seeds=4, perc_land=40, perc_sea=30, perc_blocked=30):
        """
        generates a random world with appropriate percentages
        of land/sea or blocked (cannot pass).
        Start with all sea, pick 3 seed points and grow land there
        until it hits land percentage + perc_blocked.
        Then pick 7 seed points and grow narrow block points until 
        that hits perc_blocked.
        """
        rnge = math.floor(num_seeds/2)
        # self.show_grid_stats()
        seeds = [[randint(0,self.grd.grid_height-1), randint(0,self.grd.grid_width-1)] for _ in range(rnge) for _ in range(rnge)]
        for seed in seeds:
            self.expand_seed(seed, (self.grd.grid_height * self.grd.grid_width)/(perc_sea),  TERRAIN_LAND)
        
        self.refresh_stats()
        #   print(self.show_grid_stats())
        expand = 1
        old_land = self.tot_land
        while (100*self.tot_land)/self.tot_pix < perc_land - 1:
            expand +=1
            
            self.denoise_grid(TERRAIN_LAND, expand)
            self.refresh_stats()
            #  print(expand, self.show_grid_stats())
            if old_land == self.tot_land:   # no extra expansion, so add another seed
                self.expand_seed(self.add_new_seed(), 50, TERRAIN_LAND)
            else:
                old_land = self.tot_land
        self.add_blocks(perc_blocked)
        self.refresh_stats()

         
    def add_new_seed(self):
        y = randint(0,self.grd.grid_height-1)
        x = randint(0,self.grd.grid_width-1)
        print('adding seed = ', y, x)
        return [y, x]
                
    def expand_seed(self, start_seed, num_iterations, val):
        """
        takes a seed start point and grows out in random
        directions setting cell points to val
        """
        self.grd.set_tile(start_seed[0], start_seed[1], val)
        cur_pos = [start_seed[0], start_seed[1]]
        while num_iterations > 0:   # don't use loop as it will hit boundaries often
            num_iterations -= 1
            for y in range(cur_pos[0]-randint(0,2), cur_pos[0] + randint(0,2)):
                for x in range(cur_pos[1]-randint(0,2), cur_pos[1] + randint(0,2)):
                    if x < self.grd.grid_width and x >= 0 and y >= 0 and y < self.grd.grid_height:
                        #print(x,y,val)
                        if self.grd.get_tile(y,x) != val:
                            self.grd.set_tile(y, x, TERRAIN_LAND)
                            num_iterations -= 1
            new_x = cur_pos[0] + randint(0,3)-2
            new_y = cur_pos[1] + randint(0,3)-2
            if new_x > self.grd.grid_width - 1:
                new_x = 0
            if new_y > self.grd.grid_height - 1:
                new_y = 0
            if new_x < 0:
                new_x = self.grd.grid_width - 1
            if new_y < 0:
                new_y = self.grd.grid_height - 1
            cur_pos = [new_y, new_x]    
                
    def denoise_grid(self, val, expand=1):
        """
        for every cell in the grid of 'val' fill all cells
        around it to de noise the grid
        """
        
        updated_grid = [[self.grd.get_tile(y,x) \
                        for x in range(self.grd.grid_width)] \
                        for y in range(self.grd.grid_height)]
        for row in range(self.grd.get_grid_height() - expand):
            for col in range(self.grd.get_grid_width() - expand):
                updated_grid[row][col] = self.grd.get_tile(row,col)  # set original point
                if self.grd.get_tile(row,col) == val:
                    for y in range(-expand, expand):
                        for x in range(-expand, expand):
                            new_x = col+x
                            new_y = row+y
                            if new_x < 0: new_x = 0
                            if new_y < 0: new_y = 0
                            if new_x > self.grd.get_grid_width() - 1: new_x = self.grd.get_grid_width() - 1
                            if new_y > self.grd.get_grid_height() - 1: new_y = self.grd.get_grid_height() - 1
                            # randomly NOT denoise to make interesting edges
                            if expand > 0: 
                                if randint(1,expand * 2) > (expand+1):
                                    updated_grid[new_y][new_x] = val
                            else:
                                updated_grid[new_y][new_x] = val
                        
        
        self.grd.replace_grid(updated_grid)

        
    def add_blocks(self, perc_blocked=30):
        """  
        adds a series of blocks - normally more straight than
        random sea/land features - blocks are default 5x2
        """
        self.refresh_stats()
        #print(self.show_grid_stats())
        while (100*(self.tot_blocked-10))/self.tot_pix < perc_blocked - 1:
            self.add_block()
            self.refresh_stats()
            #print(self.show_grid_stats())
 
    def add_mountains(self):
        """
        instead of the add_blocks function which was to produce
        line shaped walls for blocking path finding agents, this
        function creates more natural looking blocking areas like
        mountains
        """
        from noise import pnoise2
        import random
        random.seed()
        octaves = (random.random() * 0.5) + 0.5
        freq = 17.0 * octaves  # 
        for y in range(self.grd.grid_height - 1):
            for x in range(self.grd.grid_width - 1):
                pixel = self.grd.get_tile(y,x)
                if pixel == 'X':     # denoise blocks of mountains
                    n = int(pnoise2(x/freq, y / freq, 1)*11+5)
                    if n < 1:
                        self.grd.set_tile(y, x, '#')
        
        
 
    def add_block(self):
        """ adds a random size block to the map """
        row_max = self.grd.get_grid_height() - 15
        if row_max < 2:
            row_max = 2
        row = randint(0, row_max)
        
        col_max = self.grd.get_grid_width() - 10
        if col_max < 2:
            col_max = 2
        col = randint(0, col_max)
        
        direction = randint(1,19)-10
        if direction > 0:
            y_len = 10 * (math.floor(self.grd.get_grid_height() / 120) + 1)
            x_len = 1 * (math.floor(self.grd.get_grid_width() / 200) + 1)
        else:
            y_len = 1 * (math.floor(self.grd.get_grid_height() / 200) + 1)
            x_len = 10 * (math.floor(self.grd.get_grid_width() / 120) + 1)
        
        print("Adding block to ", row, col, direction)
        for r in range(row, row + y_len):
            for c in range(col, col + x_len):
                self.grd.set_tile(r,c,TERRAIN_BLOCKED)
        


class WorldSimulation(object):
    """
    takes a world object and number of agents, objects
    and runs a simulation
    
    """
    def __init__(self, cls_world, agent_list, LOG_LEVEL):
        self.world = cls_world
        self.agent_list = agent_list
        self.LOG_LEVEL = LOG_LEVEL
        #print("WorldSimulation:Simulation loading...")
    
    def run(self, num_runs, show_trails, log_file_base):
        """
        Run each agent in the world for 'num_runs' iterations
        Optionally saves grid results to file if base name is
        passed to method.
        """
        print("--------------------------------------------------")
        print("Starting Simulation - target = ", self.agent_list[0].target_y, self.agent_list[0].target_x)
        self.world.grd.set_tile(self.agent_list[0].target_y , self.agent_list[0].target_x , 'T')
        #self.highlight_cell_surroundings(self.agent_list[0].target_y, self.agent_list[0].target_x)
        self.start_all_agents()
        # save the agents results here
        try:
            with open (log_file_base + '__agents.txt', "w") as f:
                f.write("Starting World = \n")
                f.write(str(self.world.grd))
        except Exception:
            print('Cant save log results to ' + log_file_base)
            
        for cur_run in range(0,num_runs):
            print("WorldSimulation:run#", cur_run)
            for num, agt in enumerate(self.agent_list):
                if show_trails == 'Y':
                    if len(self.agent_list) == 1 or len(self.agent_list) > 9:
                        self.world.grd.set_tile(agt.current_y, agt.current_x, 'o')
                    else:
                        self.world.grd.set_tile(agt.current_y, agt.current_x, str(num))
                agt.do_your_job()
                self.world.grd.set_tile(agt.current_y, agt.current_x, 'A')    # update the main world grid with agents changes
            
            # save grid after each run if required
            if log_file_base != 'N':
                self.world.grd.save(log_file_base + '_' + str(cur_run) + '.log')
    
        # save the agents results here
        with open (log_file_base + '__agents.txt', "a") as f:
            f.write("\nWorld tgt= [" + str(self.agent_list[0].target_y) + "," + str(self.agent_list[0].target_x) + "]\n")
            f.write(str(self.world.grd))
            f.write('\n\nAgent Name , starting, num Steps , num Climbs\n')
            for num, agt in enumerate(self.agent_list):
                res = agt.name + ' , [' + str(agt.start_y) + ', ' + str(agt.start_x) + '], '
                res += str(agt.num_steps)  + ' , ' + str(agt.num_climbs) + ' , '
                res += ''.join([a for a in agt.results])
                f.write(res + '\n')
                
    def highlight_cell_surroundings(self, target_y, target_x):
        """
        highlights the cells around a target to make it simpler
        to see on a grid. Currently assumes the target is within
        the boundary by 1 on all sides
        """
        if target_y < 1:
            print("target too close to top")
        if target_y > self.world.grd.grid_height - 1:  
            print("target too close to bottom")
        if target_x < 1:
            print("target too close to left")
        if target_x < self.world.grd.grid_width:  
            print("target too close to right")
        #valid_cells = ['\\', '-', '|', '/']    
        self.world.grd.set_tile(target_y - 1, target_x - 1, '\\')
        self.world.grd.set_tile(target_y - 0, target_x - 1, '-')
        self.world.grd.set_tile(target_y + 1, target_x - 1, '/')

        self.world.grd.set_tile(target_y - 1, target_x - 0, '|')
        self.world.grd.set_tile(target_y + 1, target_x - 0, '|')
        
        self.world.grd.set_tile(target_y - 1, target_x + 1, '/')
        self.world.grd.set_tile(target_y - 0, target_x + 1, '-')
        self.world.grd.set_tile(target_y + 1, target_x + 1, '\\')
        
               
    
    def start_all_agents(self):
        """
        Start all agents - not sure yet if this method 
        should be used - probably leave this up to the 
        calling procedure so it can be managed, but put
        here for simplicity now.
        """
        for agt in self.agent_list:
            agt.start()
            #print(agt.name, " has started")
 
