#!/usr/bin/python3
# -*- coding: utf-8 -*-
# room.py

import os
import sys 


import environment as env

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder)
import cls_log 
import config as mod_cfg


class Room(env.Environment):
    """
    Room environments
    """
    def __init__(self, name):
        env.Environment.__init__(self, name)
        self.doors_connect_to = []
        
        
        
    def __str__(self):
        """
        show the Room details
        """
        res = 'Room: ' + self.name + '\n'
        return res

        
        
    def connects_to(self, room, direction):    
        """
        to build simple map of a home
        """
        self.doors_connect_to.append([room, direction])
        
        
        
    