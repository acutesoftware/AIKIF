# cls_grid.py       written by Duncan Murray 15/6/2014
# class to handle a grid used for board and puzzle games

import random

EMPTY = '.'   # TODO - need to change this in multiple places (see worlds.py, cls_grid, world_generator)
FULL = 'X'     


class Grid(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width, pieces, spacing=6):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.spacing = spacing
        self.pieces = pieces
        self.reset()
        self.grid = [[EMPTY for dummy_col in range(self.grid_width)] 
                       for dummy_row in range(self.grid_height)]
        #print(self.grid)
        
                       
    def reset(self):
        """
        Reset the game so the grid is zeros (or default items)
        """
        self.grid = [[0 for dummy_l in range(self.grid_width)] for dummy_l in range(self.grid_height)]

    def clear(self):
        """
        Clears grid to be EMPTY
        """
        self.grid = [[EMPTY for dummy_col in range(self.grid_width)] for dummy_row in range(self.grid_height)]
      
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        output_string = ''
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                output_string += str(self.grid[row][col]).rjust(self.spacing)
            output_string += "\n"
        output_string += "\n"
        return output_string

    def save(self, fname):
        """ saves a grid to file as ASCII text """
        try:
            with open(fname, "w") as f:
                f.write(str(self))
        except Exception as ex:
            print('ERROR = cant save grid results to ' + fname + str(ex))
            
        
        
    def load(self, fname):
        """ loads a ASCII text file grid to self  """
        
        # get height and width of grid from file
        self.grid_width = 4
        self.grid_height = 4
        
        # re-read the file and load it
        self.grid = [[0 for dummy_l in range(self.grid_width)] for dummy_l in range(self.grid_height)]
        with open(fname, 'r') as f:
            for row_num, row in enumerate(f):
                if row == '':
                    break
                for col_num, col in enumerate(row.strip('\n')):   
                    self.set_tile(row_num, col_num, col) 
    
        #print('loaded grid = \n', str(self))
        
        
        

        
        
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def is_empty(self, row, col):
        """
        Checks whether cell with index (row, col) is empty
        """
        return self.grid[row][col] == EMPTY

    def extract_col(self, col):
        """
        get column number 'col'
        """
        new_col = [row[col] for row in self.grid]
        return new_col

    def extract_row(self,  row):
        """
        get row number 'row'
        """
        new_row = []
        for col in range(self.get_grid_width()):
            new_row.append(self.get_tile(row, col))    
        return new_row

    def replace_row(self, line, ndx):
        """ 
        replace a grids row at index 'ndx' with 'line' 
        """
        for col in range(len(line)):
            self.set_tile(ndx, col, line[col])
        
    def replace_col(self, line, ndx):
        """ 
        replace a grids column at index 'ndx' with 'line' 
        """
        for row in range(len(line)):
            self.set_tile(row, ndx, line[row])

    def reverse_line(self, line):
        """
        helper function
        """
        return line[::-1]
      

    def new_tile(self, num=1):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        for _ in range(num):                
            if random.random() > .5: 
                new_tile = self.pieces[0]
            else:
                new_tile = self.pieces[1]
            
            # check for game over
            blanks = self.count_blank_positions()
            
            if blanks == 0:
                print ("GAME OVER")
            else:
                res = self.find_random_blank_cell()
                row = res[0]
                col = res[1]
                self.set_tile(row, col, new_tile)
                

    def count_blank_positions(self):
        """
        return a count of blank cells
        """
        blanks = 0
        for row_ndx in range(self.grid_height - 0):
            for col_ndx in range(self.grid_width - 0):
                if self.get_tile(row_ndx, col_ndx) == EMPTY:
                    blanks += 1
        return blanks
        
    def count_filled_positions(self):
        """
        return a count of blank cells
        """
        filled = 0
        for row_ndx in range(self.grid_height - 0):
            for col_ndx in range(self.grid_width - 0):
                if self.get_tile(row_ndx, col_ndx) != EMPTY:
                    filled += 1
        return filled
        
    def find_random_blank_cell(self):
        if self.count_blank_positions() == 0:
            return None
        row = random.randrange(0, self.grid_height)
        col = random.randrange(0, self.grid_width)
        while self.grid[row][col] != EMPTY:
            row = random.randrange(0, self.grid_height)
            col = random.randrange(0, self.grid_width)
        return [row, col]
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """   
        #print('set_tile: y=', row, 'x=', col)
        if col < 0:
            print("ERROR - x less than zero", col)
            col = 0
            #return
            
        if col > self.grid_width :
            print("ERROR - x larger than grid", col)
            col = self.grid_width - 1
            #return
            
        if row < 0:
            print("ERROR - y less than zero", row)
            row = 0
            #return
            
        if row > self.grid_height:
            print("ERROR - y larger than grid", row)
            row = self.grid_height - 1
            #return
        try:    
            self.grid[row][col] = value
            #if value == 'A':
            #    print("AGENT INSTALLED at ", row, col)
        except Exception:
            print("Error - tile out of range")

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """   
        #print('attempting to get_tile from ', row, col)
        return self.grid[row][col]

    def set_empty(self, row, col):
        """
        Set cell with index (row, col) to be empty
        """
        self.grid[row][col] = EMPTY
    
    def set_full(self, row, col):
        """
        Set cell with index (row, col) to be full
        """
        
        self.grid[row][col] = FULL
    
        
    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self.grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self.grid_width - 1:
            ans.append((row, col + 1))
        return ans

    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self.grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self.grid_width - 1:
            ans.append((row, col + 1))
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))
        if (row > 0) and (col < self.grid_width - 1):
            ans.append((row - 1, col + 1))
        if (row < self.grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))
        if (row < self.grid_height - 1) and (col < self.grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans
    
    def get_index(self, point, cell_size):
        """
        Takes point in screen coordinates and returns index of
        containing cell
        """
        return (point[1] / cell_size, point[0] / cell_size) 

    def replace_grid(self, updated_grid):
        """
        replace all cells in current grid with updated grid
        """
        for col in range(self.get_grid_width()):
            for row in range(self.get_grid_height()):
                if updated_grid[row][col] == EMPTY:
                    self.set_empty(row, col)
                else:
                    self.set_full(row, col)
   
    def find_safe_starting_point(self):
        """
        finds a place on the grid which is clear on all sides 
        to avoid starting in the middle of a blockage
        """
        y = random.randint(2,self.grid_height-4)
        x = random.randint(2,self.grid_width-4)
        return y, x
        
