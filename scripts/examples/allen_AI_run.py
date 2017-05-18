#!/usr/bin/python3
# coding: utf-8
# Allen_AI_run.py      written by Duncan Murray 10th-Oct-2015

import os
import sys
import aikif.dataTools.cls_datatable as mod_dt

aikif_prog_root = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  + os.sep + ".." + os.sep + "aikif" )

sys.path.append(aikif_prog_root  + os.sep + "toolbox")
import Toolbox as mod_tool

sys.path.append(aikif_prog_root)
import project as mod_prj


if os.name == 'nt':
    root_folder = 'T:\\user\\dev\\src\\python\\kaggle'
else:
    root_folder = '/home/duncan/dev/src/python/kaggle/aicomp'
    
src_data = root_folder + os.sep + 'data'
op_folder = root_folder + os.sep + 'output'

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

    p.record(lookup_src, '', ['YAGO', 'http://yago-knowledge.org'])
    p.record(lookup_src, '', ['Dbpedia', 'http://dbpedia.org'])
    p.record(lookup_src, '', ['Freebase', 'http://freebase.com'])
    p.record(lookup_src, '', ['Entitycube', 'http://entitycube.research.microsoft.com'])
    p.record(lookup_src, '', ['renlifang', 'http://renlifang.msra.cn'])
    p.record(lookup_src, '', ['NELL', 'http://rtw.ml.cmu.edu'])
    p.record(lookup_src, '', ['DeepDive', 'http://deepdive.stanford.edu'])
    p.record(lookup_src, '', ['Probase', 'http://research.microsoft.com/en-us/projects/probase/'])
    p.record(lookup_src, '', ['KnowItAll', 'http://openie.cs.washington.edu'])
    p.record(lookup_src, '', ['ReVerb', 'http://reverb.cs.washington.edu'])
    p.record(lookup_src, '', ['BabelNet', 'http://babelnet.org'])
    p.record(lookup_src, '', ['WikiNet', 'http://www.h-its.org/english/research/nlp/download/'])
    p.record(lookup_src, '', ['ConceptNet', 'http://conceptnet5.media.mit.edu'])
    p.record(lookup_src, '', ['WordNet', 'http://wordnet.princeton.edu'])
    p.record(lookup_src, '', ['Linked Open Data', 'http://linkeddata.org'])

    
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
        print(('tool=', tool))
        for param in params:
            result = t.run(tool, ['test' + str(tool_num), param],  root_folder)
            p.record(results, '', [tool['file'], tool['function'], param, result, mod_dt.TodayAsString()])
    results.save_csv(os.path.join(root_folder, 'allen_AI_results.csv'))   
       
    
       
    p.build_report('allen_AI.rst', tpe='rst')
    print('Done...')


main()
