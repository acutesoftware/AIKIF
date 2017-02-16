#!/usr/bin/python3
# -*- coding: utf-8 -*-
# agent_pcusage.py

import os
import sys

agent_root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(agent_root_folder)
import agent as agt


class PCUsageAgent(agt.Agent):
    """
    agent to process raw PC usage data
    """
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        #agt.Agent.__init__(self, *arg)
        agt.Agent.__init__(self, name,  fldr, running)
        self.LOG_LEVEL = LOG_LEVEL


    def process_file(self, fname, map_object):
        """
        takes a raw PC usage file and uses the MapUsage 
        instance to aggregate.
        """
        pass
        

class MapUsage(object):
    """
    reads a mapping file of raw PC Usage strings to
    classify what user was doing. Useful for aggregate
    of time spent on applications and work/life balance
    and for measuring billable hours.
    """
    
    def __init__(self, fname):
        """
        reads the mapping file used by this agent to 
        process the raw data.
        """
        self.maps = []
        cur_line = []
        cur_map = {}
        
        with open(fname, 'r') as fip:
            for line in fip:
                if line != '':
                    cur_line = line.split(',')
                    self.maps.append(cur_line)
                    
                    
            
        
    def process_line(self, line):
        """
        takes a single line of data from logged PC usage
        and returns the mapped application name, project, 
        and classification.
        
        """
        
        res_app = ''
        res_proj = ''
        res_clas = ''
        

        return res_app, res_proj, res_clas
        
        
        