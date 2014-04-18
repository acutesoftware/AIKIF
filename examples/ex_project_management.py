# ex_project_management.py     written by Duncan Murray 12/4/2014
# example to use AIKIF for project management

import os
import sys
import csv
sys.path.append('..//AI')
import AIKIF_utils as aikif
import fileMapping as filemap
import dataTools.dataTools as dt

import add

# Sample Data (real data taken from database / Excel or agent collection)

goals = [
	{'id': 'python', 'name': 'Learn Python'},
	{'id': 'house', 'name': 'Maintain House'},
	{'id': 'aikif', 'name': 'Build AIKIF'}
	]

projects = [
	{'id': 'aikif', 'parent': '',  'due_date': '12/12/2012', 'name': 'Artificial Intelligence Knowledge Information Framework', 'folder': r'T:\user\dev\src\python\AI'},
	{'id': 'aikif_examples', 'parent': 'aikif', 'due_date': '06/09/2012', 'name': 'Build Examples for AIKIF', 'folder': r'S:\DATA\opendata\ontology\WordNet\wnsqlbuilder\SQL'},
	{'id': 'shelves', 'parent': 'house', 'due_date': '11/05/2012', 'name': 'Put up shelf in kitchen', 'folder':''}
	]

tasks = [
	{'id': '01', 'project': 'shelves', 'dependancy': '', 'name': 'Buy Wood', 'add_date': '1/1/2001', 'due_date': '1/1/2002', 'complete_date': '1/1/2003' },
	{'id': '02', 'project': 'shelves', 'dependancy': '01', 'name': 'Install Shelf' , 'add_date': '2/2/2001', 'due_date': '2/2/2002', 'complete_date': '2/2/2003'},
	{'id': '03', 'project': 'aikif', 'dependancy': '', 'name': 'build core structures' , 'add_date': '3/3/2001', 'due_date': '3/3/2002', 'complete_date': '3/3/2003'},
	{'id': '04', 'project': 'aikif', 'dependancy': '', 'name': 'build example code' , 'add_date': '4/4/2001', 'due_date': '4/4/2002', 'complete_date': '4/4/2003'},
	{'id': '05', 'project': 'aikif', 'dependancy': '04', 'name': 'document usage', 'add_date': '5/5/2001', 'due_date': '5/5/2002', 'complete_date': '5/5/2003' }
	]
	
contacts = [
		{ 'name': 'Duncan', 'contact': 'self'},
		{ 'name': 'Jack', 'contact': 'jack@localhost'},
		{ 'name': 'Jill', 'contact': '555-5656'},
		{ 'name': 'Bunnings', 'contact': 'Main North Road'}
	]
	
resources = [
	{'id': '1', 'name': 'Wood', 'type': 'Building'},
	{'id': '2', 'name': 'Power Drill', 'type': 'Tool'},
	{'id': '3', 'name': 'Text Editor', 'type': 'Development Tool'},
	{'id': '4', 'name': 'Computer', 'type': 'ASSET_COMPUTER'}
	]
	

# AIKIF specific mappings
tableList = ['goals', 'projects', 'tasks', 'contacts']
links = [
	{'src': 'projects.id', 'dest': 'projects.parent', 'weight': 1},
	{'src': 'tasks.id', 'dest': 'tasks.dependancy', 'weight': -1}
	]

aikif_events = [
	{'table': 'tasks',   'column': 'add_date'},
	{'table': 'tasks',   'column': 'due_date'},
	{'table': 'tasks',   'column': 'complete_date'},
	{'table': 'projects',   'column': 'due_date'},
	{'table': 'contacts', 'column': 'add_date'}
]

aikif_objects = [
	{'table': 'resources',  'column': 'name'}
]

aikif_locations = [
	{'table': 'contacts', 'column': 'contact'},
	{'table': 'projects', 'column': 'folder'}
]



def main():
	print('AIKIF Project Management Example')
	print('Uses sample data for a project management schema to generate AIKIF structures')
	#ShowData()
	#for t in tableList:
	#ProcessData('PIM', goals, 'goals')
	ProcessData('project', projects, 'projects')
	#ProcessData('TASK', tasks, 'tasks')
	#ProcessData('contact', contacts, 'contacts')
	#ProcessData('RESOURCE', resources, 'resources')
	
	
def ProcessData(subjectAreaSearch, lst, title):
	subjectArea = filemap.FindOntology(subjectAreaSearch) 
	event_fileList = filemap.GetFullFilename(filemap.FindType('event'), subjectArea[0])    
	object_fileList = filemap.GetFullFilename(filemap.FindType('object'), subjectArea[0])    
	#print('filemap.FindType(object) = ', filemap.FindType('object'))
	#print('subjectAreaSearch = ', subjectAreaSearch)
	#print('subjectArea = ', subjectArea)

	print('Processing - ', title)
	location_fileList = filemap.GetFullFilename(filemap.FindType('location'), subjectArea[0])   
	eventsList = [[0, 'date', 'event_type', 'name']]
	locationsList = [[0, 'folder']]
	objectsList = [[0, 'resources']]

	#print(dic.name)
	for dictRecord in lst:
		text = ''
		#print(dictRecord)
		for k,v in dictRecord.items():  # this is the projects, tasks, contacts or goals
			print('key=',k,', val=',v)
			#text = v['name']
			if k == 'name': 
				text = v
			for e in aikif_events:
				if e['table'] == title:
					print('TESTING k=', k, ' == ', e['column'])
					if e['column'] in k:
#						if text != '':
						print('mapping ', text, ' to ', k) 
						eventsList.append([0, v, k, text])
			for dic in aikif_objects:
				if dic['table'] == title:
					if dic['column'] in k:
						objectsList.append([0, text])
			for dic in aikif_locations:
				if dic['table'] == title:
					if dic['column'] in k:
						objectsList.append([0, text])
			
			
	appendToExistingFiles = False
	if len(locationsList) > 1:
		print('LOCATION :  ' + location_fileList + ' (' + str(len(locationsList)) + ') rows')
		aikif.SaveFileDataToFile(locationsList, location_fileList, appendToExistingFiles)
	if len(eventsList) > 1:	
		print('EVENTS   :  ' + event_fileList + ' (' + str(len(eventsList)) + ') rows')
		aikif.SaveFileDataToFile(eventsList, event_fileList, appendToExistingFiles)
	if len(objectsList) > 1:	
		print('OBJECTS  :  ' + object_fileList + ' (' + str(len(objectsList)) + ') rows')
		aikif.SaveFileDataToFile(objectsList, object_fileList, appendToExistingFiles)


	
	
def ShowData():		
	def show_goals():
		print('Goals = ',  str(len(goals)))
		
	def show_projects():
		print('Projects = ' + str(len(projects)))
		for p in projects:
			#print (p['name'])
			add.add_string(p['name'])
			add.add_dataset(p['folder'])
		
	def show_tasks():
		print('Tasks = ' + str(len(tasks)))
	show_goals()
	show_projects()
	show_tasks()
		

		
if __name__ == '__main__':
	main()