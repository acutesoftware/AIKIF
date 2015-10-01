#!/usr/bin/python3
# -*- coding: utf-8 -*-
# doc_roadmap.py

import os
import sys
import unittest
import yaml
import pprint

def main():
    """
    read the yaml file to generate the roadmap for AIKIF
    """
    #_print_yaml('aikif-roadmap.yaml')
    dat = _read_yaml('aikif-roadmap.yaml')
    create_roadmap_doc(dat, 'roadmap.md')
    #pprint.pprint(dat)

def create_roadmap_doc(dat, opFile):
    """
    takes a dictionary read from a yaml file and converts
    it to the roadmap documentation
    """
    op = format_title('Roadmap for AIKIF')
    for h1 in dat['projects']:
        op += format_h1(h1)
        if dat[h1] is None:
            op += '(No details)\n'
        else:
            for h2 in dat[h1]:
                op += '\n' + format_h2(h2)
                if dat[h1][h2] is None:
                    op += '(blank text)\n'
                else:
                    for txt in dat[h1][h2]:
                        op += '  - ' + txt + '\n'
                        
                        
        op += '\n'

    print(op)
    
def format_title(txt):
    res = txt + '\n'
    res += '===================================================\n'
    return res
    
def format_h1(txt):
    res = txt + '\n'
    res += '---------------------------------------------------\n'
    return res
    
def format_h2(txt):
    res = txt + '\n'
    res += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    return res
    
def _print_yaml(fname):
    print('\n' + fname)
    with open(fname, 'r') as stream:
        print(yaml.load(stream))
     
def _read_yaml(fname):
    with open(fname, 'r') as stream:
        return yaml.load(stream)


if __name__ == '__main__': 
    main()
    
    