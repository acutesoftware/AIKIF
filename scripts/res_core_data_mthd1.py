#!/usr/bin/python3
# -*- coding: utf-8 -*-
# res_core_data_mthd1.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" ) 
sys.path.append(root_folder)
import core_data as mod_core

def get_method(fname):
    """
    returns a description in RST for the research paper
    
   
    append_rst('Method 2 - Method 2 - Drill Up / Drill down\n')
    append_rst('---------------------------------------\n\n')

    
    
    """
    txt = 'Method 1 - Ontological Mapping\n'
    txt += '---------------------------------------\n\n'
    txt += 'Using an ontology, map the columns in raw data to a set of standard tables\n\n'
    return txt
    
def get_results(fname, dat):
    append_rst(fname, '\nMethod 1: running source data ' + dat + ' .... \n')
    with open(dat, 'r') as f:
        for line in f:
            cols = parse_csv(line)
            print(cols)


def append_rst(fname, txt):
    with open(fname, 'a') as f:
        f.write(txt)
        
        
def parse_csv(txt):
    cols = txt.split(',')
    return cols