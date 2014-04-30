# coding: utf-8
# tools.py	written by Duncan Murray 20/3/2014	(C) Acute Software
# Script to configure the functional toolbox of AIKIF

import os
import sys
import AIKIF_utils as aikif
import fileMapping as filemap
import toolbox.Toolbox as tool
import time
from random import randint

fldr = os.getcwd() + '\\toolbox\\'
sys.path.append(fldr)

def main():
	tl = tool.Toolbox()


	tl.add({'file':fldr + 'test_tool.py', 'function':'sum_even_numbers', 'args':['list'], 'return':['int']})
	tl.add({'file':fldr + 'test_tool.py', 'function':'get_min_even_num', 'args':['list'], 'return':['int']})
	tl.add({'file':fldr + 'test_tool.py', 'function':'test_function', 'args':[], 'return':['int']})
	# 	 test_function():
	
	progName = os.getcwd() + '\\toolbox\\solve_knapsack.py'
	tl.add({'file':progName, 'function':'solve_greedy_trivial', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'solve_smallest_items_first', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'solve_expensive_items_first', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'solve_value_density', 'args':['int', 'dict'], 'return':['int', 'list']})
	tl.add({'file':progName, 'function':'main', 'args':['int', 'dict'], 'return':['int', 'list']})
	#tl.add({'file':'solve_knapsack.py', 'function':'', 'args':['int', 'dict'], 'return':['int', 'list']})

	
	tl.save('tools.txt')
	args = [1,2,3,4,5,6,7]
	for ndx in range(0,2):
		testResult = tl.run(tl.lstTools[ndx], args, 'N')
		print('Ran test on ', os.path.basename(tl.lstTools[ndx]['file']) + '->' + tl.lstTools[ndx]['function'], ' Result = ', testResult)

#	testResult = tl.run(tl.lstTools[1], args, 'N')
#	print('Ran test on ', os.path.basename(tl.lstTools[1]['file']) + '->' + tl.lstTools[0]['function'], ' Result = ', testResult)
	
	
	run_multiple(tl, tl.lstTools[0], 500)
	

def run_multiple(t1, tool, numIterations, silent='Y'):
	results = []
	start_time = time.time()		
	for i in range(0,numIterations):
		args = [randint(10,99) for j in range(1,randint(2,5))]
		testname = tool['file'] + '.' + tool['function']
		answer = t1.run(tool, args, silent)
		results.append({'tool':testname, 'args':args, 'result':answer})
	print("Method1 = ", time.time() - start_time, "seconds")
	print('Done processing ' + str(len(results)) + ' calculations')
	return results
	


	
if __name__ == '__main__':
    main()	
	
