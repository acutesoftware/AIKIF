# example.py

import os


#Step 1 - configure AIKIF
import aikif.config as cfg
cfg.set_folder = os.getcwd()	# sets folder for saving, and creates sub folders (log, raw, etc)
#cfg.set_password(input('enter password'))  # not yet implemented


#Step 2 - define your working environment (personal ontology)
import aikif.project as prj
my_projects = prj.Projects()
my_projects.add_ontology('Business')	# options are student, business, worker, tradesman, researcher, software_dev
my_projects.add_ontology('software_dev')
my_projects.add_ontology('researcher')


# Step 3 - setup your projects with goals / targets


proj_dev_aikif = prj.Project('AIKIF development')   # development project
proj_script_mgt = prj.Project('Script management')  # logging of projects
proj_acute = prj.Project('Acute Software Business') # business project
proj_research = prj.Project('Personal Research')    # study / research project

proj_dev_aikif.add_goal('REL_ALPHA', 'Milestone - Alpha Release', due_date='2015/06/01', priority='High')
proj_dev_aikif.add_goal('REL_BETA', 'Milestone - Beta Release', due_date='2016/01/01', priority='High')
proj_dev_aikif.add_goal('TEST','User testing', due_date='2015/06/01', priority='High')

proj_script_mgt.add_goal('SCRIPT_LOG', 'Log of script runs')

my_projects.add_project(proj_acute)
my_projects.add_project(proj_script_mgt)
my_projects.add_project(proj_acute)
my_projects.add_project(proj_research)

# a new project can be defined directly into Projects but shown here after for simplicity
my_projects.add_project(prj.Project(name='Another Project', desc='created adhoc'))

another_project = my_projects.get_by_name('Another Project')

print(another_project)


# Step 4 - define your data sources

proj_script_mgt.add_source('src1', 'http://www.blah')
proj_script_mgt.add_source('src2', 'http://www.blah2')


# Step 5 - setup your processes (how data is updated)
import aikif.toolbox.Toolbox as mod_tool
tools = mod_tool.Toolbox()

tools.add({'name':'email collection', 'file':'agent.gather.agent_email', 'interval':'Daily'})
tools.add({'name':'file download', 'file':'toolbox.download', 'interval':'On call'})
tools.add({'name':'file copy', 'file':'cls_file.copy'})

tools.add({'name':'script1', 'PC':'linux_main', 'file':'/usr/bin/script1', 'log':'script1.log'})
tools.add({'name':'script2', 'PC':'ent_win8', 'file':'C:\\script\\run.BAT', 'log':'script2.log'})
tools.add({'name':'script3', 'PC':'linux_NAS', 'file':'/user/home/backup', 'log':'script3.log'})

#tools.schedule('Activate')


# Step 6 - monitor and manage via web app

# What do you get out of documenting all these processes?
# Keep track of projects
# All projects are visible and other team members can find the source years later

# Auto-Generated Documentation
# Because all the pertinant info is stored in the database, it is a simple process to extract this into a series of wiki pages for your project

# Auto-Generated Project Reports
# You can see the progress on any report

# Email alerts when things stop
# If a process stops you get an email

# Simple search across ALL your information
# With a copy of everything locally, a rich search is available


print(' Start web server via : GO_WEB_AIKIF')

