# page_programs.py	written by Duncan Murray 28/5/2014
# handles the programs display page for AIKIF web interface

import sys
import web_utils as web
sys.path.append('..\\..\\AI')


def get_page():
	txt = ''
	txt += get_program_list()
	return txt
	
def get_program_list():
	txt = '<TABLE width=100% border=0>'
	#print(agt.agent_list)
	txt += '<TR><TD>Program List</TD></TR>'
	txt += '</TABLE>\n\n'
	return txt
	