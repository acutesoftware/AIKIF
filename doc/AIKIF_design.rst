
====================
AIKIF Design
====================

Last updated 28-May-2015
AIKIF Dev version 0.0.10

This document is a scratch pad area for design notes during the development of AIKIF

.. contents::



Design Overview 
---------------


As areas are completed, the contents will be copied to a users manual

*tags for progress are*

[unresolved]  = not sure how to do this
[in progress] = work may have started but early stages
[testing]     = key parts developed, testing results
[completed]   = tests passed and contents copied to users manual / ext paper


Key Concepts
``````````````


- create data structures to hold information

- define mappings to populate data structures

- define / use toolbox to populate data

- build agents to collect and aggregate

- optional build environments for test areas  (eg File System?)

- build controller to manage agents (currently tools.py)

- monitor and update on web interface and via collection agents / mappers


The key principle here is along the lines of “Reproducible Research”
Everything is defined , coded and run *by* the computer rather than you doing it.

This way all results can be re-run at any stage

========================
Logging
========================

This is the main part of AIKIF and the idea is to be able to log any level of detail such as

- high level events (Christmas Party)

- local events (buy milk)

- detailed project info (meeting for projectX on Thursday)

- low level functions (eg iterations of a genetic algorithm)

Logging Events
-----------------

The main program is aikif/cls_log and at the moment this simply appends to a text file.


The main methods of the cls_log.py are below

.. code:: python

    class Log:
        def __init__(self, fldr):
        def record_source(self, src, prg=''):
        def record_process(self, process, prg=''):
        def record_command(self, cmd, prg=''):
        def record_result(self, res, prg=''):

This is used as follows

.. code:: python

    import aikif.cls_log as mod_log

    mylog = mod_log.Log(test_fldr)
    mylog.record_process('test', 'hello - recording process')
    mylog.record_command('test', 'hello - recording command')
    mylog.record_source('test', 'hello - recording source')
    mylog.record_result('test', 'hello - recording result')



Log aggregation [in progress]
------------------------------

To do the log aggregation run the command

.. code:: python

mod_log.LogSummary(self.mylog, test_fldr)

This currently produces a simple count by session ID, but will need to extract key events from the data.


Log Watchpoints
----------------
Watchpoints can be set for any project to monitor for specific events, such as success in a genetic algorithm 

**Key Events to Extract**
Depending of the type of log file, you can do the following

find max/min results and show parameters used for that run
find the best run (eg solvers)
find the shortest / longest / average run time for a session
determine whether run in DEV / PROD (based on folder from config and location of libraries)

===========================
Mapping and Business Rules
===========================

The mapping class contains the business rules engine to control how information is passed


Mapper 
---------------


Mapper.py will be the main method to read the rules from CSV (or YAML) and apply them

A domain is a collection of rules and information that makes it easier to manage for humans entering the data. These include concepts such as ‘study, work, play’ or concrete things like ‘small business’, plumber, write a play, do food shopping.

A domain can get based on other domains so that it uses those rules and information - there can be many to many links, and collisions are listed and must be overridden. e.g. Plumber derives from Tradeskill and Small business




Mapping Process
``````````````````````
So how will this actually work? Some scenarios below:

Automatic data reading
 - read a bunch of CSV or data files, and use the column names and content to generate mapping rules (by linking the column names to standard ontology_colums)
    for each file
        create_map_from_rule
        for each map
            process_map
            


Mapping Functions
``````````````````````
This section has notes on possible functions used in the mapping module - some currently in development but still haven't decided on correct approach.


create_map_from_file
        reads the data_filename into a matrix and calls the main
        function '' to generate a .rule file based on the data in the map
        
        For all datafiles mapped, there exists a .rule file to define it



Mapping Hierarchies
``````````````````````

physics - rules that SHALL be obeyed according to natural law (eg drop something -> it will fall)

law - rules that are governed by law. e.g. All sales must be reported to IRS / ATO

generic - generic laws, eg Emails flagged spam > move to spam folder

profession specific - eg Software developers -> emails from RegNow are sales, carpenters -> profit = sale - (cost_wood + time + tool_wear)

situational - e.g. Work mode -> hide Reddit, Game mode -> turn off notifications, Sales mode -> ringer volume loud

[YOUR_MAPPING] = add all own mappings which if duplicated, override above



Domains (Ontology Examples) [unresolved]
-----------------------------------------

Originally, the plan was  to have everything mapped that you do in your world. A full ontology contains roughly 98% of items that do not appear in your horizon, so rather than link to an external Ontology at this stage, there will be a local Ontology you can modify for your own use.

TODO = think about a local ontology - look at the original ones

Core Domains
``````````````

These are generic core domains that many other things are based on - they have presetup rules so you dont need to manually add everything.

Note that for these domains it might be easier to extract data from big ontology rather than type it all in

*Business* - the act of running a business to make a profit

*Project* - doing something non trivial, pretty much everything can be a project

*Student* - the act of studying something to learn, test yourself, apply it, put on resume

*Worker* - A job. ie learning, using and implementing a tradeskill or degree to make money

*Materials* - things like wood, pipe, hard disk space that are needed to do a Task

*Tools* - anything that is needed or will help do a task

*Tradeskill* - a recognised group of skills, such as woodworking, plumber, programmer the uses physical tools and materials to produce things

*Task* - in instance of a job to do - may involve materials, special tradeskills

*Play* - the act of relaxing. This is here to specify methods such as turn off phone, book holidays, close emails

*Methods* - functions that actually do something, which can be automated logged. Initially most methods are manual with links to doco, but it is still important to link them here so that they can be tracked on the web application and logged. In the future as methods are broken down you will be able to implement with python OR outsource to other people

Domain - Small business
``````````````````````````````

see examples in aikif - this is sort of a ROOT domain which many other things can be derived from

goal = make money, build reputation, sell business

how to get to the goal?

plan = build products, get customers, make sales, reduce costs

tasks (linked to goals)

build products -> research competition, work out demand, prototype, test, manufacture

get customers -> plan campaign, write flyers, build website, social media, cold calling

make sales ->

reduce costs -> rank expenses


methods (these are ACTUAL things the AI knows how to do which can assist automation)
Note that initially ALL the methods will default to ‘manual’ with a link to documentation, but eventually in some domains the automation rate can be reasonable (eg software deployment, data quality checking, estimating and quoting on woodwork jobs


tables (info) - this is where you store [LINKED to ontologies] information for your domain

Domain - Graphic Designer
``````````````````````````````

derives from small business

derives from artist

Domain - Carpenter
`````````````````````````````

derives from small business

derives from tradeskill


Bias [unresolved]
------------------------------

The Bias network has weightings based on sources which determine the probable accuracy of the source data

BIAS Sources

How should the sources of data be mapped / ranked?

Should there be a bias network for all people or groups of people

If groups - who decides on the group boundaries

========================
Agents and Environments
========================

Agents [testing]
------------------------------

Agents are run to do collection and aggregation of source data and can be used to manage any external process (ie call your own software)



Base Agent Class
``````````````````````

The base agent code has the following methods

.. code:: python

    class Agent(object):
        """
        Class for Agents in AIKIF, all agents base class this
        """
        def __init__(self, name='',  fldr='', running=False):
        def __str__(self):
        def start(self):
        def do_your_job(self):
        def stop(self):
        def check_status(self):
        def report(self):

You need to subclass the methods do_your_job and optionally others such as check_status



Sample Agents
``````````````

The explore agent looks like the following

.. code:: python

    class ExploreAgent(agt.Agent):
        """
        agent that explores a world (2D grid)
        """
        def __init__(self, name,  fldr, running, LOG_LEVEL):
            agt.Agent.__init__(self, name,  fldr, running)
            self.LOG_LEVEL = LOG_LEVEL
            self.num_steps = 0
            self.num_climbs = 0

        def set_world(self, grd, start_y, start_x, y, x):
            """
            tell the agent to move to location y,x
            """
        def do_your_job(self, *arg):
    # code to actually do stuff

        def show_status(self):
        # code to show agent status


Testing an Agent
``````````````````````

The following code shows how to start and stop agents

.. code:: python

    myAgent = Agent('TEST Agent', os.getcwd(), True)  # auto run immediately
    manualAgent = Agent('manual', os.getcwd(), False)  # initialises in stopped status
    manualAgent.start()
    manualAgent.stop()
    print(manualAgent.check_status())
    print(manualAgent.report())





Environments [testing]
------------------------------
This is a data structure / parameter set which allows agents to run in worlds

They contain methods to self generate randomly so you can create a set of worlds with different layouts / parameters and simulate the agents running in them.


Sample Environments
``````````````````````

 - Location based (see World example)
This is a simple grid world used to generate a random terrain to allow agents to explore it.

It has no functionality apart from generating itself from random data, loading and saving maps



- Parameter based (see Happiness example)
This is a toy sample and does not have an actual structure for the environment - it is simple a set of parameters used to see how “happy” types of people would be in that instance of the world.



Process for Environments
``````````````````````````````
As part of the environment module there can be one or many helper classes for the environment and these are setup to run agents or simulations in the world.

In the World.py environment here is a  WorldSimulation class which takes a World object and a list of agents (of type Agent) and needs a *run* method to allow the agents to interact with the world

.. code:: python

    class WorldSimulation(object):
        """
        takes a world object and number of agents, objects
        and runs a simulation

        """
        def __init__(self, cls_world, agent_list, LOG_LEVEL):
            self.world = cls_world
            self.agent_list = agent_list
            self.LOG_LEVEL = LOG_LEVEL

        def run(self, num_runs, show_trails, log_file_base):
            """
            Run each agent in the world for 'num_runs' iterations
            Optionally saves grid results to file if base name is
            passed to method.
            """

It is not required to have a class [YourWorld]Simulation() as part of the environment but it makes it simpler to manage the process.

Running Agents in Environments [testing]
``````````````````````````````````````````````

An environment can be used as follows:

.. code:: python

    # see - aikif.examples.world_generator.py
    import aikif.environments.worlds as my_world
    import aikif.agents.explore.agent_explore_grid as agt

    myWorld = my_world.World( height, width, ['.','X','#'])
    myWorld.build_random( num_seeds, perc_land, perc_sea, perc_blocked)
    agt_list = []
    for agt_num in range(0,num_agents):
        ag = agt.ExploreAgent( 'exploring_agent' + str(agt_num),  log_folder, False, LOG_LEVEL)
        start_y, start_x = myWorld.grd.find_safe_starting_point()
        ag.set_world(myWorld.grd, start_y, start_x, target_coords[0], target_coords[1])
        agt_list.append(ag)
    sim = my_world.WorldSimulation(myWorld, agt_list, LOG_LEVEL)
    sim.run(iterations, 'Y', log_folder + '\\agt_run')
    sim.world.grd.save('test_world_traversed.txt')


===========================
AI Management
===========================
Section to show how AI applications can use the AIKIF
    
This should centre around having an algorithm such as machine learning which attempts to solve a question.

Start by specifying the problem and its data sources, then setup AIKIF to call the AI with parameters to get logs.


.. code:: python

    proj='ML_solver1'
    source='c:\data\'
    algorithms=['cluster', 'multivariate']

    lg = aikif.Project('ML_solver1')
    lg.add_source('Your source')
    lg.add_param(type='algorithm', name='cluster')
    lf.add_param(type='X', 54)
    lf.add_param(type='Y', 4.2)

    t = aikif.toolbox.Toolbox('c:\ml_solver.py')   # your AI

    lg.run(t)    # run the AI with the parameters and results are logged

    lg.parse_logs('success')  # extract logs saying success


The results can be tracked on the web interface in a nice summary    
    
    
    
===================
Memory / Knowledge
===================

This section has thoughts (not yet implemented) on how to handle memory and transfer of knowledge from information and raw data.

High Level Processes  [unresolved]
-----------------------------------

List of the processes showing how information is loaded at various stages.

Not all data is loaded at once, and it is expected that agents run at various times to refresh certain sections.

The wakeup/learn areas are only set out this way to allow for flexible options for the future - this application will not actually do any learning.

Startup (Wake up)
``````````````````````

identify context
check self - folders
load last short term memory

Read (loading selected files to memory)
``````````````````````````````````````````````

load short term memory from disk cache to reddis


Learn ( use short term memory to find new facts) [unresolved]
``````````````````````````````````````````````````````````````

how to decide what memory is useful?

might leave this out - getting out of scope here. The goal of AIKIF it to provide data structures and processes to manage information, not to actually learn.



Sleep (Save useful short term memory to disk) [unresolved]
``````````````````````````````````````````````````````````````

When the sleep function is called this saves data in reddis to disk.

What is defined as useful
list of tasks done during day
location of all files, including temp files
meaning / aggregate result of day
KEY parts from logfiles (any peaks, max/min, patterns)

What is defined as not useful
- duplicate raw data from temporary files


Data Structures for Memory [in progress]
-----------------------------------------

How is the information stored

Short Term Memory (REDDIS)
``````````````````````````````

Mapper list
knowledge table
ref tables
goals


Long Term Memory (DISK) [in progress]
``````````````````````````````````````

RDF Files
CSV files
Databases


==============
Outputs
==============

What can you automatically create when you have all this information and meta data stored in AIKIF?

Overview
-------------

This section describes how various outputs are generated - see AIKIF_requirements.rst for full list of requirements



PIM Outputs
---------------------

Diary
``````````````

Looks at the events logs

groups by 15 minute intervals

uses context to identify location

aggregates and adds diary entries to new table
5/5/2015 - 10am 2hrs, Meeting with John about design
7/7/2015 -  2pm 30min, released AIKIF v0.0.12 to pypi

TODO lists
``````````````

shows tasks for you (or team member) for all projects with priority

can include estimations and suggested sequence (if you use the ai_search.py planner)

Contacts Lists
``````````````

toolbox method to read emails, phone, document lists of contacts

agent to get distinct names / emails / nicknames and add to list of alias

build contacts database

updates are kept as new datasets, so database can be reproduced



Project Management Outputs
-------------------------------

Project Plan
``````````````
shows the proposed list of tasks in order for any project


Timesheets
``````````````

Looks at the events logs

groups by 15 minute intervals

uses project mappings to identify projects



Other Outputs
--------------------------

Automating Database Updates [testing]
``````````````````````````````````````````````

"Add country region from UN database to our customer address dimension"

- find agent - looks for data table on regions with countries
- toolbox to download and save data
- mapping to update dimension based on UN data
- schedule to do routine updates

(AND - it should generate ALL of this automatically, allow you to review, then just do it)

Routine Computer Tasks [testing]
``````````````````````````````````````

Backup my working documents to the server each week

- agent to find working doc folder (needs to be a MAPPING set of rules)
    - if file modified date less than week old, backup folder TREE
    - if folder NAME == project_NAME then backup folder TREE



Resume
````````````````````````

  - list of events where you worked
  - list of courses online you did
  - high level summary of study plan
  - employement contacts

You can also run tasks such as "Tailor my resume for [work_type]” which shows those work experiences first where overlaps occur

.. code:: python

    p = aikif.Project('MyResume')
    skills = p.add_table('skills', ['skill', 'comment'])
    work = p.add_table('work history', ['date_start','date_end', 'company', 'task'])

    # populate company history by looking at emails SENT address
    work.populate(aikif.core_data('SELECT min(date), max(date), from_address FROM aikif_pim_email'))

    # populate skills based on what you spend time on
    skills.populate(aikif.core_data('SELECT distinct languages FROM aikif_pim_github'))

    # add skills based on your github repos
    skills.populate(aikif.core_data('SELECT TOP 10 projects FROM aikif_pim_pc_usage'))

    # format the resume
    p.format(aikif_template_resume, 'C:\my_resume.rst')


