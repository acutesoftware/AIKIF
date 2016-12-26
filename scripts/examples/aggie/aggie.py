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


def main():
    
    a = Aggie()
    a.run()
    print(a)
    print('done')
    

class Aggie(object):
    """
    main class for agent
    """
    
    def __init__(self, fldr=os.getcwd(), skills = None, info = None):
        self.fldr = fldr
        
        self.skills = skills
        
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
            print(self.answer(self.get_input()))
        
        print('Bye')
    
    def get_input(self):
        q = input(self.status + ' > ')
        if q.lower() == 'quit' or q.lower() == 'exit':
            self.status = 'EXIT'
        return q

    def answer(self, question):
        """
        takes a question and returns the best answer based on known skills
        """
        ans = ''
        if self.status == 'EXIT':
            print('bye')
            sys.exit()
        if 'weather' in question:
            ans = 'sunny'
        elif 'where' in question:
            ans = '4km to the North'
            
        elif 'when' in question:
            ans = 'next week'
        elif question.startswith(':LIST'):
            for i in self.info.raw_input:
                print('raw input = ', str(i))
                
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
    
