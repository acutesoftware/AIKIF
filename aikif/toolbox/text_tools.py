#!/usr/bin/python3
# -*- coding: utf-8 -*-
# text_tools.py 

def parse_text_to_table(txt):
    """
    takes a blob of text and finds delimiter OR guesses 
    the column positions to parse into a table.
    input:   txt = blob of text, lines separated by \n
    output:  res = table of text
    """
    res = []                # resulting table
    delim = identify_delim(txt)
    if delim == '' or delim == ' ':
        fixed_split = identify_col_pos(txt)
        if fixed_split == []:
            res = []
        else:
            res = parse_text_by_col_pos(txt, fixed_split)
    else:
        res = parse_text_by_delim(txt, delim)
        
    
    return res

def identify_col_pos(txt):
    """
    assume no delimiter in this file, so guess the best 
    fixed column widths to split by
    """
    res = []
    #res.append(0)
    lines = txt.split('\n')
    prev_ch = ''
    for col_pos, ch in enumerate(lines[0]):
        if _is_white_space(ch) is False and _is_white_space(prev_ch) is True:
            res.append(col_pos)
        prev_ch = ch
    res.append(col_pos)
    return res

    
def _is_white_space(ch):
    if ch in [' ', '\t']:
        return True
    else:
        return False


def load_tbl_from_csv(fname):
	"""
	read a CSV file to list without worrying about odd characters
	"""
    import csv

    rows_to_load = []
    
    with open(filename, 'r', encoding='cp1252', errors='ignore') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',' )

        reader = csv.reader(csvfile)            

        rows_to_load = list(reader)
    
    return rows_to_load
    	
        
def save_tbl_as_csv(t, fname):
    with open(fname, 'w') as f:
        for row in t:
            for col in row:
                f.write('"' + col + '",')
            f.write('\n')
        
        
def parse_text_by_col_pos(txt, fixed_split):
    tbl = []
    cur_pos = 0
    lines = txt.split('\n')
    for line in lines:
        if line.strip('\n') != '':
            cols = []
            prev_spacing = 0
            for cur_pos in fixed_split:
                cols.append(line[prev_spacing:cur_pos])
                prev_spacing = cur_pos
            cols.append(line[cur_pos:])
        tbl.append(cols)
    return tbl
    
def parse_text_by_delim(txt, delim):
    tbl = []
    lines = txt.split('\n')
    for line in lines:
        if line.strip('\n') != '':
            tbl.append(line.split(delim))
    return tbl
    
def _get_dict_char_count(txt):
    """
    reads the characters in txt and returns a dictionary
    of all letters
    """
    dct = {}
    for letter in txt:
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1
    return dct
 

def identify_delim(txt):
    """
    identifies delimiters and returns a count by ROW
    in the text file as well as the delimiter value (if any)
    The delim is determined if the count of delims is consistant
    in all rows.
    """
    possible_delims = _get_dict_char_count(txt)  # {'C': 3, 'a': 4, 'b': 5, 'c': 6, ',': 6, 'A': 3, '\n': 3, 'B': 3})
        
    delim = max(possible_delims.keys(), key=(lambda k: possible_delims[k]))
    
    """
    count_by_row = []
    max_cols = 0
    max_rows = 0

    lines = txt.split('\n')
    for line in lines:
        if len(line) > max_cols:
            max_cols = len(line)
        this_count = _get_dict_char_count(line)
        count_by_row.append(this_count)
        print('line = ', line)
        print('count_by_row = ', this_count)
        max_rows += 1

    # make a matrix
    matrix = [[0 for i in range(max_rows)] for j in range(max_cols)]
    pprint.pprint(matrix)
    """

    
    return delim
   
def fingerprint(txt):
    """
    takes a string and truncates to standard form for data matching.
    Based on the spec at OpenRefine 
    https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth#fingerprint
    - remove leading and trailing whitespace
    - change all characters to their lowercase representation
    - remove all punctuation and control characters
    - split the string into whitespace-separated tokens
    - sort the tokens and remove duplicates
    - join the tokens back together
    - normalize extended western characters to their ASCII representation (for example "gödel" → "godel")  
    
    """
    raw_text = txt.upper() #.strip(' ').replace('\n','')
    tokens = sorted(list(set(raw_text.split(' '))))
    #print('tokens = ', tokens)
    
    res = ''.join([strip_nonalpha(t) for t in tokens])
    return res
 
def strip_nonalpha(txt):
    """
    removes non alpha characters from string
    TODO - replace UniCode chars with standard replacements
    res = ''
    for c in txt:
        if c.isalpha():
            res += c
    return res
    """
    
    return ''.join([c for c in txt if c.isalpha()]) 
    
 
def is_match(txt1, txt2):
    """
    see if there is a match based on fingerprint
    """
    if fingerprint(txt1) == fingerprint(txt2):
        return True
    else:
        return False

 
 
def get_date_from_str(datestring):
	"""
	find a date from string
	"""

	import dateutil.parser
	return dateutil.parser.parse(datestring)
 
 
