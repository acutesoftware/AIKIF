#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_agent_interface_environment.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'agents' 

sys.path.append(pth)


import agent_interface_env as mod_agt
agt = mod_agt.AgentInterfaceEnv('Agent Enviroment Interface')
print(agt)
