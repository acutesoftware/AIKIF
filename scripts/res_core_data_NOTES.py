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

def main():
    """
    This generates the research document based on the results of 
    the various programs and includes RST imports for introduction
    and summary
    """
    print("Generating research notes...")
    if os.path.exists(fname):
       os.remove(fname)
    with open(fname, 'w') as f:
        f.write('================================================\n')
        f.write('Comparison of Information Aggregation Techniques\n')
        f.write('================================================\n\n')
        f.write('.. contents::\n\n')
       
        # import header
        f.write(open('res_core_data_HEADER.rst', 'r').read())
        
        # call programs
        import res_core_data_mthd1
        res_core_data_mthd1.main()
        
        # import footer
        f.write(open('res_core_data_FOOTER.rst', 'r').read())    
    print("Done!")
    

main()