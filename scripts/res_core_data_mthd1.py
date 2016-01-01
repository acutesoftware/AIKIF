#!/usr/bin/python3
# -*- coding: utf-8 -*-
# res_core_data_mthd1.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder)
import core_data as mod_core

def run(fname, dat):
    append_rst(fname, '- Data File : ' + dat + '\n')
    append_rst(fname, '\nrunning source data ' + dat + ' .... \n\n')
 


def append_rst(fname, txt):
    with open(fname, 'a') as f:
        f.write(txt)