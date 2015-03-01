# AIKIF_project.py      written by Duncan Murray 1st-Mar-2015

import os
import sys
import aikif.cls_log as mod_log
import aikif.project as mod_prj
import aikif.dataTools.cls_datatable as mod_dt



def main():
    """
    This is an example of project documentation using AIKIF
    It documents the project itself, including requirements, 
    design, test, goals, 
    
    """
    print('Initialising AIKIF Project...')
    name = 'AIKIF'
    type = 'Software'
    desc = 'Artificial Intelligence Knowledge Information Framework'
    fldr = 'T:\\user\\dev\\src\\python\\AIKIF\\aikif\\examples\\AIKIF_project'
    report_file = fldr + '\\aikif_report.md'
    p = mod_prj.Project(name, type, desc, fldr)
    project_setup(p)

    requirements = mod_dt.DataTable('requirements.csv', ',', col_names=['id', 'dep_id', 'name', 'details'])
    p.log_table(requirements)
    p.record(requirements, '', ['a', 'process data', 'automatically process source files to tables based on rules'])
    p.record(requirements, '', ['b', 'define structures', 'use mappings and ontology to specifiy what to do'])
    p.record(requirements, '', ['c', 'log intent', 'log key events'])
    p.record(requirements, '', ['d', 'methods toolbox', 'implement a set of programs that can be used generically'])

    
    
    
    p.build_report(report_file)
    print('Done...')


def project_setup(p):
    """
    Define the project and add details
    """
    p.add_detail('website', 'http://www.acutesoftware.com.au')
    p.add_detail('email', 'djmurray@acutesoftware.com.au')

 
 
"""
Utility Functions (may be moved to project)
"""
    
    
def read_table():
    """
    
    """
    pass

if __name__ == '__main__': 
    main()