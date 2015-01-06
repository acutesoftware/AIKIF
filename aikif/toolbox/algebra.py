# algebra.py  written by Duncan Murray 6/1/2015
# functions for toolbox to solve algebra problems

import math
import parser

def TEST():
    formula = '4*(n - 2)**2 + 3'     # works
    formula = '3n**2 + 18n + 25'     # fails
    formula = '3*n**2 + 18*n + 25'   # works
    for n in range(-7, 7):
        evalFunction(formula, n)
        



def evalFunction(formula, n, verbose = 'verbose'):
    answer = 0
    code = parser.expr(formula).compile()
    try:
        answer = eval(code)
    except ZeroDivisionError:
        pass
 #       print('error at value n = ', n)
    if verbose == 'verbose':
        print ('IF n=',n, ' THEN ', formula, ' = ', round(answer, 4))
    return answer

if __name__ == '__main__':        
    TEST()