#!/usr/bin/python3
# -*- coding: utf-8 -*-
# res_core_data_NOTES.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  + os.sep + "aikif"  ) 
sys.path.append(root_folder)
import core_data as mod_core

fname = 'res_core_data.rst'

data_files = ['test1.dat', 'test2.dat']

def main():
    """
    This generates the research document based on the results of 
    the various programs and includes RST imports for introduction
    and summary
    """
    print("Generating research notes...")
    if os.path.exists(fname):
       os.remove(fname)
    append_rst('================================================\n')
    append_rst('Comparison of Information Aggregation Techniques\n')
    append_rst('================================================\n\n')
    append_rst('.. contents::\n\n')
       
    # import header
    append_rst(open('res_core_data_HEADER.rst', 'r').read())
    
    # call programs
    append_rst('Method 1 - Ontological Mapping\n')
    append_rst('---------------------------------------\n\n')
    import res_core_data_mthd1
    
    for dat in data_files:
        res_core_data_mthd1.run(fname, dat)
    
    append_rst('\n\n')
    
    # import footer
    append_rst(open('res_core_data_FOOTER.rst', 'r').read())    
    print("Done!")
    
def append_rst(txt):
    with open(fname, 'a') as f:
        f.write(txt)
    
main()