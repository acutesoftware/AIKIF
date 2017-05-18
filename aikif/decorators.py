#!/usr/bin/python3
# coding: utf-8
# decorators.py
import time

def debug(fn):
    def wrapper(*args):
        res = fn(*args)
        print((fn.__name__ + ' ' +  str(args) + ': ' + str(res)))
        return res
    return wrapper

def show_timing(fn):
    def wrapper(*args):
        start_time = time.time()
        res = fn(*args)
        end_time = time.time()
        print(('Timing Function : ', fn.__name__, ' with args ', str(args), '\ntook ' , end_time - start_time, ' milliseconds'))
        return res
    return wrapper