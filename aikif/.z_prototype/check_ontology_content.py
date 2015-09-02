# check_ontology_content.py

import os
import yaml
import pprint

def main():
    """
    checks for content, mainly to show how to access
    the various sections
    
    examples
    print('', len())
    t = y['Event']
    """
    with open(os.path.join('..','data','ref','ontology.yaml'), 'r') as stream:
        y = yaml.safe_load(stream)
    
    pprint.pprint(y) 
    
    # Top level tests
    for top in y:
        print('Top level : ', top)
    
    # 2 levels
    print_2_levels(y)
    
    #t = y['Event']
    #print('t = y[Event]', len(t), t)
    
    # print individual elements
    print('[Location][Virtual] [len:' + str(len(y['Location']['Virtual'])) + '] = ', y['Location']['Virtual'])
    print('[Location][Virtual][Website] [len:' + str(len(y['Location']['Virtual']['Website'])) + '] = ', y['Location']['Virtual']['Website'])
    
    print('[Location][Virtual][Website][0] [len:' + str(len(y['Location']['Virtual']['Website'][0])) + '] = ', y['Location']['Virtual']['Website'][0])
    print('[Location][Virtual][Website][1] [len:' + str(len(y['Location']['Virtual']['Website'][1])) + '] = ', y['Location']['Virtual']['Website'][1])
    
    print('[Location][Physical][1] [len:' + str(len(y['Location']['Physical'][1])) + '] = ', y['Location']['Physical'][1])

    print('[People][Label_Friendly] [len:' + str(len(y['People']['Label_Friendly'])) + '] = ', y['People']['Label_Friendly'])
    print('[Object][Physical][Materials] [len:' + str(len(y['Object']['Physical']['Materials'])) + '] = ', y['Object']['Physical']['Materials'])
  
    # find specific items
    print('People = ', search_dict(y, 'People'))
    print('Virtual = ', search_dict(y, 'Virtual'))
    print('Profession = ', search_dict(y, 'Profession'))
    print('Student = ', search_dict(y, 'Student'))
 
    # recursively print ontology
    print_ontology(y, '  ', '')
    
    print('\n-== Viewing Dictionary in dot notation ==-')
    z = DictView(y)
    print(z.Event)
    print(z.People)
    print(z.Object['Virtual'])   # doesnt seem to work in dot notation past level 1
                                 # SEE mini lib to do this - https://github.com/tardyp/dictns
                                 # also bunch = https://github.com/dsc/bunch
                                 
                                 

class DictView(object):
    def __init__(self, d):
        self.__dict__ = d
    
def print_2_levels(dct):
    for d in dct:
        print(d)
        #for num, l2 in enumerate(dict[d]):
        for num, l2 in enumerate(dct[d]):
            print(' - ' , str(l2))
            try:
            #if type(dct[d][num]) is list:
                for l3 in dct[d][l2]:
                    print('   - ' , str(l3))    
            except Exception as ex:
                print('     [no more breakdowns] ')

def print_ontology(dct, level_spacing = '  ', space_char = '-'):
    print('====================== print_ontology ================')
    #if not isinstance(dct, dict):
        #print(dct + ' is not a dictionary')
    #    print(dct)
        #print_ontology(dct, level_spacing, space_char)
    #else:
    if isinstance(dct, str):
        print(dct)
    else:
        for k,v in dct.items():
            if isinstance(k, dict):    
                print_ontology(k, level_spacing, space_char)
            else:
                print(level_spacing + str(v))
        
def search_dict(dct, key):
    stack = [dct]
    while stack:
        d = stack.pop()
        if key in d:
            return d[key]
        for k, v in d.items():
            if isinstance(v, dict):
                stack.append(v)
                
main()    