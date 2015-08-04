# test_core_data.py

import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif'

sys.path.append(pth)
import core_data as mod_core

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")

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

    def test_03_events(self):
    
        # Events
        e = mod_core.Event('Sales Meeting', ['2015-04-11', 'Office', 'Meet with client to discuss custom software'])
        self.assertEqual(len(e.format_csv()), 85)
        self.assertEqual(len(e.format_dict()), 104)
        
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

        # contract (or rollup - ie get parent) the shelf - NOT IMPLEMENTED
        #self.assertEqual(str(shelf.contract()), 'Projects')
        self.assertEqual(1,2)


        
if __name__ == '__main__':
    unittest.main()