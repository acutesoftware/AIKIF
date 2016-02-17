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
    txt += load_agent_list(os.path.join(root_fldr,"data"))
    return txt
    
def load_agent_list(fldr):
    """
    reads the text file showing the list of agent classes used
    and presents counts based on the agent usage
    """
    res = '\n<TABLE border=1 valign=top width=80%><TR><TH>Class</TH><TH>Name</TH></TR>\n'
    cols = []
    with open(os.path.join(fldr, 'list_agent_names.txt'), 'r') as f:
        for line in f:
            res += '<TR><TD>'
            cols = line.split(':')
            res += cols[0] + '</TD><TD>'
            res += cols[1] + '</TD>'
            res += '</TR><BR>\n'
    res += '</TABLE><BR><BR>\n'
    
    
    return res