#!/usr/bin/python3
# -*- coding: utf-8 -*-
# agent_interface_env.py

import os
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "..") 

from . import agent as agt


class AgentInterfaceEnv(agt.Agent):
    """
    Base class for an agent to interact with a computer, via 
    reading responses and sending keys / mouse clicks. Depends
    heavily on the toolbox functions, but wraps these to provide
    a standard interface to an agent (though these agents have no
    goals as such, they just 'send this string to this program'
    """
    def __init__(self, name):
        self.name = name
        agt.Agent.__init__(self, name,  fldr=os.getcwd(), running=True)
        
    def __str__(self):
        return self.name  + " is " + self.status
        
    def send_string(self, *args):
        """
        sends a string of text to the window 'wnd', note that this 
        must be subclassed by appropriate OS
        """
        print('HEY - you cant call send_string directly')
        raise ValueError('agent_interface_env.py->AgentInterfaceEnv: WARNING - dont run this from base class') 
        
    
class AgentInterfaceWindows(AgentInterfaceEnv):
    def send_string(self, wnd, txt):
        """
        sends a string to window and returns True/False as result
        """
        print('sending string to OS Windows')
        return True
        
       
    
class AgentInterfaceLinux(AgentInterfaceEnv):
    pass
    
class AgentInterfaceIOS(AgentInterfaceEnv):
    pass
    
class AgentInterfaceAndroid(AgentInterfaceEnv):
    pass
    
    
