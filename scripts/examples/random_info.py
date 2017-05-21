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
    prj_random = prj.Project(name='Random Information Request', desc=desc, fldr=proj_fldr)
    
    # add sources of data
    prj_random.add_source('Root Ontology', os.path.join(src_fldr, 'data','ref', 'ontology.yaml'))
    prj_random.add_source('Toolboxes', os.path.join(src_fldr, 'data','ref', 'toolbox.csv'))
    
    
    # parse the request for possible toolboxes to use based on local ontology
    keywords = []
    for s in prj_random.data_sources:
        with open(s[1], 'r') as f:
            for line in f:
                print(s[1], ' = ' , line)
                for word in line:
                    keywords.append(word)
    
    # a. split request into words
    # b. lookup local ontology of words to concepts
    # c. lookup toolboxes that match the concepts
    print(list(set(keywords)))
    # test the matching toolboxes on the source data
    # a. run the test on each toolboxes
    # b. compare test results and attempt to rank results
    
    
    all_projects = prj.Projects()
    all_projects.add_ontology('researcher')
    all_projects.add_project(prj_random)
    
    
    print(prj_random)

if __name__ == '__main__':
    main()


