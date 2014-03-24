# processRawData.py   written by Duncan Murray 16/3/2014  (C) Acute Software
# script to process raw data into core tables in AIKIF, like events processes
# The logging of the PROCESSing occurs here, but the logging (and storage) of
# the src file locations needs to stay with the program itself, as that should
# encapsulate and handle the info there, rather than one big list


import subprocess
import sys
import AIKIF_utils as aikif
import fileMapping as filemap

def main():
	print('processRawData.py - process raw information to core tables in AIKIF')
	run('loadCountry_Gdeltproject.py')
	run('loadPIM_shoppingList.py')
	run('loadPIM_Filelist.py')
	
	# load ontology - S:\DATA\opendata\ontology\COSMO 
	
	print('Done')

def run(scriptFile, logUsage='Y'):
	from subprocess import call
	print('  ... running ' + scriptFile)
	aikif.LogProcess(scriptFile)
	try:
		retcode = call(scriptFile + ' Q', shell=True)   # Q tells program to run in silent mode
		if retcode < 0:
			#print("Child was terminated by signal", -retcode, file=sys.stderr)
			aikif.LogResult(scriptFile + ' terminated by signal')
		else:
			#print("Child returned", retcode, file=sys.stderr)
			aikif.LogResult(scriptFile + ' success')
	except OSError as e:
		#print("Execution failed:", e, file=sys.stderr)	
		aikif.LogResult(scriptFile + ' error')
	
if __name__ == '__main__':
    main()	
	
	