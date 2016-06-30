#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_agent_learn_quiz.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = os.path.join(root_folder,'aikif','agents','learn' )
tool_folder = os.path.join(root_folder, 'aikif', 'toolbox')

sys.path.append(pth)
import agent_learn_quiz as mod_agt

sys.path.append(tool_folder)

agt = mod_agt.LearnAgentQuiz('TEST - quiz_agent',  os.getcwd(), 4, True)



class TestAgentLearnQuiz(unittest.TestCase):
    """
    Sample output of logfile
    "2016-06-28 22:56:09","000000026","Duncan","Treebeard","TEST - quiz_agent - initilising","agent",
    "2016-06-28 22:56:09","000000026","Duncan","Treebeard","['calc', '4', '+', '5']","TEST - quiz_agent",
    "2016-06-28 22:56:09","000000026","Duncan","Treebeard","['where', 'is', 'boston?']","TEST - quiz_agent",
    "2016-06-28 22:56:09","000000026","Duncan","Treebeard","['when', 'did', 'i', 'hand', 'in', 'the', 'latest', 'tps', 'report?']","TEST - quiz_agent",
    "2016-06-28 22:56:09","000000026","Duncan","Treebeard","['why', 'do', 'my', 'potplants', 'have', 'faded', 'leaves?']","TEST - quiz_agent",
    """
    
    def test_11_answer_maths(self):
        #self.assertEqual(agt.answer('calc 4 + 5'), 'calculating maths result')
        response = agt.answer('calc 4 + 5')
        print(response)
        
    def test_12_answer_geography(self):
        #self.assertEqual(agt.answer('where is Boston?'), "that's somewhere on Earth I think")
        pass
        
    def test_13_answer_dates(self):
        #self.assertEqual(agt.answer('When did I hand in the latest TPS report?'), 'Last Wednesday')
        pass
        
    def test_14_answer_facts(self):
        #self.assertEqual(agt.answer('Why do my potplants have faded leaves?'), 'Probably caused by lack of sunlight')
        pass
        
if __name__ == '__main__':
    unittest.main()
