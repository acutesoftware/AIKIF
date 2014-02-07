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
sys.path.append('..//aspytk')
#import as_util_data as dat
import lib_data as dat
import lib_file as fle
ipFolder = 'S://DATA//opendata//datasets//dict//'
opFolder = os.getcwd()

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
    print ('Saved ' + str(numRecs) + ' ' + msg)
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
    print ('Saved ' + str(numRecs) + ' verbs')


def ExtractCat():

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
    ipFile = 'S:\\DATA\\opendata\\ontology\\wikipedia_categories\\dbpedia-ontology.owl.bz2.owl.bz2.owl'
    print(ipFile + ' = ' + str(dat.countLinesInFile(ipFile)) + ' rows' )

    
    
  #  dom = xml.dom.minidom.parse( ipFile )   # parse an XML file
    #print (dom1.toxml())
   # dom.findall('owl:DatatypeProperty', namespaces=namespaces)
#    for node in dom.getElementsByTagName('DatatypeProperty'):  # visit every node <bar />

    dom = parse( ipFile )
    for node in dom.getElementsByTagName('rdfs:label'):  # visit every node <bar />
        print (node.toxml())


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
print('create_word_list.py')
print('script to extract lists for AIKIF')
#ExtractListOfWords()
ExtractCat()
print('Done..')

