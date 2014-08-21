# game_board_utils.py	written by Duncan Murray 15/6/2014
# misc functions to manipulate lists and grids in a game board
# part of toolbox for AIKIF. most of these will later be parts 
# of appropriate classes (cls_board, cls_2048, etc) but here to
# assist testing usage of functions within Toolbox class.
# 

from cls_grid import Grid

def build_board_2048():
	""" builds a 2048 starting board 
	Printing Grid
     0     0     0     2
     0     0     4     0
     0     0     0     0
     0     0     0     0

	"""
	grd = Grid(4,4, [2,4])
	grd.new_tile()
	grd.new_tile()
	print(grd)
	return grd
	
def build_board_checkers():
	""" builds a checkers starting board 
	Printing Grid
     0     B     0     B     0     B     0     B
     B     0     B     0     B     0     B     0
     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0
     0     W     0     W     0     W     0     W
     W     0     W     0     W     0     W     0
	"""
	grd = Grid(8,8, ["B","W"])
	for c in range(4):
		grd.set_tile(0,(c*2) - 1, "B")
		grd.set_tile(1,(c*2) - 0, "B")
		grd.set_tile(6,(c*2) + 1, "W")
		grd.set_tile(7,(c*2) - 0, "W")
	print(grd)
	
	return grd
	

def TEST():
	""" tests for this module """
	
	
	grd = Grid(4,4, [2,4])
	grd.new_tile()
	grd.new_tile()
	print(grd)
	print("There are ", grd.count_blank_positions(), " blanks in grid 1\n")

	grd2 = Grid(5,5, ['A','B'])
	grd2.new_tile(26)
	print(grd2)
	build_board_checkers()
	
	print("There are ", grd2.count_blank_positions(), " blanks in grid 2")

#build_board_checkers()
build_board_2048()
#TEST()