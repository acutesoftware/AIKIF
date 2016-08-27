#!/usr/bin/python3
# coding: utf-8
# decorators.py

def debug(fn):
    def wrapper(*args):
        res = fn(*args)
        print (fn.__name__ + ' ' +  str(args) + ': ' + str(res))
        return res
    return wrapper
