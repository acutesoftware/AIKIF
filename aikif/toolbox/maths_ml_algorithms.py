# maths_ml_algorithms.py  written by Duncan Murray 20/11/2014
# machine learning algorithms for toolbox in AIKIF

# takes a list of items or table and does standard calculations
# with verbose output (for learning and tracebility)

# confidence, support, lift

import math


def TEST():
    """ local test  """
    ml_entropy([3,3])


def ml_entropy(lst):
    """
    General Machine Learning Formulas
    Intermezzo  - computing Logarithms
    log2(x) = y <=> 2^y = x

    Definition of Entropy

            k
    E = - SUM ( p[i] log2(p[i])
            i=1
    where
             k = possible values enumerated 1,2,...,k
             p[i] = c[i] / n  is the fraction of elements having value [i]
             with c[i] >= 1 the number of i values and
                                        k
                                    n = SUM  c[i]
                                        i=1
                                        
    """
    tot = sum(lst)
    res = 0
    for v in lst:
        if v > 0:
            p = v / tot
            l = math.log( p, 2)
            res += round(p * l, 6)
    res = round(res * -1, 6)
    print('lst = ', lst, 'entropy = ', res)
    return res
  

def ml_weighted_average(lst):
    """ calculate weighted average """
    pass
    
def ml_information_gain(lst):
    pass
    
def ml_gini_index(lst):
    pass
    
def ml_weighted_average(lst):
    pass
    
def ml_support(lst):
    pass
    
def ml_confidence(lst):
    pass
    
def ml_lift(lst):
    pass
    
def ml_apriori(lst):
    pass
    
def ml_process_mining_alpha(lst):
    """
    Alpha Algorithm: A Process Discovery Algorithm
    http://en.wikipedia.org/wiki/Alpha_algorithm
    """
    print('Alpha Algorithm: calculating footprint matrix')
    if len(lst) == 0:
        print('no logs passed')
        return [0]
    else:
        """ TODO """
        return [1]
    
#if __name__ == '__main__':
#    TEST()
    
    
    