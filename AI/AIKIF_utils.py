# AIKIF_utils.py   written by Duncan Murray 28/7/2013  (C) Acute Software
# AIKIF = Artificial Intelligence Knowledge Information Framework
# This contains the functions to load the information accessible by all 
# AI componants

import os
import sys
import csv
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle

localPath = '..//data//' # os.getcwd()
logFileProcess = localPath + 'log//process.log'
logFileSource = localPath + 'log//source.log'
logFileCommand = localPath + 'log//command.log'
logFileResult = localPath + 'log//result.log'

# -----------------------------------------
# --   Prepare Data structures 
# -----------------------------------------
def build_AIKIF_structure():
    AIKIF_FileList = []  # filelist is a list of dictionary objects
    AIKIF_FileList.append({"fname": "refObject.csv", "fields":["objectTypeName","PhysicalType", "description"], "use": "Top level ref file for objects"} )
    AIKIF_FileList.append({"fname": "refAction.csv", "fields":["ActionTypeName","PhysicalType", "description"], "use": "Top level ref file for actions"} )

    AIKIF_FileList.append({"fname": "rawData.csv", "fields":["date","source","person","raw_string"], "use": "Holds raw data found on web"} )
    AIKIF_FileList.append({"fname": "bias.csv", "fields":["source","weight"], "use": "BIAS values to rate the accuracy of data" } )
    AIKIF_FileList.append({"fname": "websites.csv", "fields":["url","bias"], "use": "websites for bias rankings" } )
    AIKIF_FileList.append({"fname": "people.csv", "fields":["username","source_type","source_locations", "bias"], "use": "people / usernames for bias rankings" } )
    AIKIF_FileList.append({"fname": "goal_types.csv", "fields":["rating", "goal_type", "description"], "use": "details on types of goals for the AI" } )
    AIKIF_FileList.append({"fname": "goals.csv", "fields":["goal_type", "category", "priority", "perc_complete", "goal_name", "goal_description"], "use": "goals for the AI" } )
    AIKIF_FileList.append({"fname": "knowledge.csv", "fields":["category", "fact", "weight"], "use": "extrapolated knowledge" } )
    AIKIF_FileList.append({"fname": "commands.csv", "fields":["command", "priority"], "use": "list of things to do as told by human operator" } )

   
    return AIKIF_FileList

def showColumnStructures(AIKIF_FileList):
    print('\n--------------   Column Structures of Data Files  -----------------')
    for j in range(len(AIKIF_FileList)):
        for key in AIKIF_FileList[j]:  # dont use sorted function
            if key == 'fname':
                dat.print_no_newline('\n ' + AIKIF_FileList[j][key].ljust(14, ' ') + ': ') 
            if key == 'fields':
                for fld in AIKIF_FileList[j][key]:
                    dat.print_no_newline(fld + ',' )  # prints all heirachy - works
    print('\n-------------------------------------------------------------------\n')
	
def debugPrintFileStructures(AIKIF_FileList):
    for j in range(len(AIKIF_FileList)):
        for key in sorted(AIKIF_FileList[j]):
            print('     ', key, '\t=>', AIKIF_FileList[j][key])  # prints all heirachy - works
    print ("AIKIF_FileList[0][\"fname\"]  = ", AIKIF_FileList[0]["fname"] )
    print ("AIKIF_FileList[1][\"fields\"][0] = ", AIKIF_FileList[1]["fields"][0] )

def printFileList(l): 
    fileList = [row['fname'] for row in l]
    numFiles = 0 
    for fileName in fileList:
        fileName = localPath + 'temp//' + fileName
        numFiles=numFiles+1
        print (fileName, "\t",dat.countLinesInFile(fileName), "rows" , "\t(", os.path.getsize(fileName), "bytes)")
  
    
def getFileList(l):
    lst = []
    fileList = [row['fname'] for row in l]
    numFiles = 0
    for fileName in fileList:
        lst.append(fileName)
    return lst
    
        
def SaveFileList(fl, filename):
    lst = getFileList(fl)
    w = open(filename, "wt")
    w.writelines(list( "%s\n" % item for item in lst ))
    w.close()

def GetElementsAsString(lst, delim, quote='"'):
    # gets the remaining elements of a list as strings
	opLst = []
	for itm in lst:
		opTxt = ''
		for i in itm:
			if type(i) is str:
				#if len(i.strip()) > 0:
				opTxt = opTxt + quote + i.strip('"') + quote + delim
			else:
				opTxt = opTxt + quote + str(i) + quote + delim
		if opTxt[-1:] == delim:
			#opTxt = opTxt + quote + quote  # this works but adds a new blank field (not a big deal)
			# opTxt = opTxt.strip(delim)	# remove the last delim from line
			pass
		
		opLst.append(opTxt)
		#print ('GetElementsAsString='  + opTxt)
	return(opLst)

def SaveFileDataToFile(lst, filename, append=False):
	if append == True:
		w = open(filename, "at")
	else:
		w = open(filename, "wt")
	for line in GetElementsAsString(lst, ','):
		#print('line = _' + line + '_')
		w.writelines(line + '\n')
	w.close()


    
# -----------------------------------------
# --   Logging Functions 
# -----------------------------------------
def LogDataSource(src, prg=''):
    # function to collect raw data from the web and hard drive[ currently using documents on disk instead of web ]
    #print(' source  =', src)
	fle.log(logFileSource , dat.ForceToString(src), prg)
    
def LogProcess(process, prg=''):
    # log a process or program
    #print(' process = ', process)
	fle.log(logFileProcess, dat.ForceToString(process), prg)

def LogCommand(cmd, prg=''):
    # record the command passed
    #print(' command = ', cmd)
	fle.log(logFileCommand , dat.ForceToString(cmd), prg)

def LogResult(res, prg=''):
    # record the output of the command
    #print('   result    = ', res)
	fle.log(logFileResult , dat.ForceToString(res), prg)
    

 


