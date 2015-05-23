# coding: utf-8
# project.py	written by Duncan Murray 11/1/2015	(C) Acute Software

class Projects(object):
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
        
 
class Project(object):
    """
    handles the projects in AIKIF, meaning logs the names
    and parameters used for various algorithms.
    """
    def __init__(self, name, tpe='', fldr=None , desc=''):
        self.nme = name
        self.goals = []
        self.data_sources = []
        self.datatables = []
        self.ontology = []
        self.links = []
        self.tasks = []
        self.params = []
        self.fldr = fldr
        self.tpe = tpe
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

    def add_goal(self, goal_id, name, due_date=None, priority=None):
        """
        adds a goal for the project
        """
        self.goals.append([goal_id, name, due_date, priority])
        
    def add_task(self, task_id, name, due_date=None, priority=None):
        """
        adds a task for the project
        """
        self.tasks.append([task_id, name, due_date, priority])
        
    
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

    def add_detail(self, tpe, detail):
        """
        handles the data sources used in projects, mainly as an 
        abstract to call the data sources in /lib and /dataTools
        """
        self.details.append([tpe, detail])

    def add_param(self, task_id, param_key, param_val):
        """
        adds parameters as key value pairs
        """
        self.params.append([task_id, param_key, param_val])
        
    def execute(self):
        """
        executes all automatic tasks in order of task id
        """
        print('running tasks...')
        for t in self.tasks:
            print('task ' + t[1])
    
    def log_table(self, datatable):
        """
        records a list of datatables used in the project
        """
        self.datatables.append(datatable)
    
    def record(self, tbl, tpe, col_data):
        """
        takes a DataTable as param and adds a record
        TODO - log details here
        """
        print(tpe)
        tbl.add(col_data)
        
        
    def build_report(self, op_file, tpe='md'):
        """
        create a report showing all project details
        """
        if tpe == 'md':
            res = self.get_report_md()
        elif tpe == 'rst':
            res = self.get_report_rst()
        else:
            res = 'Unknown report type passed to project.build_report'
        
        with open(op_file, 'w') as f:
            f.write(res)
    
    def get_report_rst(self):
        """
        formats the project into a report in RST format
        """
        res = ''
        res += '-----------------------------------\n' 
        res += self.nme  + '\n'
        res += '-----------------------------------\n\n'
        res += '::\n'
        res += '     ' + self.desc + '\n\n'
        res += '     ' + self.fldr + '\n\n'
        res += '.. contents:: \n\n\n'

        res += 'Overview\n' + '===========================================\n\n'
        res += 'This document contains details on the project : ' + self.nme + '\n\n'
        res += 'TABLES\n' + '===========================================\n\n'
        
        for t in self.datatables:
            res +=  t.name + '\n'
            res += '-------------------------\n\n'
            res += t.format_rst() + '\n\n'
        
        
        
        return res

    def get_report_md(self):
        """
        formats the project into a report in MD format - WARNING - tables missing BR
        """
        res = '#' + self.nme  + '\n'
        res += self.desc + '\n'
        res += self.fldr + '\n'
        
        res += '\n\n##TABLES\n' + '\n'
        
        for t in self.datatables:
            res += '###' + t.name + '\n'
            res += '-------------------------\n'
            res += str(t) + '\n\n'
        
        
        return res

