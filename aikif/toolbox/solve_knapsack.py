#!/usr/bin/python
# -*- coding: utf-8 -*-
# solve_knapsack.py		written by Duncan Murray 24/4/2014
# WARNING - untested and inefficient solvers (here to test to AIKIF toolbox function)
from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def describe_problem(capacity, items):
    print('\nAIKIF Knapsack Solver - 9/3/2014')
    print('This attempts to maximise the number of items that can fit into a Knapsack')
    print('--------------------------------------------------------------------------')
    print('PROBLEM : '   )
    print('Knapsack Capacity = ' + str(capacity))
    print('Total Items = ' + str(len(items)))
    for item in items:
        print ('item [' + str(item.index) + '] value = ' + str(item.value) + ', item.weight = ' + str(item.weight) + ' density = ' + str(item.density))
    print('--------------------------------------------------------------------------')
    

def solve_greedy_trivial(capacity, items):
    taken = [0]*len(items)
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
            #density = 

    return value, taken

def solve_smallest_items_first(capacity, items):
    taken = [0]*len(items)
    value = 0
    weight = 0
    taken = [0]*len(items)
    sortedList = sorted(items, key=lambda dens: dens[2], reverse=False)
    for item in sortedList:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return value, taken
    
def solve_expensive_items_first(capacity, items):
    taken = [0]*len(items)
    value = 0
    weight = 0
    taken = [0]*len(items)
    sortedList = sorted(items, key=lambda dens: dens[1], reverse=True)
    for item in sortedList:
        #print ('item [' + str(item.index) + '] value = ' + str(item.value) + ', item.weight = ' + str(item.weight) + ' density = ' + str(item.density))
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
            #print('Adding [' + str(item.index) + '],  value = ' + str(item.value) + ' wght = ' + str(item.weight) )

    return value, taken
    
    
def solve_value_density(capacity, items):
    value = 0
    weight = 0
    taken = [0]*len(items)
    valueDensity = sorted(items, key=lambda dens: dens[3], reverse=True)
    for item in valueDensity:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return value, taken
 


def main():
    # Modify this code to run your optimization algorithm

    #Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])
    capacity = 19

    items = []
    items.append(Item(1, 8, 4, 8 * 4))
    items.append(Item(1, 10, 5, 10 * 5))
    items.append(Item(1, 15, 8, 15 * 8))
    items.append(Item(1, 4, 3, 4 * 3))

    describe_problem(capacity, items)
    value, taken = solve_expensive_items_first(capacity, items)
    print('solve_expensive_items_first = ', value, taken)
    
    value, taken = solve_smallest_items_first(capacity, items)
    print('solve_smallest_items_first = ', value, taken)

    value, taken = solve_value_density(capacity, items)
    print('solve_value_density = ', value, taken)

if __name__ == '__main__':
    main()
