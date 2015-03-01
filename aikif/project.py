# coding: utf-8
# project.py	written by Duncan Murray 11/1/2015	(C) Acute Software

import os
import sys

aikif_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(aikif_dir)

def TEST():
    print('starting project')
    proj_diary = Project('Diary', fldr=aikif_dir, desc='Diary database for PIM application')
    proj_diary.add_src('Calendar', aikif_dir)
    proj_diary.add_src('Bookmarks', aikif_dir)
    proj_diary.add_src('File Usage', aikif_dir)
    proj_diary.add_src('PC Usage', aikif_dir)
    proj_diary.add_src('TODO List', aikif_dir)

    print(proj_diary)
 
    my_biz = Project(name='Acute Software', type='business', desc='Custom Software development', fldr='')
    my_biz.add_detail('website', 'http://www.acutesoftware.com.au')
    my_biz.add_detail('email', 'djmurray@acutesoftware.com.au')
    print(my_biz)


 
class Project():
    """
    handles the projects in AIKIF, meaning logs the names
    and parameters used for various algorithms.
    """
    def __init__(self, name, type='', fldr=None , desc=''):
        self.nme = name
        self.data_sources = []
        self.datatables = []
        self.fldr = fldr
        self.type = type
        self.desc = desc
        self.details = []   # as much info as is needed for project 

    def __str__(self):
        res = ' /---- Project ------------------------------- \n' 
        res += '|  name = ' + self.nme + '\n'
        res += '|  desc = ' + self.desc + '\n'
        res += '|  fldr = ' + self.fldr + '\n'
        res += '\---------------------------------------------\n'
        if len(self.details) > 0:
            res += ':Details:\n'
            for d in self.details:
                res += d[0] + '\t ' + d[1] + '\n'
        if len(self.data_sources) > 0:
            res += ':Data Sources:\n'
            for d in self.data_sources:
                res += d[0] + '\t ' + d[1] + '\n'
        return res
    
    def add_src(self, nme, location):
        """
        handles the data sources used in projects, mainly as an 
        abstract to call the data sources in /lib and /dataTools
        """
        self.data_sources.append([nme, location])

    def add_detail(self, type, detail):
        """
        handles the data sources used in projects, mainly as an 
        abstract to call the data sources in /lib and /dataTools
        """
        self.details.append([type, detail])
    
    def log_table(self, datatable):
        """
        records a list of datatables used in the project
        """
        self.datatables.append(datatable)
    
    def record(self, tbl, type, col_data):
        """
        takes a DataTable as param and adds a record
        TODO - log details here
        """
        tbl.add(col_data)
        
        
    def build_report(self, op_file, type='md'):
        """
        create a report showing all project details
        """
        print('TODO - create report')
        res = '#' + self.nme 
        res += self.desc
        res += self.fldr
        
        res += '\n\n##TABLES'
        
        for t in self.datatables:
            res += str(t)
        
        
        with open(op_file, 'w') as f:
            f.write(res)
        
if __name__ == '__main__':
    TEST()	
    