# generateTestData.py		written by Duncan Murray 17/4/2014


import os
import random
import binascii
import string

root = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "..")
dat_fldr = root + os.sep + 'data' 
names =    dat_fldr + os.sep + 'ref' + os.sep + 'names.csv'  # via http://www.cs.princeton.edu/introcs/data/names.csv
places =   dat_fldr + os.sep + 'core' + os.sep + 'LOCATION_WORLD.CSV'  # use fileMap GETONTOLOGY
wordList = dat_fldr + os.sep + 'ref' + os.sep + 'nounList.txt'

def TEST():
    print('generateTestData.py')
    print('Creates random data and strings in various formats')
    print('Random Strings....\n  ', random_hex_string(20), '\n  ', random_letters(50))
    print('Random Block ....')
    print(random_block(30,11))
    print('Data Table ....')
    colLabel = ['DATE', 'name', 'password', 'Born',  'Quote', 'Score']
    colTypes = ['DATE', 'PEOPLE', 'STRING', 'PLACE', 'WORD',  'INT']
    tbl = random_table(6,5, colTypes, colLabel)
    show_table(tbl)
    save_table(tbl, '..//..//data//temp//test123.csv')
    print('password generator = ', generate_password(10))
    
def random_int(min_v=0, max_v=100):
    return random.randrange(min_v, max_v)
    
def random_letters(sze=20):
    lst = [random.choice(string.ascii_letters + string.digits) for _ in range(sze)]
    return "".join(lst)

def generate_password(sze=18):
    if sze < 8: sze = 8
    return random_letters(sze-3).lower() + str(random_int(10,99)) + random_letters(sze-6).upper()
    
def random_hex_string(sze=30):
    return binascii.b2a_hex(os.urandom(sze))
    
def random_block(cols=40, rows=5):
    return ''.join([random_letters(cols) + '\n' for _ in range(0,rows)])

def random_table(cols=3, rows=10, colSpecs, hdr):
    # verify the colSpecs required and assign defaults to empty sets
    colTypes = fill_colList_blanks(colSpecs, cols)
    print('Generating columns - ', colTypes)
    wordLists = load_lists(colTypes)
    tbl = []
    tbl.insert(0, hdr) # column headers
    for _ in range(0,rows):
        thisRow = []
        txt = ''
        for c in range(0, cols):
            if colTypes[c] == 'INT':
                txt = str(random_int())
            elif colTypes[c] == 'STRING':
                txt = random_letters()
            else:
                for lst in wordLists:
                    if lst['name'] != 'INT':
                        if lst['name'] == colTypes[c]:
                            txt = get_rand_text_from_list(lst['lst'])
            thisRow.append(txt)
        tbl.append(thisRow)
    return tbl

def show_table_OLD(tbl):
    for row in tbl:
        txt = ''
        for col in row:
            if type(col) is str:
                txt = txt + col + ', '
            else:
                txt = txt + str(col) + ', '
        print(txt)

def show_table_BETTER(tbl):
    for row in tbl:
        print(''.join([col + ', ' if type(col) is str else str(col) + ', ' for col in row]))

def show_table(tbl):
    print('\n'.join(','.join([col if type(col) is str else str(col) for col in row]) for row in tbl))

def save_table(tbl, fname, delim=',', qu='"'):
    with open(fname, "wt") as f:
        f.write('\n'.join(delim.join([qu + col + qu if type(col) is str else qu + str(col) + qu for col in row]) for row in tbl))

def get_rand_text_from_list(lst):
    return lst[random.randrange(0, len(lst))]
    
def fill_colList_blanks(partialCols, numRequiredCols):
    colWord = []
    num = 0
    for _ in range(0, numRequiredCols):
        tpe = partialCols[num]
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
        if tpe == 'STRING2':
            results.append({'name': 'STRING', 'lst': get_list_string(40)})
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

def get_list_string_OLD():
    lst = []
    for _ in range(0,100):
        lst.append(random_letters(10))
    return lst

def get_list_string(num = 40):
    return [random_letters(num) for _ in range(0,100)]
    
def get_list_words_OLD():
    lst = []
    with open(wordList) as f:
        for line in f:
            if random.randrange(1,100) > 90:  # only load 10% of random words
                lst.append(line.strip().replace('_', ' '))
    return lst
    
def get_list_words():
    with open(wordList) as f:
        return [line.strip().replace('_', ' ') for line in f if random.randrange(1,100) > 90]

def get_list_dates():
    return [i for i in range(1985, 2014)]

def get_list_places():
    with open(places) as f:
        return [line.split(',')[2].strip().strip('"').title() for line in f]

def get_list_people():
    with open(names) as f:
        return [line.split(',')[0].title() for line in f]
    
            
if __name__ == '__main__':
    TEST()	
    
