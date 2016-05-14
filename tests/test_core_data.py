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
        f = mod_core.CoreDataWhat('Food')
        self.assertEqual(str(f) , 'Food (type=what)') 
        f.expand('List', ['Apples', 'Chops', 'Cheese'])
        self.assertEqual(str(f.drill_down()[0]) , 'Apples') 
        self.assertEqual(str(f.drill_down()[1]) , 'Chops') 
        self.assertEqual(str(f.drill_down()[2]) , 'Cheese') 
        self.assertEqual(f.drill_up() , None) # TODO - keep track of location of graph 

    def test_03_events(self):
    
        # Events
        e = mod_core.CoreDataWhen('Sales Meeting', ['2015-04-11', 'Office', 'Meet with client to discuss custom software'])
        self.assertEqual(len(e.format_csv()), 85)
        self.assertEqual(len(e.format_dict()), 104)
        self.assertEqual(str(e), 'Sales Meeting (type=when)')
        
    def test_04_detailed_core_data_usage(self):
        root = mod_core.CoreDataWhat('Everything')

        # add the domains
        root.expand('List', ['Food', 'Projects', 'Software'])

        # define a domain and instantiate a class (example - you 
        # dont do this in day to day usage
        food = root.get_child_by_name('Food')

        # for the Food - expand it further
        food.expand('List', ['Apples', 'Chops', 'Cheese'])
        self.assertEqual(str(food)[0:4],'Food')
        self.assertEqual(str(food.parent),'Everything (type=what)')
        

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
        self.assertEqual(str(proj.contract('TODO - set process')), 'Everything (type=what)')
        
        
    def test_05_save_a_table(self):
        try:
            os.remove(test_fldr + os.sep + 'Events2015.user01')
        except Exception:
            print('file not found, but we dont care')
        
        #ev = mod_core.CoreTable(config.fldrs['log_folder'], tpe='Events', user='user01', header=['date', 'category', 'details'])
        ev = mod_core.CoreTable(test_fldr, tpe='Events', user='user01', header=['date', 'category', 'details'])
        ev.add(mod_core.CoreDataWhen('Sales Meeting', ['2014-01-11', 'Office', 'Catchup with client']))
        ev.add(mod_core.CoreDataWhen('Sales Meeting#3', ['2015-03-11', 'Office', 'Catchup with client']))
        ev.add(mod_core.CoreDataWhen('DEV AIKIF - core data', ['2015-05-11', 'Software', 'update TEST - no test for CORE_DATA']))
        ev.add(mod_core.CoreDataWhen('DEV LifePim - core data', ['2015-03-11', 'Software', 'use data for LifePim']))
        ev.add(mod_core.CoreDataWhen('DEV AIKIF - data tools', ['2015-05-11', 'Software', 'fix data tools ']))
        ev.save()
        with open(test_fldr + os.sep + 'Events2015.user01', 'r') as f:
            txt = f.read()
        self.assertEqual(len(txt), 353)
        ev.generate_diary()
        
    def test_06_core_table(self):
        ob = mod_core.CoreTable(test_fldr, tpe='Object', user='user03', header=['code', 'desc'])
        self.assertEqual(len(str(ob)) > 50, True)
        self.assertEqual(ob.get_filename('2999'), test_fldr + os.sep + 'Object2999.user03')
        
       
    def test_10_links_to(self):
        f = mod_core.CoreDataWhat('Food')
        r = mod_core.CoreDataWhat('Recipe')
        f.links_to('Recipe', 'Process')
        self.assertEqual(f.links, [['Recipe', 'Process']])
        self.assertRaises(Exception, f.links_to, 'Recipe', 'WRONG_TYPE')
        
    def test_21_core_data_who(self):
        l = mod_core.CoreDataWho('Frank', ['Frank', 'Physical', 'Customer'])
        self.assertEqual(str(l) , 'Frank (type=who)')
        self.assertEqual(l.type_desc , 'Character')
        self.assertEqual(l.data_type , 'who')
       
    def test_22_core_data_what(self):
        l = mod_core.CoreDataWhat('Apple')
        self.assertEqual(len(l.format_csv()) >  5, True)
        self.assertEqual(str(l) , 'Apple (type=what)')
        self.assertEqual(l.type_desc , 'Object')
        self.assertEqual(l.data_type , 'what')
       
    def test_23_core_data_where(self):
        l = mod_core.CoreDataWhere('Office', ['Office', 'Physical', '2 Downing St, London'])
        self.assertEqual(len(l.format_csv()) >  5, True)
        self.assertEqual(str(l) , 'Office (type=where)')
        self.assertEqual(l.type_desc , 'Location')
        self.assertEqual(l.data_type , 'where')
       
    def test_24_core_data_when(self):
        l = mod_core.CoreDataWhen('Sales Meeting', ['Meet with Clients'])
        self.assertEqual(len(l.format_csv()) >  5, True)
        self.assertEqual(str(l) , 'Sales Meeting (type=when)')
        self.assertEqual(l.type_desc , 'Event')
        self.assertEqual(l.data_type , 'when')
        
    def test_25_core_data_how(self):
        l = mod_core.CoreDataHow('Automatic Backup', ['./backup.py'])
        self.assertEqual(len(l.format_csv()) >  5, True)
        self.assertEqual(str(l) , 'Automatic Backup (type=how)')
        self.assertEqual(l.type_desc , 'Process')
        self.assertEqual(l.data_type , 'how')
 
    def test_26_core_data_why(self):
        l = mod_core.CoreDataWhy('List of Countries', [{'src_file':'countries.csv','bias':0.9}])
        self.assertEqual(len(l.format_csv()) >  5, True)
        self.assertEqual(str(l) , 'List of Countries (type=why)')
        self.assertEqual(l.type_desc , 'Fact')
        self.assertEqual(l.data_type , 'why')
        self.assertEqual(l.data[0]['src_file'] , 'countries.csv')
        self.assertEqual(l.data[0]['bias'] , 0.9)
        csv_str = l.format_csv()  # "List of Countries","{'src_file': 'countries.csv', 'bias': 0.9}",
        self.assertTrue('"List of Countries","{' in csv_str)
        self.assertTrue("'src_file': 'countries.csv'" in csv_str)
        self.assertTrue("'bias': 0.9" in csv_str)
        
        
    def test_30_duplicate_nodes(self):
        """
        test to demonstrate how core data handles
        copies of nodes and duplicate named nodes
        """
        person1 = mod_core.CoreDataWho('Tolkien', [{'first_name':'John', 'type':'person', 'occupation':'Author'}])
        person2 = mod_core.CoreDataWho('Bilbo', [{'knownas':'Bilbo Baggins', 'type':'fictional', 'occupation':'Thief'}])
        self.assertFalse(person2 == person1)   # confirm objects aren't same for different names

        person3 = person1
        self.assertTrue(person3 == person1)  # confirm assign new object is the same
        
        person4 = mod_core.CoreDataWho('Tolkien', [{'first_name':'Christopher', 'type':'person', 'occupation':'Author'}])
        #print('person4 = ', person4)
        
        self.assertEqual(person4.name,person1.name)  # confirm names same for object
        self.assertFalse(person4 == person1)         # but they are different object
   
        
        
if __name__ == '__main__':
    unittest.main()