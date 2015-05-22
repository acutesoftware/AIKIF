# cls_grid_life.py

import os
import random
import sys
cur_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
lib_folder = os.path.abspath(cur_folder )
aikif_folder = os.path.abspath(cur_folder + os.sep + ".."  )

import aikif.toolbox.cls_grid as mod_grid # 

class GameOfLife(mod_grid.Grid):
    """
    Extend Grid class to support Game of Life
    """
    
    def update_gol(self):
        """
        Function that performs one step of the Game of Life
        """
        
        updated_grid = [[self.update_cell(row, col) \
                            for col in range(self.get_grid_width())] \
                            for row in range(self.get_grid_height())]
        
        self.replace_grid(updated_grid)
       

    def update_cell(self, row, col):
        """
        Function that computes the update for one cell in the Game of Life
        """
        # compute number of living neighbors
        neighbors = self.eight_neighbors(row, col)
        living_neighbors = 0
        for neighbor in neighbors:
            if not self.is_empty(neighbor[0], neighbor[1]):
                living_neighbors += 1
            
        # logic for Game of life        
        if (living_neighbors == 3) or (living_neighbors == 2 and not self.is_empty(row, col)):
            return mod_grid.FULL
        else:
            return mod_grid.EMPTY
        
class GameOfLifePatterns(object):
    """
    class to generate patterns on a grid for Game of Life
    All patterns have a start pos of 2,2 so needs to be offset
    by calling program or random screen generation
    """
    
    def __init__(self, num_patterns, max_x=77, max_y=21):
        self.patterns = []
        self.max_x = max_x
        self.max_y = max_y
        self.pattern_list = ['block','beehive','loaf',          # stationary
                             'boat','blinker','toad','beacon',  # oscillators
                             'glider'                           # gliders
                             ]
        for _ in range(num_patterns):
            pattern_to_add = random.choice(self.pattern_list)
            methodToCall = getattr(sys.modules['cls_grid_life'], pattern_to_add)
            result = methodToCall()
            self.patterns.extend(self.random_offset(self.bitmap_pattern_to_list(result)))

    def get_patterns(self):    
        """ return the list of patterns """
        return self.patterns
        
    def bitmap_pattern_to_list(self, bmp_pat):
        """ 
        takes a list of bitmap points (drawn via Life screen) 
        and converts to a list of full coordinates
        """
        res = []
        x = 1
        y = 1
        lines = bmp_pat.split('\n')
        for line in lines:
            y += 1
            for char in line:
                x += 1
                if char == 'X':
                    res.append([y,x])
        return res
    
    def random_offset(self, lst):
        """ 
        offsets a pattern list generated below to a random
        position in the grid
        """
        res = []
        x = random.randint(4,self.max_x - 42)
        y = random.randint(4,self.max_y - 10)
        for itm in lst:
            res.append([itm[0] + y, itm[1] + x])
        return res

# Patterns are below outside the class to allow for simpler importing
 

# still lifes
def block():
    return '\n'.join([
        '.XX.......', 
        '.XX.......', 
        '..........',  
        '..........', 
        '..........'])

def beehive():
    return '\n'.join([
        '..........', 
        '..XX......', 
        '.X..X.....',  
        '..XX......', 
        '..........'])

def loaf():
    return '\n'.join([
        '..........', 
        '...XX.....', 
        '..X..X....',  
        '...X.X....', 
        '....X.....'])

def boat():
    return '\n'.join([
        '..........', 
        '.XX.......', 
        '.X.X......',  
        '..X.......', 
        '..........'])

# Oscillators
def blinker():
    return '\n'.join([
        '..........', 
        '...XXX....', 
        '..........',  
        '..........', 
        '..........'])
        
def toad():
    return '\n'.join([
        '..........', 
        '..XXX.....', 
        '.XXX......',  
        '..........', 
        '..........'])

def beacon():
    return '\n'.join([
        '.XX.......', 
        '.XX.......', 
        '...XX.....',  
        '...XX.....', 
        '..........'])
        
# Spaceships
def glider():
    return '\n'.join([
        '..........', 
        '......X...', 
        '....X.X...',  
        '.....XX...', 
        '..........'])


def _BLANK():
    return '\n'.join([
        '..........', 
        '..........', 
        '..........',  
        '..........', 
        '..........'])




    