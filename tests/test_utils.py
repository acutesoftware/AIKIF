# test_utils.py     written by Duncan Murray 18/4/2014
# functions to assist with unit testing and timing
# USAGE  (from your test script)
# import test_utils as tst
# tst.time_function(moduleName, numTestsToRun, function_name_as_string, function_params)
#
#
# SAMPLE OUTPUT
	#s:\duncan\C\user\dev\src\python\AI\tests>test_utils.py
	#fast_function - 5 tests : tot=0.05 avg=0.009 min=0.009 max=0.009
	#slow_function - 6 tests : tot=0.49 avg=0.082 min=0.081 max=0.083
	#slow_function - 3 tests : tot=1.24 avg=0.413 min=0.412 max=0.417

import os
import sys
import csv
sys.path.append('..//AI')
import time

class Timer:    
	def __enter__(self):
		self.start = time.clock()
		return self

	def __exit__(self, *args):
		self.end = time.clock()
		self.interval = self.end - self.start

		
def slow_function(longerTime=50):
	for i in range(0, 1000 * longerTime):
		for j in range(0,1000):
			x = i * j
	return x

def fast_function():
	j = 0
	for i in range(0,100000):
		j = j + i
		
def fmt_2(f, places):
    return str(round(f, places)).ljust(places+2, '0')

def time_function(modName, numTests, function_name_as_string, *args): 
	minTime = 99999
	maxTime = 0
	totTime = 0
	avgTime = 0
	modNameAsString = modName
	if modName == '':
		modName = sys.modules[__name__]
		modNameAsString = str(sys.modules[__name__]) # .string()
	else:
		modName = sys.modules[modName]
	methodToCall = getattr(modName, function_name_as_string)
	#print('Running', str(numTests), 'tests on function', function_name_as_string)
	for testNum in range(1,numTests + 1):
		with Timer() as t:
			#f(*args)
			result = methodToCall(*args)
		#print('Testnum ',testNum, ' function %.03f sec.' %t.interval)
		if t.interval > maxTime: maxTime = t.interval
		if t.interval < minTime: minTime = t.interval
		totTime += t.interval
	avgTime = totTime / testNum
	#print('Test results: totTime=', str(totTime), ' avg=', str(avgTime), 'min=', minTime, ' max=', maxTime)
	print("{6}.{5} - ran {4} tests :\n tot={0} avg={1} min={2} max={3}".format( fmt_2(totTime, 2), fmt_2(avgTime, 3),  fmt_2(minTime, 3) , fmt_2(maxTime, 3), numTests, function_name_as_string, modNameAsString))
	# {0:2d} 		 '{:.2f}'
	return avgTime, totTime, minTime, maxTime
	
def main(): 	
	time_function('', 5, 'fast_function')
	time_function('', 6, 'slow_function', 1)
	time_function('', 3, 'slow_function', 5)
	
if __name__ == '__main__':
	main()