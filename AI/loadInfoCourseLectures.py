# coding: utf-8
# loadInfoCourseLectures.py   written by Duncan Murray 5/4/2014  (C) Acute Software
# script to demostrate collecting and logging data in AIKIF


import os
import sys
sys.path.append('..//..//aspytk')
import lib_data as dat
import lib_file as fle
import lib_net as net
import AIKIF_utils as aikif
import fileMapping as filemap
import index

import json
from pprint import pprint

silent = 'N'
if len(sys.argv) == 2:
	if sys.argv[1] == 'Q':
		silent = 'Y'


rootFolderLectures = r"P:\__Downloads\lectures"
#rootFolderLectures = r"P:\__Downloads\lectures\matrix\matrix-001"
subjectArea = filemap.FindOntology('Course') # should return 'INFO-COURSE'
print ( 'subjectArea = ' + subjectArea[0])

object_fileList = filemap.GetFullFilename(filemap.FindType('object'), subjectArea[0])    
location_fileList = filemap.GetFullFilename(filemap.FindType('location'), subjectArea[0])   
course_fileList = filemap.GetFullFilename(filemap.FindType('location'), subjectArea[0])   

# Now also save the information as FILES
fileSubjectArea = filemap.FindOntology('FILE-LECTURES') # should return 'SYSTEM-PC-FILE-LECTURES'
print ( 'fileSubjectArea = ' + fileSubjectArea[0])
lectures_fileList = filemap.GetFullFilename(filemap.FindType('thing'), fileSubjectArea[0])    


# Standard functions for all loading scripts to allow querying from file mapper and checker
def GetSrcURL(): return ''
def GetTempFile(): return ''
def GetOutputFile(): return ''

 
def main():

	if silent == 'N':
		print('loadInfoCourseLectures.py - process raw information to core tables in AIKIF')

	courses, locations, objects = LoadData_Lectures(rootFolderLectures)
	#PrintList(objects)
	#PrintList(locations)

	aikif.SaveFileDataToFile(locations, location_fileList)
	aikif.SaveFileDataToFile(objects, lectures_fileList)
	aikif.SaveFileDataToFile(courses, object_fileList)

	
	if silent == 'N':
		DisplayShortListOutput(objects, 'objects')
		DisplayShortListOutput(locations, 'locations')
		DisplayShortListOutput(courses, 'courses')
		#DisplayShortListOutput(links, 'links')
		print('Done..')
		
  
def BuildUniqueLocations(locListWITH_duplicates):
    newList = []
    location_key = 1
    locList = dat.remove_duplicates(locListWITH_duplicates)
    for i in locList:
        location_key = location_key + 1
        for j in i:
            newList.append([location_key, j])
    #print(newList)
    return newList
 
  
def LoadData_Lectures(rootFolder):
    # reads a root folder containing downloaded lectures
    # and saves the core list as objects.
	# Then indexes all words in (.SRT) files to build a reference
	# table for searching
	# File Sample - .SRT Files
	# 1
	# 00:00:00,012 --> 00:00:06,902					# video time
	# >> And here is part of the planning graph		# spoken text
	# for the simple dock worker robot example

	# 2
	# 00:00:06,902 --> 00:00:12,510
	# you've seen earlier.
	# You remember the initial state consisted

	# Returns:
	# LECTURES
	# 0	lectures
	# 1	P:\__Downloads\lectures\infomation_risk_management\1 - 2 - Course Outline.mp4
	# 2	P:\__Downloads\lectures\infomation_risk_management\3 - 6 - The Evolution of Vulnerabilities.mp4
	# 3	P:\__Downloads\lectures\data_analysis\9 - 2 - Bootstrap (19-03).mp4
	# 4	P:\__Downloads\lectures\data_analysis\4 - 3 - Organizing a Data Analysis (16-13).mp4

	locations = [[0, 'folder']]
	objects = [[0, 'lectures']]
	object_key = 0
	
	# COURSE_KEY, c.name, c.short_name, c.uni, location, country, c.instructor, c.crsOff, weblink, c.categ
	courses = [[0, 'courses', 'short_name', 'uni', 'location', 'country', 'instructor', 'crsOff', 'weblink', 'categories']]
	course_key = 0
	# process the file into structures
	ndxFile = 'ndxFullLecture.txt'
	opIndex = 'ndxWordsToFilesLecture.txt'
    
	if silent == 'N':
		print (' reading folder ' , rootFolder)

	filelist = fle.GetFileList([rootFolder], ['*.*'], ["Thumbs.db", "thumbs.db"], False)
	for file in filelist:
		xtn = os.path.splitext(file)[-1].lower()
		lpath = fle.GetPath(file)
		#print (file, xtn)
		if xtn == '.mp4':	# Lecture
			object_key = object_key + 1
			objects.append([object_key, file])
		elif xtn == '.srt':	# Text of spoken words in videos
			IndexLectureText(file, ndxFile)
		elif xtn == '.json':	# Root info file for the course
			course_key = course_key + 1
			courses.append(ExtractCourseData(file, course_key))
			
		locations.append([lpath])
		
	#print(courses)	
	# Get the list of folders (not sure why, just as a test?)
	index.consolidate(ndxFile, opIndex )

	
	return(courses, BuildUniqueLocations(locations), objects)

def IndexLectureText(f, ndxFile):
	try:
		index.buildIndex(f, ndxFile, 'Y', 'Y')  # append=Y and silent=Y
	except:
		print('error indexing ', f)
		
	
	
def ExtractCourseData(jsonFile, course_key):
	# extracts course information from a coursera .json file
	# returns items in a list for now
	# COURSE_KEY, c.name, c.short_name, c.uni, location, country, c.instructor, c.crsOff, weblink, c.categ
	# == c[0], 		c[1], 		c[2]	c[3]	c[4]	c[5], 			
	json_data=open(jsonFile)
	data = json.load(json_data)
	#pprint(data)
	json_data.close()
	
	lst = []
	lst.append(course_key)
	lst.append(data["name"])
	lst.append(data["short_name"])
	
	lst.append(data["universities"][0]["name"])    # just the first uni
	lst.append(data["universities"][0]["location"])
	lst.append(data["universities"][0]["location_country"])
	for uni in data["universities"]:
		print(uni["abbr_name"], ' - ' ,uni["name"] , uni["location_country"] , uni["website"], uni["location"] )
	lst.append(data["instructor"])
		
	lst.append(data["courses"][0]["start_year"])	
	for crsOffering in data["courses"]:
		print(crsOffering["start_year"], crsOffering["start_date_string"], crsOffering["home_link"])   # one per course offering, but no way to know which offering you did, so ignore
		latestWebLink = crsOffering["home_link"]
		
	lst.append(latestWebLink)
	
	txt = ''	
	for cat in data["categories"]:
		txt = txt + (cat["name"]) + '; '
	lst.append(txt)
	return lst
		



	
def DisplayShortListOutput(lst, title):
    num = 1
    print('\n' + title + ' - ' + str(len(lst)) + ' elements')
    for i in lst:
        if num < 4:
            print(num, ' - ' , i)
        num = num + 1
    
		
if __name__ == '__main__':
    main()	
		
