# AIKIF_utils.py   written by Duncan Murray 28/7/2013  (C) Acute Software
# AIKIF = Artificial Intelligence Knowledge Information Framework
# This contains the functions to load the information accessible by all 
# AI componants

import os
import sys
import csv
sys.path.append('C://user//dev//src//python//_AS_LIB')
import as_util_data as dat

localPath = "C://user//dev//src//python//AI//"

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

    
# -----------------------------------------
# --   Logging Functions 
# -----------------------------------------
def LogDataSource(src):
    # function to collect raw data from the web and hard drive[ currently using documents on disk instead of web ]
    print(' source  =', src)
    
def LogProcess(process):
    # function to process raw data using Bias tables to get a comprehension of the information
    print(' process = ', process)

def LogCommand(cmd):
    # function to process raw data using Bias tables to get a comprehension of the information
    print(' command = ', cmd)

def LogResult(res):
    # function to process raw data using Bias tables to get a comprehension of the information
    print('   result    = ', res)
    
    