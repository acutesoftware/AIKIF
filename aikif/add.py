# coding: utf-8
# add.py	written by Duncan Murray 12/4/2014
# part of AIKIF - adds data to framework

import sys
import AIKIF_utils as aikif
import fileMapping as filemap
import getopt
			
def usage():
	print('add.py - part of AIKIF')
	print('add.py -s example   # adds a string ')
	print('add.py -t TEST.CSV -r example, col2, col3  # adds a row to table TEST.CSV ')
	print('add.py -t TEST.CSV  # adds a table to list of items being registered to table  ')

try:                                
	opts, args = getopt.getopt(sys.argv[1:], "rst:d", ["help", "grammar="])
except getopt.GetoptError:          
	usage()                         
	sys.exit(2)                     

	
def main():
	glb_txt = ''

	for opt, arg in opts:  
		if opt in ("-h", "--help"): 
			usage()                     
			sys.exit()   
		elif opt == '-s':
			print('Adding ' + arg + ' as string')
			glb_txt = arg
		elif opt == '-r':
			print('Adding ' + arg + ' as row')
			glb_row = arg
		elif opt == '-t':
			print('Adding ' + arg + ' as table')
			glb_table = arg

	add_string(glb_txt)  # todo implement
		
def add_string(txt):
	print ('string = ' + txt )
	
	
def add_row(txt, tbl):
	print ('row = ' + txt )
	
def add_dataset(dt):
	print ('dataset = ' + dt )
	

	
if __name__ == '__main__':
	main()