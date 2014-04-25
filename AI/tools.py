# coding: utf-8
# tools.py	written by Duncan Murray 20/3/2014	(C) Acute Software
# Script to configure the functional toolbox of AIKIF

import os
import AIKIF_utils as aikif
import fileMapping as filemap
import toolbox.Toolbox as tool

fldr = os.getcwd() + '\\toolbox\\'

def main():
	tl = tool.Toolbox()

	
	progName = os.getcwd() + '\\toolbox\\solve_knapsack.py'
	tl.add({'file':progName, 'function':'solve_greedy_trivial', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'solve_smallest_items_first', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'solve_expensive_items_first', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'solve_value_density', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'main', 'args':['int', 'dict'], 'return':['int', 'list']})
	#tl.add({'file':'solve_knapsack.py', 'function':'', 'args':['int', 'dict'], 'return':['int', 'list']})

	tl.save('tools.txt')

	tl.run(tl.lstTools[0])
		
if __name__ == '__main__':
    main()	
	
