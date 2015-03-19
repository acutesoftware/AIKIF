# coding: utf-8
# project.py	written by Duncan Murray 11/1/2015	(C) Acute Software

import os
import sys

aikif_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(aikif_dir)

def TEST():
    print('starting project')
    proj_diary = Project(name='Diary', fldr=aikif_dir, desc='Diary database for PIM application')
    proj_diary.add_source('Calendar', aikif_dir)
    proj_diary.add_source('Bookmarks', aikif_dir)
    proj_diary.add_source('File Usage', aikif_dir)
    proj_diary.add_source('PC Usage', aikif_dir)
    proj_diary.add_source('TODO List', aikif_dir)

    print(proj_diary)
 
    my_biz = Project(name='Acute Software', type='business', desc='Custom Software development', fldr='')
    my_biz.add_detail('website', 'http://www.acutesoftware.com.au')
    my_biz.add_detail('email', 'djmurray@acutesoftware.com.au')
    print(my_biz)
    
    
    all_projects = Projects()
    all_projects.add_project(proj_diary)
    all_projects.add_project(my_biz)
    print(all_projects)
    

class Projects():
    """
    handles the ontologies for all your projects to 
    avoid replication of data entry
    """
    def __init__(self):
        self.ontology = []
        self.project_list = []
     
    def __str__(self):
        res = '-- List of All Projects --\n'
        for p in self.project_list:
            res += p.nme.ljust(22) + p.desc + '\n'
            
        return res
    
    def add_project(self, proj):
        self.project_list.append(proj)
    
    def add_ontology(self, name):
        """
        handles the data sources used in projects, mainly as an 
        abstract to call the data sources in /lib and /dataTools
        """
        self.ontology.append(name)
    
    def get_by_name(self, name):
        """ returns an object Project which matches name """
        for p in self.project_list:
            if p.nme == name:
                return p
        return None
        
 
class Project():
    """
    handles the projects in AIKIF, meaning logs the names
    and parameters used for various algorithms.
    """
    def __init__(self, name, type='', fldr=None , desc=''):
        self.nme = name
        self.goals = []
        self.data_sources = []
        self.datatables = []
        self.ontology = []
        self.links = []
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

    def add_goal(self, id, name, due_date=None, priority=None):
        """
        adds a goal for the project
        """
        self.goals.append([id, name, due_date, priority])
        
    def add_task(self, id, name, due_date=None, priority=None):
        """
        adds a task for the project
        """
    
    def add_link(self, src_id, dest_id, src_type='Goal', dest_type='Task'):  
        """
        creates links for the projects, mainly for tasks to goals
        but also for folders to projects
        """
        self.links.append([src_id, dest_id, src_type, dest_type])
        
    def add_source(self, name, location, schedule='Daily', op=''):
        """
        handles the data sources used in projects, mainly as an 
        abstract to call the data sources in /lib and /dataTools
        """
        if op == '':
            op = name + '.log'
        self.data_sources.append([name, location, schedule, op])

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
        res = '#' + self.nme  + '\n'
        res += self.desc + '\n'
        res += self.fldr + '\n'
        
        res += '\n\n##TABLES\n' + '\n'
        
        for t in self.datatables:
            res += '###' + t.name + '\n'
            res += '-------------------------\n'
            res += str(t) + '\n\n'
            print(t)
        
        with open(op_file, 'w') as f:
            f.write(res)
            
        
if __name__ == '__main__':
    TEST()	
    