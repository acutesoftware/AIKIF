# page_search.py	written by Duncan Murray 4/6/2014
# displays search results for AIKIF web interface

import sys
import web_utils as web
sys.path.append('..\\..\\AI')

def get_page(search_text):
	lst = search_aikif(search_text)
	txt = '<TABLE width=100% border=0>'
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
						results.append(format_result(f, line, line_num))
			results.append(f + ' = ' + str(num_found) + ' results')
			
		except:
			results.append('problem with file ' + f)
	return results
			
def format_result(file, txt, line_num):
	return '&nbsp;&nbsp;' + str(line_num) + ': ' + txt 
	