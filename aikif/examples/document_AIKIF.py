# document_AIKIF.py written by Duncan Murray 18/4/2014
# All Python Program Statistics
# 26/08/2014 : Files =  110  Bytes =  377221  Lines =  10694  Lines of Code =  8836
# 30/10/2014 : Files =  127  Bytes =  444760  Lines =  12595  Lines of Code =  10409

import sys
import os
sys.path.append('..')

import programs as mod_prg
import config as mod_cfg
import aikif.lib.cls_filelist as mod_fl
import aikif.lib.cls_file as mod_file

def main():
    """
    Example of self documenting (of sorts) code, via aikif.
    Simply call functions like below to build an overview 
    which has metadata automatically updated.
    """
    document_programs(mod_cfg.fldrs['program_path']) 
    
    
    
def document_programs(fldr):
    """
    Document a subset of all programs with purpose (and intent)
    """
    p = mod_prg.Programs('AIKIF Programs', fldr)
    print(fldr)
    
    p.comment('programs.py', 'collects list of aikif programs to show progress and allows comments to be added to each file')
    p.comment('cls_file_mapping.py', 'uses ontology to get list of files to save data')
    p.comment('index.py', 'rebuilds indexes')
    

    p.comment('view.py', 'view the data in AIKIF - to be deprecated')
    p.comment('dataTools.py', 'data tools to manage database access')
    p.comment('AIKIF_create.py', 'creates default structures with test data - to be deprecated')
    p.comment('AIKIF_utils.py', 'old file mapping - to be deprecated')
    
    p.comment('generateTestData.py', 'Tool to generate various test data')
    p.comment('processRawData.py', 'calls various sub tasks to collect raw data')
    p.comment('loadInfoCourseLectures.py', 'loads course lecture notes into AIKIF')
    p.comment('loadPIM_Filelist.py', 'loads generic filelists into AIKIF - indexing not implemented')
    p.comment('loadCountry_Gdeltproject.py', 'sample load - loads country data into AIKIF')
    p.comment('loadPIM_shoppingList.py', 'sample data - loads a users shopping list into AIKIF')
    p.comment('security.py', 'future module to handle security and privacy settings')

    p.comment('bias.py', '[DATA] weight the validity of source data based on location, person, timing')
    p.comment('cls_collect_files.py', 'duplicate - see agent filelist collecting')
    p.comment('config.py', '[DATA] central point for settings in AIKIF')
    p.comment('cls_log.py', 'logging function to map to standard outputs. Almost provides auto aggregation')
    p.comment('create_word_lists.py', 'read ontology files to generate list of nouns and verbs (to be deprecated)')
    p.comment('mapper.py', 'maps business rules and columns of source data to standard aikif logs')
    p.comment('search.py', 'command line search tool')
    p.comment('tools.py', '[DATA] uses the toolbox class to create list of programs used by aikif')
    p.comment('agent.py', 'base agent class')
    p.comment('test_agent.py', 'test for agent class (why is this not in /tests root folder? TODO')
    p.comment('agg_context.py', 'detects context of user and computer')
    
    p.comment('agent_map_data.py', 'maps columns to aikif structure - attempt#3 (may be depracated)')

    
    p.comment('addRawData.py', 'original attempt at adding data (to be deprecated) ')
    p.comment('load_PC_usage.py', 'reads the logged data from agent collect PC info and logs to aikif')
    p.comment('load_info_cooking_recipe.py', 'toy attempt at adding domain specific info - to be improved or moved to business mappings')
    p.comment('agent_explore_grid.py', 'working prototype of agent to move through a grid world, using very simple path finding. Mainly an exercise in logging an agent moving through a generated world')
    p.comment('agent_email.py', 'Agent that reads emails (currently only gmail)')
    p.comment('agent_filelist.py', 'TOK - correctly scans and logs filelists from an agent')
    p.comment('collect_Win_processes.py', 'script to collect windows processes. Currently not part of agent process, more an exercise on what can be logged')
    p.comment('log_PC_usage.py', 'script to read current window title to be used as part of context to see what user is doing')
    p.comment('log_browser_history.py', 'script to dump chrome browser history to CSV - not used')
    p.comment('check_redis_limit.py', 'starts reddis database and tests limits by repeatedly adding data until it breaks')
    p.comment('cls_data.py', 'base class for data')
    p.comment('cls_dataset.py', 'functions for a schema table - progress = stub only')
    p.comment('cls_datatable.py', 'functions for a single table - progress = TOK')
    p.comment('cls_sql_code_generator.py', 'useful generation of SQL commands')
    p.comment('form_example_simple.py', 'creates a TKinter form to show how sql generation works = TOK')
    p.comment('worlds.py', 'generates a 2d grid world')
    p.comment('autobackup.py', 'example showing automatic file backups via filelists')
    p.comment('document_AIKIF.py', 'this program - collect a list of programs and add commments / progress on what is actually implemented rather than trust docstrings which show the intention of the class')
    p.comment('ex_index_mydocs.py', 'example showing what to index')
    p.comment('ex_project_management.py', 'example on using aikif for project management (poor example - needs work)')
    p.comment('finance_example.py ', 'example of using aikif for finance logging - good concept, needs completion')
    p.comment('game_of_life_console.py', 'example showing a game of life = TOK')
    p.comment('world_generator.py', 'generates a 2D grid world with random terrain - land, sea, blockages')
    p.comment('gui_view_world.py', 'script to read a saved grid from world.py and show in gui. Good for seeing grids larger than 80x25')
    p.comment('cls_file.py', 'TOK - class for handling file details - has subclasses for test, pictures and audio')
    p.comment('cls_goal.py', 'base class for managing goals')
    p.comment('cls_goal_friendly.py', 'STUB - test if a goal is friendly (needs 10-40 years work to be implemented properly)')
    p.comment('cls_goal_money.py', 'example based on cls_goal to manage money goals')
    p.comment('cls_goal_time.py', 'example based on cls_goal to manage time goals')
    p.comment('cls_plan.py', 'STUB only at this stage - this should provide the link from goals to toolbox (somewhat tricky to say the least)')
    p.comment('load_ABS_data.py', 'old example showing how to map reading a file to the aikif')
    p.comment('createMindOntology.py', 'script to parse website wiki page of OpenCog into a simple CSV structure')
    p.comment('cyc_extract.py', 'script to read OpenCyc dataset and extract data (STUB only)')
    p.comment('read_opencyc.py', 'script to read OpenCyc dataset')
    p.comment('read_wordnet.py', 'script to read WordNet dataset')
    p.comment('review_ontology.py', '[DATA] program to document details of ontology review')
    p.comment('run_agents.py', 'Top level function to run the agents')
    p.comment('Toolbox.py', 'class to manage the toolbox - list of programs and functions aikif can use')
    p.comment('cls_grid.py', 'base class for 2D grid for games - 2048, game of life, 2D terrain maps')
    p.comment('cls_grid_life.py', 'game of life game')
    p.comment('maths_ml_algorithms.py', 'machine learning algorithms for toolbox in AIKIF')
    p.comment('crypt_utils.py', 'scripts to encode / decode data')
    p.comment('game_board_utils.py', 'board game rules')
    p.comment('solve_knapsack.py ', 'toolbox - solves knapsack (using trivial algorithms)')
    p.comment('test_tool.py', 'tesing toolbox (SHOULD BE IN TESTS)')
    p.comment('page_about.py', 'web_aikif - generates page using flask')
    p.comment('page_agents.py', 'web_aikif - generates page using flask')
    p.comment('page_data.py', 'web_aikif - generates page using flask')
    p.comment('web_aikif.py', 'web_aikif - generates page using flask')
    p.comment('web_utils.py', 'web_aikif - generates page using flask')
    p.comment('check_python_env.py', 'script to test imports to ensure all correct packages are available')
    p.comment('run_tests.py', 'runs all tests in /tests subfolder')
    p.comment('if_database.py', 'dataTools - interface base class to a database')
    p.comment('if_mssqlserver.py', 'dataTools - interface class to a mssql database')
    p.comment('if_oracle.py', 'dataTools - interface class to an oracle database')
    p.comment('if_redis.py', 'dataTools - interface class to a redis database')

    p.comment('agent_browser.py', 'collects data from browser - bookmarks, visited sites')
    p.comment('outlook_export.py', 'agent to connect to outlook and export emails')
    p.comment('agent_learn_aixi.py', '')
    p.comment('dummy_learn_1.py', 'sample (but stub only) learning algorithm to be called as test below')
    p.comment('run_dummy_learn_1.py', 'sample code to call a learning algorithm')
    p.comment('cls_collect.py', 'collect filelists')
    p.comment('example_solve_happiness.py', 'toy problem - finding a world to keep all people happy (O^n^n^n complexity :) )')
    p.comment('finance_example.py', 'toy problem - logging finance data [TODO]')
    p.comment('maths_fermat_brute_force.py', 'sample script to calculate long running process')
    p.comment('puzzle_N_queens.py', 'stub only - not implemented///')
    p.comment('puzzle_missions_canninballs.py', 'calculates the path to solve problem')
    p.comment('solve_travelling_salesman.py', 'stub only')
    p.comment('cls_context.py', 'estimate what the user and PC are currently actively working on')
    p.comment('cls_filelist.py', 'fileslist class')
    p.comment('cls_plan_BDI.py', 'stub for planner based on belief, desire, intent')
    p.comment('cls_plan_search.py', 'AI planner search functions')
    p.comment('project.py', 'Core module to manage projects - meta self documentation')
    p.comment('algebra.py', 'toolbox module for based evaluation of maths problems')
    p.comment('data_structures.py', 'Node and Graph classes')
    p.comment('solve_knapsack.py', 'functions to solve the knapsack problem')


   # p.list()	# get list of all programs
    p.save()
    p.collect_program_info('progress.md')


def get_list_of_applications():
    """
    Get list of applications
    """
    apps = mod_prg.Programs('Applications', 'C:\\apps')
    fl = mod_fl.FileList(['C:\\apps'], ['*.exe'], ["\\bk\\"])
    for file in fl.get_list():
        apps.add(file, 'autogenerated list')
    apps.list()
    apps.save()


if __name__ == '__main__': 
    main()