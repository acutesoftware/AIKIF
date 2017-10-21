# page_agents.py
# handles the agents display page for AIKIF web interface

import os
import web_utils as web

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )

def get_page():
    txt = ''
    txt += load_agent_list(os.path.join(root_fldr,"data"))
    txt += web.build_edit_form('Agents', '001', ['Agent Name', 'Program Location', 'params'], '/agents')

    return txt


    
def load_agent_list(fldr):
    """
    reads the text file showing the list of agent classes used
    and presents counts based on the agent usage
    """
    res = []
    with open(os.path.join(fldr, 'list_agent_names.txt'), 'r') as f:
        for line in f:
            if line != '':
                res.append(line)

    return web.build_html_listbox(res, 'agents')
    