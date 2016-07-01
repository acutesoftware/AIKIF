#!/usr/bin/python3
# coding: utf-8
# page_search.py
# displays search results for AIKIF web interface

import os

cur_folder = os.path.dirname(os.path.abspath(__file__)) 
aikif_folder = os.path.abspath(cur_folder + os.sep + ".."  )
data_folder = os.path.abspath(aikif_folder + os.sep + '..' + os.sep  + 'data' + os.sep + 'core')

def get_page(search_text):
    """
    formats the entire search result in a table output
    """
    lst = search_aikif(search_text)
    txt = '<table class="as-table as-table-zebra as-table-horizontal">'
    for result in lst:
        txt += '<TR><TD>' + result + '</TD></TR>'
    txt += '</TABLE>\n\n'
    return txt
    
def search_aikif(txt, formatHTML=True):
    """
    search for text - currently this looks in all folders in the
    root of AIKIF but that also contains binaries so will need to 
    use the agent_filelist.py to specify the list of folders.
    
    NOTE - this needs to use indexes rather than full search each time
    """
    results = []
    num_found = 0
    import aikif.lib.cls_filelist as mod_fl
    my_files = mod_fl.FileList([aikif_folder ], ['*.*'], ['*.pyc'])
    files = my_files.get_list()
    for f in files:
        try:
            num_found = 0
            with open(f, 'r') as cur:
                line_num = 0
                for line in cur:
                    line_num += 1
                    if txt in line:
                        num_found += 1
                        if formatHTML is True:
                            results.append(format_result(line, line_num, txt))
                        else:
                            results.append([f, line, line_num, txt])
            if num_found > 0:
                if formatHTML is True:
                    results.append('<h3>' + f + ' = ' + str(num_found) + ' results</h3>')
                else:    
                    print(f + ' = ' + str(num_found) + '')
        except Exception:
            results.append('problem with file ' + f)
    if len(results) == 0:
        results.append("No results")
    return results
            
def format_result(line, line_num, txt):
    """ highlight the search result """
    
    return '&nbsp;&nbsp;' + str(line_num) + ': ' + line.replace(txt, '<span style="background-color: #FFFF00">' + txt + '</span>')
    