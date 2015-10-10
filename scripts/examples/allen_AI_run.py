#!/usr/bin/python3
# coding: utf-8
# Allen_AI_run.py      written by Duncan Murray 10th-Oct-2015

import os
import aikif.project as mod_prj
import aikif.dataTools.cls_datatable as mod_dt

root_folder = '/home/duncan/dev/src/python/kaggle/aicomp'
src_data = root_folder + '/data'
op_folder = root_folder + '/output'

def main():
    p = mod_prj.Project('Allen_AI', tpe='Software', fldr=op_folder , desc='Kaggle competetion entry for Allen_AI')
    document_project(p)
       
       
       
def document_project(p):
    """
    adds notes and progress for the project
    """
    p.add_detail('kaggle_url', 'https://www.kaggle.com/c/the-allen-ai-science-challenge')
    p.add_detail('files_root_folder', root_folder)
    p.add_detail('files_src_data', src_data)
    p.add_detail('files_op_folder', op_folder)
    p.add_detail('date_last_ran', mod_dt.TodayAsString())
    
    lookup_src = mod_dt.DataTable('lookup_src.csv', ',', col_names=['name', 'url', 'comments'])
    p.log_table(lookup_src)
    p.record(lookup_src, '', ['resources', 'http://aclweb.org/aclwiki/index.php?title=RTE_Knowledge_Resources#Publicly_available_Resources', ''])
    p.record(lookup_src, '', ['science_notes', 'http://www.ck12.org/', ''])


    progress = mod_dt.DataTable('progress.csv', ',', col_names=['program', 'percent', 'details'])
    p.log_table(progress)
    p.record(progress, '', ['Source data download', '100%',  'download competition sample data'])
    p.record(progress, '', ['Allen_AI_install.py', '0%',  'downloads lookup data, unzips'])
    p.record(progress, '', ['Allen_AI_run.py', '2%',  'main script to run the program'])
    p.record(progress, '', ['method1.py', '0%',  'method to answer questions using heuristic #1'])
    p.record(progress, '', ['method2.py', '0%',  'method to answer questions using heuristic #2'])
    p.record(progress, '', ['method3.py', '0%',  'method to answer questions using heuristic #3'])


    p.build_report('allen_AI.rst', tpe='rst')
    print('Done...')


main()
