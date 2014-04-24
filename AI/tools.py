# coding: utf-8
# tools.py	written by Duncan Murray 20/3/2014	(C) Acute Software
# Script to configure the functional toolbox of AIKIF


import toolbox.Toolbox as tool

tl = tool.Toolbox()

tl.add({'file':'solve_knapsack.py', 'function':'solve_greedy_trivial', 'args':['int', 'dict'], 'return':['int', 'list']})
tl.add({'file':'solve_knapsack.py', 'function':'solve_smallest_items_first', 'args':['int', 'dict'], 'return':['int', 'list']})
tl.add({'file':'solve_knapsack.py', 'function':'solve_expensive_items_first', 'args':['int', 'dict'], 'return':['int', 'list']})
tl.add({'file':'solve_knapsack.py', 'function':'solve_value_density', 'args':['int', 'dict'], 'return':['int', 'list']})
#tl.add({'file':'solve_knapsack.py', 'function':'', 'args':['int', 'dict'], 'return':['int', 'list']})

tl.save('tools.txt')


