#!/usr/bin/python3
# -*- coding: utf-8 -*-
# transpose.py

import sys
import os


class Transpose(object):
    """
    main transpose object
    """
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return str(self.data)