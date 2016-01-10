#!/usr/bin/python3
# -*- coding: utf-8 -*-
# res_core_data_mthd2.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" ) 
sys.path.append(root_folder)
import core_data as mod_core

def get_method(fname):
    """
    returns a description in RST for the research paper
    """
    txt = 'Method 2 - Drill Up / Drill down\n'
    txt += '---------------------------------------\n\n'
    txt += 'Data statements can be expanded (drill down)\n'
    txt += 'and overviewed (drillup) using semi-manual process\n'
    txt += 'to build a tree/graph\n\n'
    return txt
    
def get_results(fname, dat):
    append_rst(fname, '\nMethod 2: running source data ' + dat + ' .... \n')
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