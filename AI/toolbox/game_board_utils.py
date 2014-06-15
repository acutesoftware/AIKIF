# game_board_utils.py	written by Duncan Murray 15/6/2014
# misc functions to manipulate lists and grids in a game board
# part of toolbox for AIKIF. most of these will later be parts 
# of appropriate classes (cls_board, cls_2048, etc) but here to
# assist testing usage of functions within Toolbox class.
# 

def TEST():
	""" tests for this module """
	from cls_grid import Grid
	
	grd = Grid(4,4, [2,4])
	grd.new_tile()
	grd.new_tile()
	print(grd)
	print("There are ", grd.count_blank_positions(), " blanks in grid 1\n")

	grd2 = Grid(5,5, ['A','B'])
	grd2.new_tile(26)
	print(grd2)
	
	
	print("There are ", grd2.count_blank_positions(), " blanks in grid 2")


TEST()