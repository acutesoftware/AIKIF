#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_core_data.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif'

sys.path.append(pth)
import core_data as mod_core

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results")

class CoreDataTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.c = mod_core.CoreData('test') 
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.c = None

    def test_01_instantiate(self):
        self.assertEqual(len(str(self.c)) , 4) 
 
    def test_02_object(self):
        f = mod_core.Object('Food')
        self.assertEqual(str(f) , 'Food') 
        f.expand('List', ['Apples', 'Chops', 'Cheese'])
        self.assertEqual(str(f.drill_down()[0]) , 'Apples') 
        self.assertEqual(str(f.drill_down()[1]) , 'Chops') 
        self.assertEqual(str(f.drill_down()[2]) , 'Cheese') 
        self.assertEqual(f.drill_up() , None) # TODO - keep track of location of graph 

    def test_03_events(self):
    
        # Events
        e = mod_core.Event('Sales Meeting', ['2015-04-11', 'Office', 'Meet with client to discuss custom software'])
        self.assertEqual(len(e.format_csv()), 85)
        self.assertEqual(len(e.format_dict()), 104)
        self.assertEqual(str(e), 'Sales Meeting')
        
    def test_04_detailed_core_data_usage(self):
        root = mod_core.Object('Everything')

        # add the domains
        root.expand('List', ['Food', 'Projects', 'Software'])

        # define a domain and instantiate a class (example - you 
        # dont do this in day to day usage
        food = root.get_child_by_name('Food')

        # for the Food - expand it further
        food.expand('List', ['Apples', 'Chops', 'Cheese'])
        self.assertEqual(str(food)[0:4],'Food')
        self.assertEqual(str(food.parent),'Everything')
        

        # describe a 2nd domain
        proj = root.get_child_by_name('Projects')
        proj.expand('List', ['Install Shelf', 'AIKIF', 'Prepare Sales Report'])
        self.assertEqual(str(proj), 'Projects')
        shelf = proj.get_child_by_name('Install Shelf')
        self.assertEqual(str(shelf), 'Install Shelf')

        # try fake name 
        rubbish = proj.get_child_by_name('Something that doesnt exist')
        self.assertEqual(str(rubbish), 'None')

        # contract
        self.assertEqual(str(shelf.contract('')), 'Projects')
        self.assertEqual(str(proj.contract('TODO - set process')), 'Everything')
        
        
    def test_05_save_a_table(self):
        try:
            os.remove(test_fldr + os.sep + 'Events2015.user01')
        except Exception:
            print('file not found, but we dont care')
        
        #ev = mod_core.CoreTable(config.fldrs['log_folder'], tpe='Events', user='user01', header=['date', 'category', 'details'])
        ev = mod_core.CoreTable(test_fldr, tpe='Events', user='user01', header=['date', 'category', 'details'])
        ev.add(mod_core.Event('Sales Meeting', ['2014-01-11', 'Office', 'Catchup with client']))
        ev.add(mod_core.Event('Sales Meeting#3', ['2015-03-11', 'Office', 'Catchup with client']))
        ev.add(mod_core.Event('DEV AIKIF - core data', ['2015-05-11', 'Software', 'update TEST - no test for CORE_DATA']))
        ev.add(mod_core.Event('DEV LifePim - core data', ['2015-03-11', 'Software', 'use data for LifePim']))
        ev.add(mod_core.Event('DEV AIKIF - data tools', ['2015-05-11', 'Software', 'fix data tools ']))
        #print(ev)
        ev.save()
        with open(test_fldr + os.sep + 'Events2015.user01', 'r') as f:
            txt = f.read()
        self.assertEqual(len(txt), 353)
        ev.generate_diary()
        
    def test_06_core_table(self):
        ob = mod_core.CoreTable(test_fldr, tpe='Object', user='user03', header=['code', 'desc'])
        print(ob) 
        self.assertEqual(len(str(ob)) > 50, True)
        self.assertEqual(ob.get_filename('2999'), test_fldr + os.sep + 'Object2999.user03')
        
    def test_07_locations(self):
        l = mod_core.Event('Office', ['Office', 'Physical', '2 Downing St, London'])
        print('location = ', l)
        self.assertEqual(len(l.format_csv()) >  5, True)
        
        
         
if __name__ == '__main__':
    unittest.main()