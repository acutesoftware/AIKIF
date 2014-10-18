# page_search.py	written by Duncan Murray 4/6/2014
# displays search results for AIKIF web interface

import os
import sys
import web_utils as web

cur_folder = os.path.dirname(os.path.abspath(__file__)) 
root_folder = os.path.abspath(cur_folder + os.sep + ".." + os.sep + ".."  )
aikif_folder = os.path.abspath(cur_folder + os.sep + ".."  )
data_folder = os.path.abspath(aikif_folder + os.sep + '..' + os.sep  + 'data' + os.sep + 'core')

print('page_search.py: aikif_folder = ', aikif_folder)
print('page_search.py: data_folder  = ', data_folder)
sys.path.append(aikif_folder)

def get_page(search_text):
    lst = search_aikif(search_text)
    txt = '<table class="as-table as-table-zebra as-table-horizontal">'
    for result in lst:
        txt += '<TR><TD>' + result + '</TD></TR>'
    txt += '</TABLE>\n\n'
    return txt
    
def search_aikif(txt, formatHTML=True):
    results = []
    num_found = 0
    import cls_collect_files as cl
    my_files = cl.clsCollectFiles(root_folder, '*.*') 
    my_files.collect_filelist()
    files = my_files.get_filelist()
    for f in files:
        #print(f)
        try:
            num_found = 0
            with open(f, 'r') as cur:
                line_num = 0
                for line in cur:
                    #print(line)
                    line_num += 1
                    if txt in line:
                        num_found += 1
                        if formatHTML == True:
                            results.append(format_result(f, line, line_num, txt))
                        else:
                            results.append([f, line, line_num, txt])
            if num_found > 0:
                if formatHTML == True:
                    results.append('<h3>' + f + ' = ' + str(num_found) + ' results</h3>')
                else:    
                    print(f + ' = ' + str(num_found) + '')
        except:
            results.append('problem with file ' + f)
    if len(results) == 0:
        results.append("No results")
    #print(results)
    return results
            
def format_result(file, line, line_num, txt):
    """ highlight the search result """
    
    return '&nbsp;&nbsp;' + str(line_num) + ': ' + line.replace(txt, '<span style="background-color: #FFFF00">' + txt + '</span>')
    