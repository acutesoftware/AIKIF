#!/usr/bin/python3
# -*- coding: utf-8 -*-
# text_tools.py 


import os
import sys
import pprint

def TEST():
    print(parse_text_to_table('aaa,bdsdsbb,cfe\nAAA,BB,C\na,bb,ccc\n'))
    tab_data = """animal	bird	dove		
animal	bird	duck		
animal	fish	salmon		
animal	mammal	human		
animal	mammal	lion		
animal	mammal	pig		
plant	flower	rose		
plant	tree	apple	
plant	tree	lemon	
life	plant	vegetable	herb	mint	
life	plant	vegetable	herb	rosemary	
life	plant	vegetable	herb	sage	
life	plant	vegetable	pea		
life	plant	vegetable	potato		"""

    tbl = parse_text_to_table(tab_data)
    print(tbl)
    save_tbl_as_csv(tbl, 'test_csv_output_auto.csv')
    
    # no do a manual split
    t3 = parse_text_by_col_pos('aaa,bdsdsbb,cfe\nAAA,BB,C\na,bb,ccc\n', [3,3,3])
    #save_tbl_as_csv(t3, 'test_tbl3.csv')
    
def parse_text_to_table(txt):
    """
    takes a blob of text and finds delimiter OR guesses 
    the column positions to parse into a table.
    input:   txt = blob of text, lines separated by \n
    output:  res = table of text
    """
    res = []                # resulting table
    delim = identify_delim(txt)
    print('delim = _' + delim + '_')
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
    print('lines[0] = ', lines[0])
    for col_pos, ch in enumerate(lines[0]):
        #print('col_pos, ch, prev_ch = ', col_pos, ch, prev_ch)
        if _is_white_space(ch) is False and _is_white_space(prev_ch) is True:
            res.append(col_pos)
        prev_ch = ch
    res.append(col_pos)
    print('identify_col_pos ' , res)
    
    return res

    
def _is_white_space(ch):
    if ch in [' ', '\t']:
        return True
    else:
        return False
        
def save_tbl_as_csv(t, fname):
    with open(fname, 'w') as f:
        for row in t:
            for col in row:
                f.write('"' + col + '",')
            f.write('\n')
        
        
def parse_text_by_col_pos(txt, fixed_split):
    tbl = []
    lines = txt.split('\n')
    #print('reading ' + str(len(lines)) + ' in blob size ' + str(len(txt)))
    #print('fixed_split = ' , fixed_split)
    for line in lines:
        if line.strip('\n') != '':
            cols = []
            prev_spacing = 0
            for cur_pos in fixed_split:
                cols.append(line[prev_spacing:cur_pos])
                prev_spacing = cur_pos
            cols.append(line[cur_pos:])
            #print('cols = ', cols)
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
    count_by_row = []
    max_cols = 0
    max_rows = 0

    possible_delims = _get_dict_char_count(txt)  # {'C': 3, 'a': 4, 'b': 5, 'c': 6, ',': 6, 'A': 3, '\n': 3, 'B': 3})
        
    delim = max(possible_delims.keys(), key=(lambda k: possible_delims[k]))
    print('delim = ', delim)
    
    """
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
   
def keywithmaxval(d):
     """ 
        
         a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

   
TEST()