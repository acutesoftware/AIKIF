# puzzle_countdown.py   written by Duncan Murray  10/2/2015

"""
find a solution to use (4-7) small numbers to calculate one big number
Based on SBS TV show "Letters and Numbers" (based on UK show Countdown)

from: http://en.wikipedia.org/wiki/Letters_and_Numbers
Numbers round
One contestant chooses how many "small" and "large" numbers they would like to make up six randomly chosen numbers. Small numbers are between 1 and 10 inclusive, and large numbers are 25, 50, 75, or 100. All large numbers will be different, so at most four large numbers may be chosen. The contestants have to use arithmetic on some or all of those numbers to get as close as possible to a randomly generated three-digit target number within the thirty second time limit. Fractions are not allowed—only integers may be used at any stage of the calculation.

For numbers selections, they are to be straightforward. The numbers are always placed in a fixed order (going Right to Left - Small numbers are placed first, then the large ones).

Points are awarded for the closest solution, and again both contestants score if the solutions are equally close. 10 points are given for an exact answer, 7 points for a non-exact solution up to 5 from the target, and 5 points for a solution between 6 and 10 from the target. If neither contestant can get within 10, no points are awarded."

"""

import os
import sys
import math

toolbox_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." +  os.sep + "toolbox" )
lib_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." +  os.sep + "lib" )
sys.path.append(lib_folder)
sys.path.append(toolbox_folder)

def main():
    #all = get_combinations([1,2,8,3])
    #for a in all:
    #    print(a)
  #  solve(405,[50, 75], [7,3,5,10])
    solve(156,[20, 50], [1,2,5])
    
def solve(target, big_numbers, small_numbers):
    """ 
    attempt to find a solution to get a big 
    number using a set of small numbers
    """
    all_results = []
    tot = 0
    for attempt in get_combinations(small_numbers):
        tot = 0
        desc = 'Solution for ' + str(target) + ': (' + attempt[0] + ')='
        desc_big = ''
        desc_comb = ''
        desc_mult = ''
        
        for small in attempt[1]:
            desc_mult = str(small) + ', so (' + str(small) + '*'
            desc_big = ''
            for big in big_numbers:
                tot += big
                desc_big += '' + str(big) + ')+'
                tot += small
                desc_comb = ' (' + str(small) + '*' + str(small) + ')+' + str(small) + ''
                
        if tot == target:
            
            print('SUCCESS', desc + desc_mult + desc_big + desc_comb)
        all_results.append(tot)
        
    print(all_results)

def get_combinations(lst):
    """
    get new generated sets of numbers by
    combining 2 at a time
        new_list =  [5, 8]
        all_combos  =  [[5, 8]]
        new_list =  [3, 8]
        all_combos  =  [[5, 8], [3, 8]]
        new_list =  [3, 5]
        all_combos  =  [[5, 8], [3, 8], [3, 5]]    
    
    """
    all_combos = []
    multiples = []
    for a_ndx, a in enumerate(lst):
        for b_ndx, b in enumerate(lst):
            if a_ndx == b_ndx:
                continue
            new_list = [l for l in lst]
            new_list.remove(b)
            if a != b:
                new_list.remove(a)
            multiples = get_all_multiples(a,b,new_list)
            all_combos.extend(multiples)  # add the standard list
    return all_combos
  #  unique_set = [list(x) for x in set(tuple(x) for x in all_combos)]
  #  unique_set.append(['orig', lst])  # include original list
  #  return unique_set
    
def add_combo(orig_list, c, val, desc):
    tmp = [l for l in orig_list]
    tmp.append(val)
    if tmp:
        c.append([desc, tmp])
    
def get_all_multiples(a, b, orig_list):
    combo = []
    add_combo(orig_list, combo, a+b, str(a) + '+' + str(b))
    add_combo(orig_list, combo, a-b, str(a) + '-' + str(b))    
    add_combo(orig_list, combo, a*b, str(a) + '*' + str(b))    
    add_combo(orig_list, combo, a/b, str(a) + '/' + str(b))    
    add_combo(orig_list, combo, b/a, str(b) + '/' + str(a))    
    add_combo(orig_list, combo, b-a, str(b) + '-' + str(a))    
    return combo
    

    
if __name__ == '__main__':
    main()
