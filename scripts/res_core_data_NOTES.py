#!/usr/bin/python3
# -*- coding: utf-8 -*-
# res_core_data_NOTES.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  + os.sep + "aikif"  ) 
sys.path.append(root_folder)
import core_data as mod_core

def main():
    """
    This generates the research document based on the results of 
    the various programs and includes RST imports for introduction
    and summary
    """
    print("Generating research notes...")

    # import header
    
    # call programs
    import res_core_data_mthd1
    res_core_data_mthd1.main()
    
    # import footer
    
    print("Done!")
    

main()