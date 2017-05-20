#!/usr/bin/python3
# -*- coding: utf-8 -*-
# random_info.py

desc = """This project uses AIKIF to handle a random series of data collection
tasks to solve an everyday problem.

1. Request for solution
Someome has a request to solve an issue
- document details

2. Identify Problem
- map the reqest to a series of information that needs collecting

3. Find Tools to solve the problem
- work out what is needed for a solution

4. Run the tools to find possible solutions
- run the tools and keep all results

5. Test results and pick most likely solution
- for all the test results, find the most appropraite matching result


"""

import os
import sys

proj_fldr = os.getcwd()
src_fldr = os.path.join(proj_fldr, '..','..', 'aikif')
sys.path.append(src_fldr)

import project as prj

import transpose

from dataTools import cls_datatable as dt

def main():

    # define the project
    all_projects = prj.Projects()
    all_projects.add_ontology('researcher')
    prj_random = prj.Project(name='Random Information Request', desc=desc, fldr=proj_fldr)
    all_projects.add_project(prj_random)
    print(all_projects)

    # add sources of data
    
    # parse the request for possible toolboxes to use based on local ontology
    
    
    # a. split request into words
    # b. lookup local ontology of words to concepts
    # c. lookup toolboxes that match the concepts
    
    # test the matching toolboxes on the source data
    # a. run the test on each toolboxes
    # b. compare test results and attempt to rank results
    
    
    
if __name__ == '__main__':
    main()


