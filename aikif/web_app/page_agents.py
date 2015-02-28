# page_agents.py	written by Duncan Murray 26/5/2014
# handles the agents display page for AIKIF web interface

import sys
import aikif.web_app.web_utils as web
"""
cur_folder = os.path.dirname(os.path.abspath(__file__)) 
aikif_folder = os.path.abspath(cur_folder + os.sep + ".."  )
root_folder = os.path.abspath(aikif_folder + os.sep + '..')


sys.path.append('..\\..\\AI')
"""


import aikif.run_agents as agt

def get_page():
	txt = ''
	txt += '<p>Page to show agents currently setup in AIKIF.</p>'
	txt += '<p>Modify run_agents.py to update agent list.</p>'
	txt += '<BR><BR>'
	txt += get_agent_list()
	return txt
	
def get_agent_list():
	txt = '<TABLE width=100% border=0>'
	for a in agt.get_agent_list():
		txt += web.dict_to_htmlrow(a) 
	txt += '</TABLE>\n\n'
	return txt
	