#!/usr/bin/python3
# -*- coding: utf-8 -*-
# aggie.py

#import aikif.config as mod_cfg
#import aikif.cls_log as mod_log

import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + ".." )
code_fldr = os.path.join(root_fldr, 'aikif')
sys.path.append(code_fldr)
import config as mod_cfg
import cls_log as mod_log

aggie_version = '0.0.2'

def main():
    a = Aggie()
    a.run()


class Aggie(object):
    """
    main class for agent
    """
    
    def __init__(self, fldr=os.getcwd(), skills = None, info = None):
        self.fldr = fldr
        
        self.skills = skills
        self.prompt = ' Aggie ' + aggie_version + ' [EXIT | :LIST | ![add raw data]  > '
        if info:
            self.info = info
        else:
            self.info = Info()
        self.status = 'Ready'
        self.lg = mod_log.Log(fldr)
        self.lg.record_source('aggie.py','Hello, my name is Aggie.')
        self.lg.record_source('aggie.py','base folder is ' + self.fldr)
        
    def __str__(self):
        return 'running aggie in ' + self.fldr

    def run(self):
        """
        loops until exit command given
        """
        while self.status != 'EXIT':
            print(self.process_input(self.get_input()))
        
        print('Bye')
    
    def get_input(self):
        q = input(self.status + ' ' + self.prompt)
        if q.lower() == 'quit' or q.lower() == 'exit':
            self.status = 'EXIT'
        return q

    def process_input(self, question):
        """
        takes a question and returns the best answer based on known skills
        """
        ans = ''
        if self.status == 'EXIT':
            print('bye')
            sys.exit()
        
        if '?' in question:
            ans = self.info.find_answer(question)
        elif question.startswith(':LIST'):
            ans = 'List of Raw Input\n'
            for i in self.info.raw_input:
                ans += str(i) + '\n'
            
            
        else:
            #ans = 'I dont'' know'
            ans = 'Adding info..'
            self.info.raw_input.append(question)
        self.lg.record_process('aggie.py', 'Question > ' +  question)
        self.lg.record_process('aggie.py', 'Answer > ' + ans)
        return ans


class Info(object):
    def __init__(self):
        self.raw_input = []
        self.facts = []
        self.derived = []

    def __str__(self):
        res = 'Info=' +str( len(self.facts)) + ' facts known\n'
        res += 'Derived Facts = ' + str(len(self.derived))
        return res
        
    def add_fact(self, factiod):
        self.facts.append(factiod)
        
        
    def find_answer(self, qu):
        """
        This takes the question 'qu' and parses info and raw input 
        to try and find an answer.
        It should use the skills, and where parameters are needed it
        should guess them if not in there - for example weather should
        default to local location unless a [country|city] is part of question
        """
        if 'weather' in qu:
            ans = 'sunny'
        elif 'where' in qu:
            ans = '4km to the North'
            
        elif 'when' in qu:
            ans = 'next week'
        
        else:
            ans = 'I dont know'
        return ans
        
        
    
class Skills(object):
    def __init__(self):
        self.skills = []
    
    def __str__(self):
        res = 'Skills='
        for s in self.skills:
            res += str(s[0]) + ', '
        return res
    
    def add_skill(self, new_skill):
        self.skills.append(new_skill)
    
        
if __name__ == "__main__":        
    main()    
    
