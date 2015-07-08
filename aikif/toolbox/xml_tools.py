#!/usr/bin/python3
# coding: utf-8
# xml_tools.py
# XmlBreaker based on nicwolff's code - https://gist.github.com/nicwolff/b4da6ec84ba9c23c8e59
# fast_parse based on http://www.ibm.com/developerworks/xml/library/x-hiperfparse/ via
#   http://stackoverflow.com/questions/7171140/using-python-iterparse-for-large-xml-files

import os
import sys
from xml.sax import parse
from xml.sax.saxutils import XMLGenerator

from xml.etree.ElementTree import iterparse

try:
    from lxml import etree
except ImportError:
    print('you need to pip install lxml')

def TEST():
    #print('Split a large XML file into multiple files')
    #split_xml('ANC__WhereToHongKong.xml', 'annotationSet', 10)

    
    print(count_elements('ANC__WhereToHongKong.xml', 'sentence'))
    #print('Fast processing of XML files')
    #context = etree.iterparse( 'short.xml', tag='layer' )
    #fast_iter(context,process_element)
    
    
# Public facing functions
###############################

def split_xml(fname, element, num_elements):    
    parse(fname, XMLBreaker(element, break_after=num_elements, out=CycleFile(fname)))

def count_elements(fname, element):
    """
    returns (511, 35082) for ANC__WhereToHongKong.xml
    """
    num = 0
    tot = 0
    for event, elem in iterparse(fname):
        tot += 1
        if elem.text != '':
            print(' tag  = ', elem.tag)
            #print(' event  = ', event   # always end
            print(' text = ',  elem.text)
        if element in elem.tag:
            #print(elem.xpath( 'description/text( )' ))
            print(elem.text)
            num += 1
            elem.clear()
    return num, tot
    
    
# internal classes for toolkit
###############################

def fast_iter(context, func, *args, **kwargs):
    """
    http://lxml.de/parsing.html#modifying-the-tree
    Based on Liza Daly's fast_iter
    http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
    See also http://effbot.org/zone/element-iterparse.htm
    """
    for event, elem in context:
        func(elem, *args, **kwargs)
        # It's safe to call clear() here because no descendants will be
        # accessed
        elem.clear()
        # Also eliminate now-empty references from the root node to elem
        for ancestor in elem.xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]
    del context

def process_element(elem):
    print(elem.xpath( 'description/text( )' ))


class CycleFile(object):

    def __init__(self, filename):
        self.basename, self.ext = os.path.splitext(filename)
        self.index = 0
        self.open_next_file()

    def open_next_file(self):
        self.index += 1
        filename = self.basename + str(self.index) + self.ext
        self.file = open(filename, 'w')

    def cycle(self):
        self.file.close()
        self.open_next_file()

    def tell(self):
        self.file.tell()

    def write(self, txt):
        if type(txt) is str:
            self.file.write(txt)
        else:
            self.file.write(txt.decode('utf-8'))

    def writelines(sequence):
        self.file.writelines(sequence)

    def flush(self):
        self.file.flush()

    def close(self):
        self.file.close()

class XMLBreaker(XMLGenerator):
    
    def __init__(self, break_into=None, break_after=200, out=None, *args, **kwargs):
        XMLGenerator.__init__(self, out, *args, **kwargs)
        self.out_file = out
        self.break_into = break_into
        self.break_after = break_after
        self.context = []
        self.count = 0

    def start_element(self, name, attrs):
        XMLGenerator.start_element(self, name, attrs)
        self.context.append((name, attrs))

    def end_element(self, name):
        XMLGenerator.end_element(self, name)
        self.context.pop()
        if name == self.break_into:
            self.count += 1
            if self.count >= self.break_after:
                self.count = 0
                for element in reversed(self.context):
                    self.out_file.write("\n")
                    XMLGenerator.end_element(self, element[0])
                self.out_file.cycle()
                for element in self.context:
                    XMLGenerator.start_element(self, *element)


if __name__ == '__main__':
    TEST()	
 





