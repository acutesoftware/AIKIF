# generateTestData.py		written by Duncan Murray 17/4/2014


import os
import sys
import csv
import random
import binascii
import string

names = 'S:\\DATA\\opendata\\datasets\\names.csv'  # via http://www.cs.princeton.edu/introcs/data/names.csv
places = 'S:\\duncan\\C\\user\\dev\\src\\python\\AI\\data\\LOCATION_WORLD.CSV'  # use fileMap GETONTOLOGY
wordList = 'S:\\duncan\\C\\user\\dev\\src\\python\\AI\\data\\nounList.txt'

def TEST():
	print('generateTestData.py')
	print('Creates random data and strings in various formats')
	print('Random Strings....\n  ', random_hex_string(20), '\n  ', random_letters(50))
	print('Random Block ....')
	print(random_block(40,3))
	print('Data Table ....')
	colLabel = ['DATE', 'name', 'password', 'Born',  'Quote', 'Score']
	colTypes = ['DATE', 'PEOPLE', 'STRING', 'PLACE', 'WORD',  'INT']
	tbl = random_table(6,50, colTypes, colLabel)
	show_table(tbl)
	save_table(tbl, 'test123.csv')
	
def random_int(min=0, max=100): return random.randrange(min, max)
	
def random_letters(sze=20):
	lst = [random.choice(string.ascii_letters + string.digits) for n in range(sze)]
	return "".join(lst)

	
def random_hex_string(sze=30):
	return binascii.b2a_hex(os.urandom(sze))
	
def random_block(cols=40, rows=5):
	op = ''
	for r in range(0,rows):
		op = op + random_letters(sze=cols) + '\n'
	return op

def random_table(cols=3, rows=10, colSpecs =[], hdr=[]):
	# verify the colSpecs required and assign defaults to empty sets
	colTypes = fill_colList_blanks(colSpecs, cols)
	print('Generating columns - ', colTypes)
	wordLists = load_lists(colTypes)
	tbl = []
	tbl.insert(0, hdr) # column headers
	for r in range(0,rows):
		thisRow = []
		txt = ''
		for c in range(0, cols):
			if colTypes[c] == 'INT':
				txt = str(random_int())
			else:
				for lst in wordLists:
					if lst['name'] != 'INT':
						if lst['name'] == colTypes[c]:
							txt = get_rand_text_from_list(lst['lst'])
			thisRow.append(txt)
		tbl.append(thisRow)
	return tbl

def show_table(tbl):
	for row in tbl:
		txt = ''
		for col in row:
			if type(col) is str:
				txt = txt + col + ', '
			else:
				txt = txt + str(col) + ', '
		print(txt)


def save_table(tbl, fname, delim=',', quote='"'):
	f = open(fname, "wt")
	for row in tbl:
		txt = ''
		for col in row:
			if type(col) is str:
				txt = txt + quote + col + quote + delim
			else:
				txt = txt + quote + str(col) + quote + delim
		txt = txt + '\n'
		f.write(txt)

def get_rand_text_from_list(lst):
	try:
		return lst[random.randrange(0, len(lst))]
	except:
		return 'ERROR getting list'
	
def fill_colList_blanks(partialCols, numRequiredCols):
	colWord = []
	num = 0
	for c in range(0, numRequiredCols):
		try:
			tpe = partialCols[num]
		except:
			tpe = 'STRING'
		#print('num = ', num, ' type = ', tpe)
		if tpe == '': 
			tpe = 'STRING'
		colWord.append(tpe)
		num = num + 1
	return colWord

def load_lists(lst):
	# loads a sample of data for each type in lst
	results = []	# will return a lists of dictionarys of lists (yes, that is right)
	lists_to_load = {l for l in lst}	# get unique list of types so only loading them once each
	for tpe in lists_to_load:
		if tpe == 'STRING':
			results.append({'name': 'STRING', 'lst': get_list_string()})
		if tpe == 'WORD':
			results.append({'name': 'WORD', 'lst': get_list_words()})
		if tpe == 'DATE':
			results.append({'name': 'DATE', 'lst': get_list_dates()})
		if tpe == 'PLACE':
			results.append({'name': 'PLACE', 'lst': get_list_places()})
		if tpe == 'PEOPLE':
			results.append({'name': 'PEOPLE', 'lst': get_list_people()})
	return results

def get_list_string():
	lst = []
	for i in range(0,100):
		lst.append(random_letters(10))
	return lst
	
def get_list_words():
	lst = []
	with open(wordList) as f:
		for line in f:
			if random.randrange(1,100) > 90:  # only load 10% of random words
				lst.append(line.strip().replace('_', ' '))
	return lst

def get_list_dates():
	return [i for i in range(1985, 2014)]

def get_list_places():
	lst = []
	with open(places) as f:
		for line in f:
			lst.append(line.split(',')[2].strip().strip('"').title())
	return lst

def get_list_people():
	lst = []
	with open(names) as f:
		for line in f:
			lst.append(line.split(',')[0].title())
	return lst
	
			
if __name__ == '__main__':
    TEST()	
	
