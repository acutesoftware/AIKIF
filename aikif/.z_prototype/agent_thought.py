#!/usr/bin/python3
# -*- coding: utf-8 -*-
# agent_thought_ex1.py

import os
import sys
sys.path.append('..')

import cls_file_mapping as mod_filemap
import core_data as c
from agents import agent as mod_ag
from environments import environment as mod_env

from lib import cls_goal as mod_goal

from data.core import base_emotions as emotions
from data.core import base_actions as actions
from data.core import base_objects as objects

op_folder = os.path.join(os.getcwd(), 'results')

def main():
    """
    prototype on thought process
    """
    
    world = mod_env.Environment('Earth')  # may implement later, but not needed now
    
    goals = [
            mod_goal.Goal('Be Happy'),
            mod_goal.Goal('Get Rich'),
            mod_goal.Goal('Learn to Juggle')
            ]
    jenny = ThinkingAgent('Jenny', goals)
    print(jenny)
    
    # define the thoughts and actions that can occur
    t = Thoughts(jenny)
    t.add(Thought('Hang out with Friends', result_success = actions.fun, result_fail = [], time_cost=1, cash_cost=0.0))
    t.add(Thought('Find a Job', result_success = actions.job, result_fail = emotions.sadness, time_cost=3, cash_cost=0.2))
    t.add(Thought('Go to Work', result_success = objects.cash, result_fail = emotions.sadness, time_cost=5, cash_cost=-10))
    t.add(Thought('Read a book', result_success = [actions.fun, actions.training], result_fail = [], time_cost=3, cash_cost=0))
    t.add(Thought('Rob a bank', result_success = [objects.cash, actions.prison], result_fail = [emotions.sadness, actions.prison], time_cost=1, cash_cost=0.2))

    all_links = Links(jenny)
    all_links.add_link('goal', goals[0], 'thought', t.thoughts[0])
    all_links.add_link('goal', goals[1], 'thought', t.thoughts[1])
    all_links.add_link('goal', goals[1], 'thought', t.thoughts[2])
    all_links.add_link('goal', goals[0], 'thought', t.thoughts[3])
    
    print(all_links)


class ThinkingAgent(mod_ag.Agent):
    def __init__(self, name, goals):
        super(ThinkingAgent, self).__init__(name, fldr=op_folder, running=False)
        self.goals = goals
        
    
    def __str__(self):
        res = 'Agent Name = ' + self.name + '\n'
        res += 'Goals:\n' 
        for num, g in enumerate(self.goals):
            res += ' G> ' + str(num) + ' = ' + str(g) + '\n'
        return res
    
    def add_goal(self, goal, position=0):
        self.goals.append(goal)
        
        
    def plan_day(self, mood=None):
        """
        use the thoughts to guess the best pathto achieving goals
        based on mood.
        (Mood will affect how successful (time/energy penalties?)
         you are to complete thoughts (should these be call actions?)
         
        """ 
       
        
class Goals(object):
    """
    
    """
    def __init__(self, goals=None):
        if goals:   
            self.goals = goals
        else:
            self.goals = []
    
 
class Thought(object):    
    """
    a thought modifies actions. Actually not really sure here.
    The idea is that this is a bunch of stuff going on in an 
    agents head that they could do, in order to achieve a goal.
    It starts as thoughts, but are normally mapped as actions.
    
    May need to rename this
    
    """
    
    def __init__(self, name, result_success, result_fail, time_cost, cash_cost):
        self.name = name
        self.result_success = result_success
        self.result_fail = result_fail
        self.time_cost = time_cost
        self.cash_cost = cash_cost

    def __str__(self):
        res = ' T> '
        
        res += self.name + ' (costs ' + str(self.time_cost) + ' days and $' + str(self.cash_cost) + ')\n'
        res += 'If successful, you get = ' + str(self.result_success) + '\n'
        res += 'If failed, you get = ' + str(self.result_fail) + '\n'
        
        return res
        
        
class Thoughts(object):
          
    """
    a thought modifies actions
    """
    
    def __init__(self, agent):
        self.agent = agent
        self.thoughts = []
    
    def __str__(self):
        res = 'Thoughts : \n'
        for t in self.thoughts:
            res += ' - ' + str(t) + '\n'
        return res
    
    def add(self, thought):
        self.thoughts.append(thought)
        
    

class Link(object):
    def __init__(self, src_type, src_obj, dest_type, dest_obj):
        self.src_type = src_type
        self.src_obj = src_obj
        self.dest_type = dest_type
        self.dest_obj = dest_obj
    
    def __str__(self):
        res = ' L> '
        res += self.src_type + '='
        if self.src_type == 'goal':
            res += str(self.src_obj) + '==>' 
        else:
            res += self.src_obj.name + ' ==> ' 
        
        res += self.dest_type + '='
        if self.dest_type == 'goal':
            res += str(self.dest_obj) + '\n'
        else:
            res += self.dest_obj.name + '\n' 
        return res
        
class Links(object):
    """
    manage links between goals, actions, thoughts, modifiers
    """
    def __init__(self, agent):
        self.agent = agent
        self.links = []

    def __str__(self):
    
        res = 'Links: '
        for l in self.links:
            res += str(l) #+ '\n'
        return res
         
    def add_link(self, src_type, src_obj, dest_type, dest_obj):
        self.links.append(Link(src_type, src_obj, dest_type, dest_obj))
        
    
    
    
    
main()