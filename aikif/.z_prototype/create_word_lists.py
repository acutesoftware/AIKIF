# coding: utf-8
# create_word_lists.py   written by Duncan Murray 3/2/2014
# creates a simple list of verbs, nouns and adjectives for 
# simple 'bag of words' parsing.
# First implementation uses the following dataset:
#     WordNet 3.1 Copyright 2011 by Princeton University.

import os
import sys
from xml.dom.minidom import parse, parseString
import xml
sys.path.append('..//..//aspytk')
#import as_util_data as dat
import lib_data as dat
import lib_file as fle
import xml.etree.ElementTree as ET

ontologyClassificationFile = 'S:\\DATA\\opendata\\ontology\\wikipedia_categories\\dbpedia-ontology.owl.bz2.owl.bz2.owl'
ipFolder = 'S://DATA//opendata//datasets//dict//'
opFolder = '..//data//ref//'  # os.getcwd()

def SaveListFirstWordOnly(msg, ipfile, opFile):
    numRecs = 0
    opList = []
    rawList = dat.ReadFileToList(ipfile)
    for line in rawList:
        if line[0:1] != ' ':
            numRecs = numRecs  + 1
            noun = line[0:line.find(' ')]
            opList.append(noun)
    dat.SaveListToFile(opList, opFile)
    print(('Saved ' + str(numRecs) + ' ' + msg))
    return numRecs

def ExtractListOfWords():
    # ----  get the list of nouns, adverbs and adjectives ---- 
    numRecs = SaveListFirstWordOnly('nouns', ipFolder + 'index.noun', opFolder + 'nounList.txt')
    numRecs = SaveListFirstWordOnly('adverbs', ipFolder + 'index.adv', opFolder + 'advList.txt')
    numRecs = SaveListFirstWordOnly('adjectives', ipFolder + 'index.adj', opFolder + 'adjList.txt')

    # ---- get the list of verbs ---- (need some stemming here)
    numRecs = 0
    verbList = []
    rawList = dat.ReadFileToList(ipFolder + 'index.verb')
    for line in rawList:
        if line[0:1] != ' ':
            numRecs = numRecs  + 1
            verb = line[0:line.find(' ')]
            verbList.append(verb)
            verbList.append(verb + 's')  # turns play to plays  - TODO, use stemming algorithm
            verbList.append(verb + 'ed')
    dat.SaveListToFile(verbList, opFolder + 'verbList.txt')    
    print(('Saved ' + str(numRecs) + ' verbs'))


def ExtractCat(fname, opFile):

    #Look at the wikipedia categories - no - far too detailed
    #S:\DATA\opendata\ontology\wikipedia_categories\articlecategories_en.csv.bz2.csv.bz2.csv
    #ipFile = 'S:\\DATA\\opendata\\ontology\\wikipedia_categories\\articlecategories_en.csv.bz2.csv.bz2.csv'
    # ipFile = 'S:\\DATA\\opendata\\ontology\\wikipedia_categories\\articlecategories_en.csv.bz2.csv.bz2.csv'
    # headFile = 'S:\\DATA\\opendata\\ontology\\wikipedia_categories\\articlecategories_head.csv'
    # sampleFile = 'S:\\DATA\\opendata\\ontology\\wikipedia_categories\\articlecategories_sample.csv'
    # dat.unix_head(ipFile, headFile, 5000)
    # dat.getPercentRandomRecords(ipFile, sampleFile, 1)

    # Later
    # infoboxproperties_en.csv.bz2.csv.bz2 = list of properties or labels (name, age, BestBowlerFirstInnings, PilotName, ProducerAge, etc)

    # ontology is in RDF format
    print((fname + ' = ' + str(dat.countLinesInFile(fname)) + ' rows' ))

     
    
  #  dom = xml.dom.minidom.parse( fname )   # parse an XML file
    #print (dom1.toxml())
   # dom.findall('owl:DatatypeProperty', namespaces=namespaces)
#    for node in dom.getElementsByTagName('DatatypeProperty'):  # visit every node <bar />
    numFound = 0
    categories = []
    dom = parse( ontologyClassificationFile )
    for node in dom.getElementsByTagName('rdfs:label'):  # visit every node <bar />
        #print (node.toxml())
        numFound = numFound + 1
        cat = dat.StriptHTMLtags(node.toxml()) 
        print(cat)
        categories.append(cat)
        
        #print ('subclasses = ')
        #for sub in node.findall('subClassOf'):
        #    print (sub.toxml())
    dat.SaveListToFile(categories, opFile)
    return numFound 

def GetOntologyExtract(fname, txt):
    numFound = 0
    # see http://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-elementtree
    namespaces = {'owl': 'http://www.w3.org/2002/07/owl#'} # add more as needed
    #namespaces = {'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'}
    print(('Extracting ' + txt ))
    tree = ET.parse(fname)
    doc = tree.getroot()
    #nodes = doc.findall('owl:Class', namespaces=namespaces)
    nodes = doc.findall(txt, namespaces=namespaces)
    #nodes = doc.findall('rdfs:label', namespaces=namespaces)
    print(('found ' + str(len(nodes)) + ' nodes\n ' ))
    for node in nodes:
        numFound = numFound + 1
        for itm in list(node.items()):
            print((itm[1][28:]))
        #print(node.tail)    
   # find_in_tree(root,"myNode")
        #print(node.attrib)
        #print(len(node))
        #print(node.get('rdfs'))
        #print('node.text= ' + node.text)
        #print('node.tag = ' + node.tag)
    return numFound
        
        
        
#-----------------------------------------------------------#
#                 Build a Master Word List                  #
#-----------------------------------------------------------#
# Idea is to concatenate unique words from all lists and also 
# names from contacts or baby names list (+country names, etc)
# to create one huge list of ALL words used in english sentences.
# Then, in a table each word has flags like isVerb, isNoun, isAdv,
# isAdjective, isName, isPerson, isPlace
# Once this is built then ANY sentence can be parsed into a list
# of ids instead of storing strings you store a series of numbers.


#    MAIN
opFile = '..\\data\\ref\\ontology_list.txt'
print('create_word_list.py - script to extract lists for AIKIF')
print(('Reading - ' + ontologyClassificationFile))
#ExtractListOfWords()
print(('Extracted ' + str(ExtractCat(ontologyClassificationFile, opFile)) + ' nodes to ' + opFile))
#print('Found ' + str(GetOntologyExtract(ontologyClassificationFile, 'owl:Class')) + ' nodes')
print('Done..')

