#!/usr/bin/python3
# coding: utf-8
# Allen_AI_run.py      written by Duncan Murray 10th-Oct-2015

import os
import sys
#import aikif.project as mod_prj
import aikif.dataTools.cls_datatable as mod_dt


# fudge to make sure we run LOCAL aikif programs


py_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  + os.sep + ".." + os.sep + "aikif"  + os.sep + "toolbox")
sys.path.append(py_fldr)
import Toolbox as mod_tool

sys.path.append( os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  + os.sep + ".." + os.sep + "aikif" ))
import project as mod_prj

root_folder = '/home/duncan/dev/src/python/kaggle/aicomp'
src_data = root_folder + '/data'
op_folder = root_folder + '/output'

params = [ -0.5, -0.02, 1, 124]

def main():
    p = mod_prj.Project('Allen_AI', tpe='Software', fldr=op_folder , desc='Kaggle competetion entry for Allen_AI')

    p.add_detail('kaggle_url', 'https://www.kaggle.com/c/the-allen-ai-science-challenge')
    p.add_detail('files_root_folder', root_folder)
    p.add_detail('files_src_data', src_data)
    p.add_detail('files_op_folder', op_folder)
    p.add_detail('date_last_ran', mod_dt.TodayAsString())
    
    lookup_src = mod_dt.DataTable('lookup_src.csv', ',', col_names=['name', 'url'])
    p.log_table(lookup_src)
    p.record(lookup_src, '', ['page-resources', 'http://aclweb.org/aclwiki/index.php?title=RTE_Knowledge_Resources#Publicly_available_Resources'])
    p.record(lookup_src, '', ['science_notes', 'http://www.ck12.org/'])
    p.record(lookup_src, '', ['data-wikipedia', 'https://en.wikipedia.org/wiki/Wikipedia:Database_download'])

    progress = mod_dt.DataTable('progress.csv', ',', col_names=['program', 'percent', 'details'])
    p.log_table(progress)
    p.record(progress, '', ['Source data download', '100%',  'download competition sample data'])
    p.record(progress, '', ['Allen_AI_install.py', '0%',  'downloads lookup data, unzips'])
    p.record(progress, '', ['Allen_AI_run.py', '2%',  'main script to run the program'])
    p.record(progress, '', ['method1.py', '5%',  'method to answer questions using heuristic #1'])
    p.record(progress, '', ['method2.py', '0%',  'method to answer questions using heuristic #2'])
    p.record(progress, '', ['method3.py', '0%',  'method to answer questions using heuristic #3'])

    t = mod_tool.Toolbox()
    t.add({'file':'method1.py', 'function':'solve', 'args':['list'], 'return':['int']})
    t.add({'file':'method2.py', 'function':'solve', 'args':['list'], 'return':['int']})
    t.add({'file':'method3.py', 'function':'solve', 'args':['list'], 'return':['int']})

    results = mod_dt.DataTable('results.csv', ',', col_names=['program', 'function', 'param', 'result', 'date_ran'])
    p.log_table(results)
    
    for tool_num, tool in enumerate(t.lstTools):
        print('tool=', tool)
        for param in params:
            result = t.run(tool, ['test' + str(tool_num), param], 'Y', root_folder)
            p.record(results, '', [tool['file'], tool['function'], param, result, mod_dt.TodayAsString()])
    results.save_csv(os.path.join(root_folder, 'allen_AI_results.csv'))   
       
    
       
    p.build_report('allen_AI.rst', tpe='rst')
    print('Done...')

       



def define_tools(p):
    """
    setup all programs to be used for the competition
    """


    p2.add_task(1, 'Fetch source data', aikif.toolbox.data_view)
    p2.add_task(2, 'Aggregate Population', t['Calc Average'])

    p2.add_param(task=1, tbl = 'S_REF_COUNTRY' )
    p2.add_param(task=2, group_by_col = 'CONTINENT', measure_col='POPULATION' )

    p2.execute()  # with no parameters, data outputs to console    

main()
