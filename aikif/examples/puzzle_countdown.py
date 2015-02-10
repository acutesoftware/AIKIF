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
    print(get_combinations([2,3,5,8]))
    #solve(500,[75], [2,3,6,7,4])
    
def solve(target, big_numbers, small_numbers):
    """ 
    attempt to find a solution to get a big 
    number using a set of small numbers
    """
    all_results = []
    tot1 = 0
    tot2 = 0
    for s in small_numbers:
        for b in big_numbers:
            tot1 += b * s
            tot2 += b + s
        all_results.append(tot1)
        all_results.append(tot2)
    print(all_results)

def get_combinations(lst):
    """
    get new generated sets of numbers by
    combining 2 at a time
    """
    all_combos = []
    multiples = []
   # unique_set = []
    for a_ndx, a in enumerate(lst):
        for b_ndx, b in enumerate(lst):
            if a_ndx == b_ndx:
                continue
            new_list = [l for l in lst]
            new_list.remove(b)
            if a != b:
                new_list.remove(a)
            all_combos.append(new_list)  # add the standard list
            print('new_list = ', new_list)
            print('all_combos  = ', all_combos)
            """    
            print('new_list (before get mult) = ', new_list)
            multiples = get_all_multiples(a,b,new_list)
            print('\n\nmultiples=',multiples)
            for m in multiples:
                if m:
                    all_combos.append(m)
            """
    unique_set = [list(x) for x in set(tuple(x) for x in all_combos)]
    return unique_set

def get_all_multiples(a, b, orig_list):
    combo = []
    combo.append([l for l in orig_list].extend([a,b])) # add orig val to list
    print('orig_list=', orig_list)
    print('combo=', combo)
    
    tmp = [l for l in orig_list]
    print('tmp=', tmp, 'a=',a,'b=',b,' orig_list = ', orig_list)
    combo.append([tmp.append(a + b)])
    tmp = [l for l in orig_list]
    tmp.append(a - b)
    print('tmp=', tmp)
    combo.append(tmp)
    
    """
    tmp = [l for l in orig_list]
    combo.append([tmp.append(b - a)])
    tmp = [l for l in orig_list]
    combo.append([tmp.append(a * b)])
    tmp = [l for l in orig_list]
    combo.append([tmp.append(a / b)])  # check for null remainder
    tmp = [l for l in orig_list]
    combo.append([tmp.append(b / a)])  # check for null remainder
    """
    print('combo=', combo)
    return combo
    

    
if __name__ == '__main__':
    main()
