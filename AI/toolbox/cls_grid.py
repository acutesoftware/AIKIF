# cls_grid.py		written by Duncan Murray 15/6/2014
# class to handle a grid used for board and puzzle games

import random

class Grid:
	"""
	Class to run the game logic.
	"""

	def __init__(self, grid_height, grid_width, pieces):
		self.grid_height = grid_height
		self.grid_width = grid_width
		self.grid = []
		self.pieces = pieces
		self.reset()

	def reset(self):
		"""
		Reset the game so the grid is empty.
		"""
		self.grid = [[0 for dummy_l in range(self.grid_width)] for dummy_l in range(self.grid_height)]
	 
	def __str__(self):
		"""
		Return a string representation of the grid for debugging.
		"""
		output_string = "Printing Grid\n"
		for row in range(self.grid_height):
			for col in range(self.grid_width):
				output_string += str(self.grid[row][col]).rjust(6)
			output_string += "\n"
		output_string += "\n"
		return output_string
		
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
		for i in range(num):				
			if random.random() > .5: 
				new_tile = self.pieces[0]
			else:
				new_tile = self.pieces[1]
			
			# check for game over
			blanks = self.count_blank_positions()
			
			if blanks == 0:
				print ("GAME OVER")
			else:
				row, col = self.find_random_blank_cell()
				self.set_tile(row, col, new_tile)
				

	def count_blank_positions(self):
		"""
		return a count of blank cells
		"""
		blanks = 0
		for row_ndx in range(self.grid_height - 0):
			for col_ndx in range(self.grid_width - 0):
				cell = self.get_tile(row_ndx, col_ndx)
				if cell == 0:
					blanks += 1
		return blanks
		
	def find_random_blank_cell(self):
		if self.count_blank_positions() == 0:
			return None
		row = random.randrange(0, self.grid_height)
		col = random.randrange(0, self.grid_width)
		while self.grid[row][col] != 0:
			row = random.randrange(0, self.grid_height)
			col = random.randrange(0, self.grid_width)
		return row, col
		
	def set_tile(self, row, col, value):
		"""
		Set the tile at position row, col to have the given value.
		"""   
		self.grid[row][col] = value

	def get_tile(self, row, col):
		"""
		Return the value of the tile at position row, col.
		"""        
		return self.grid[row][col]

