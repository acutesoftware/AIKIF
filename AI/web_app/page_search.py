# page_search.py	written by Duncan Murray 4/6/2014
# displays search results for AIKIF web interface

import sys
import web_utils as web
sys.path.append('..\\..\\AI')

def get_page(search_text):
	lst = search_aikif(search_text)
	txt = '<table class="as-table as-table-zebra as-table-horizontal">'
	for result in lst:
		txt += '<TR><TD>' + result + '</TD></TR>'
	txt += '</TABLE>\n\n'
	return txt
	
def search_aikif(txt):
	results = []
	num_found = 0
	import cls_collect_files as cl
	my_files = cl.clsCollectFiles('..\\data\\core', '*.*') 
	my_files.collect_filelist()
	files = my_files.get_filelist()
	for f in files:
		try:
			num_found = 0
			with open(f, 'r') as cur:
				line_num = 0
				for line in cur:
					line_num += 1
					if txt in line:
						num_found += 1
						results.append(format_result(f, line, line_num, txt))
			if num_found > 0:
				results.append(f + ' = ' + str(num_found) + ' results')
			
		except:
			results.append('problem with file ' + f)
	if len(results) == 0:
		results.append("No results")
	return results
			
def format_result(file, line, line_num, txt):
	""" highlight the search result """
	
	return '&nbsp;&nbsp;' + str(line_num) + ': ' + line.replace(txt, '<span style="background-color: #FFFF00">' + txt + '</span>')
	