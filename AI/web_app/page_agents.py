# page_agents.py	written by Duncan Murray 26/5/2014
# handles the agents display page for AIKIF web interface

import sys
import web_utils as web
sys.path.append('..\\..\\AI')
import run_agents as agt


def get_page():
	txt = ''
	txt += get_agent_list()
	return txt
	
def get_agent_list():
	txt = '<TABLE width=100% border=0>'
	#print(agt.agent_list)
	for a in agt.get_agent_list():
		#txt += web.list2html(a)
		txt += web.dict_to_htmlrow(a) 
	txt += '</TABLE>\n\n'
	return txt
	