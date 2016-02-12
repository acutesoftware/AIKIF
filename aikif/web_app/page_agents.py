# page_agents.py
# handles the agents display page for AIKIF web interface

import os
import sys
#import aikif.web_app.web_utils as web
import web_utils as web

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
print(root_fldr)

def get_page():
    txt = ''
    txt += '<p>Page to show agents currently setup in AIKIF.</p>'
    txt += load_agent_list(os.path.join(root_fldr,"data"))
    return txt
    
def load_agent_list(fldr):
    """
    reads the text file showing the list of agent classes used
    and presents counts based on the agent usage
    """
    res = '\n'
    with open(os.path.join(fldr, 'list_agent_names.txt'), 'r') as f:
        for line in f:
            res += line + '<BR>\n'
    res += '<BR><BR>\n'
    
    
    return res