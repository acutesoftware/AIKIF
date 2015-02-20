# example_solve_happiness.py   written by Duncan Murray 8/2/2015

import os
import sys
import random

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
env_folder = root_folder + os.sep + 'environments' 
#sys.path.append(root_folder)
sys.path.append(env_folder)

import happiness as mod_hap_env

people_list = []
people_list.append(['Gand', {'tax_min':0.3, 'tax_max':0.5, 'tradition':0.2, 'equity':0.9}])
people_list.append(['Trsa', {'tax_min':0.0, 'tax_max':0.9,'tradition':0.4, 'equity':0.9}])
people_list.append(['Whtv', {'tax_min':0.1, 'tax_max':0.9,'tradition':0.1, 'equity':0.3}])
people_list.append(['Mrdk', {'tax_min':0.0, 'tax_max':0.2,'tradition':0.8, 'equity':0.1}])

def main():
    all_people = []
    for p in people_list:
        all_people.append(mod_hap_env.Person(p[0], p[1]))
    all_people = create_random_population(num=100)
    utopia = mod_hap_env.WorldFinder(all_people)
    utopia.solve(silent=False)
    print(utopia)
    """
    print('people_list')
    print(people_list)
    print('ALL_PEOPLE')
    print(all_people)
    """
    

############# Utility functions ############
def create_random_population(num=100, diversity=0.4):
    """
    create a list of people with randomly generated names and stats
    """
    people = []
    for _ in range(num):
        nme = 'blah'
        tax_min = random.randint(1,40)/100
        tax_max = tax_min + random.randint(1,40)/100
        tradition = random.randint(1,100)/100
        equity = random.randint(1,100)/100
        pers = mod_hap_env.Person(nme, {'tax_min':tax_min, 'tax_max':tax_max, 'tradition':tradition, 'equity':equity})
        people.append(pers)
        #print(pers)

    return people
if __name__ == '__main__':
    main()
