#!/usr/bin/python3
# -*- coding: utf-8 -*-
# agent_learn_quiz.py.py


import os
import random
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "..") 

import aikif.agents.agent as agt


class LearnAgentQuiz(agt.Agent):
    """
    sample agent that pretends to know information.
    Use for trying out method of rating AI agents.
    """
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        agt.Agent.__init__(self, name,  fldr, running)
        self.LOG_LEVEL = LOG_LEVEL

        
    def do_your_job(self):
        print('Waiting for question...')
 
    def show_status(self):
        """
        dumps the status of the agent
        """
        txt = 'Agent Status:\n'
        print(txt)
        return txt

    def answer(self, question):
        """
        These are dummy answers to questions
        """
        words = [w.lower() for w in question.split(' ')]
        self.mylog.record_command(self.name, str(words))
        if 'calc' in words:
            return 'calculating maths result'
        elif 'where' in words:
            return "that's somewhere on Earth I think"
        elif 'when' in words:
            return "Last Wednesday"
        elif 'why' in words:
            return "Probably caused by lack of sunlight"
        
        