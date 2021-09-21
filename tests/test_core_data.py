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
        self.assertEqual(f.format_all(),"""
--- Format all : Food -------------
 parent = None
 child = Apples
 child = Chops
 child = Cheese
 links = None
""")



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

        self.assertEqual(proj.format_all(), """
--- Format all : Projects -------------
 parent = Everything (type=what)
 child = Install Shelf
 child = AIKIF
 child = Prepare Sales Report
 links = None
""")

    def test_05_save_a_table(self):
        try:
            os.remove(test_fldr + os.sep + 'Events2015.user01')
        except Exception:
            print('file not found, but we dont care')

        ev = mod_core.CoreTable(test_fldr, tpe='Events', user='user01', header=['date', 'category', 'details'])
        ev.add(mod_core.CoreDataWhen('Sales Meeting', ['2014-01-11', 'Office', 'Catchup with client']))
        ev.add(mod_core.CoreDataWhen('Sales Meeting#3', ['2015-03-11', 'Office', 'Catchup with client']))
        ev.add(mod_core.CoreDataWhen('DEV AIKIF - core data', ['2015-05-11', 'Software', 'update TEST - no test for CORE_DATA']))
        ev.add(mod_core.CoreDataWhen('DEV LifePim - core data', ['2015-03-11', 'Software', 'use data for LifePim']))
        ev.add(mod_core.CoreDataWhen('DEV AIKIF - data tools', ['2015-05-11', 'Software', 'fix data tools ']))
        ev.save('2015')
        with open(test_fldr + os.sep + 'Events2015.user01', 'r') as f:
            txt = f.read()
        self.assertEqual(len(txt), 353)
        ev.generate_diary()


        srch = ev.find('Sales')
        self.assertEqual(str(srch[0]), 'Sales Meeting (type=when)')
        self.assertEqual(str(srch[1]), 'Sales Meeting#3 (type=when)')

        srch2 = ev.find('data')
        self.assertEqual(len(srch2), 3)

        # now save with header
        ev.save('2015', add_header='Y')
        with open(test_fldr + os.sep + 'Events2015.user01', 'r') as f:
            txt = f.read()
        self.assertEqual(len(txt), 735)



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
        self.assertEqual(person4.name,person1.name)  # confirm names same for object
        self.assertFalse(person4 == person1)         # but they are different object


    def test_40_linking_overview(self):
        """
        shows usage on general linking of objects using a Fact.
        Note - work in progress, none of these methods allow for
        any real discoverability without contrived coding / searching
        in datasets.
        """
        ob_cat = mod_core.CoreDataWhat('Cat', [{'genus':'Felis', 'is_tameable':True}])

        # option 1 - link via data (though difficult to autosearch)
        pet1 = mod_core.CoreDataWho('Tiddles', [{'obj_type':ob_cat, 'type':'animal', 'likes':'Fish'}])
        self.assertEqual(pet1.name, 'Tiddles')
        self.assertEqual(pet1.data[0]['obj_type'], ob_cat)
        self.assertEqual(pet1.data[0]['obj_type'].data[0]['is_tameable'], True)

        # option 2 - link 2 objects with 3rd 'Fact' object
        pet2 = mod_core.CoreDataWho('Meatball', [{'type':'cat', 'likes':'Fish'}])
        self.assertEqual(pet2.name, 'Meatball')
        pet2.links_to(ob_cat, 'Character')
        self.assertEqual(pet2.links, [[ob_cat, 'Character']])

        # option 3 - link objects via parent / child
        ob_dog = mod_core.CoreDataWhat('Dog', [{'genus':'Canis', 'is_tameable':True}])
        pet3 = mod_core.CoreDataWho('Rover', data=[{'type':'dog'}], parent=ob_dog)
        self.assertEqual(pet3.name, 'Rover')
        self.assertEqual(pet3.parent, ob_dog)
        self.assertEqual(pet3.parent.name, 'Dog')

    def test_42_object_drilldown_detailed(self):
        """
        demonstrate how mulitple drilldowns can work
        """
        asset =  mod_core.CoreDataWhat('Asset')
        f = mod_core.CoreDataWhat('Furniture', parent = asset)
        chair = mod_core.CoreDataWhat('Chair', parent=f)
        table = mod_core.CoreDataWhat('Table', parent=f)
        cupboard = mod_core.CoreDataWhat('Cupboard', parent=f)

        tradeperson = mod_core.CoreDataWho('Trade Person')
        carpenter = mod_core.CoreDataWho('Carpenter', parent=tradeperson)

        f.links_to(chair, 'Object')
        f.links_to(table, 'Object')
        f.links_to(cupboard, 'Object')

        f.links_to(carpenter, 'Character')

        self.assertEqual(str(f) , 'Furniture (type=what)')
        f.expand('List', [table, chair, cupboard])

        wood = mod_core.CoreDataWhat('Wood', parent = mod_core.CoreDataWhat('Material'))
        leather = mod_core.CoreDataWhat('Leather', parent = mod_core.CoreDataWhat('Material'))
        wood.links_to(chair, 'Object')
        wood.links_to(table, 'Object')
        wood.links_to(cupboard, 'Object')
        leather.links_to(chair, 'Object')


        woodwork = mod_core.CoreDataHow('Woodwork')
        build_chair =  mod_core.CoreDataHow('Build Chair', parent=woodwork)
        bld_assemble_legs =  mod_core.CoreDataHow('Assemble Chair Legs', parent=build_chair)
        bld_cut_wood =  mod_core.CoreDataHow('Cut Wood for chair', parent=build_chair)
        bld_measure =  mod_core.CoreDataHow('Measure Wood for chair', parent=build_chair)
        build_chair.links_to(bld_assemble_legs, 'Process')
        build_chair.links_to(bld_cut_wood, 'Process')
        build_chair.links_to(bld_measure, 'Process')

        chair.links_to(build_chair, 'Process')

        self.assertEqual(str(chair.format_all()),"""
--- Format all : Chair -------------
 parent = Furniture (type=what)
 child = None
 links = Build Chair (type=how)
   sublink = Assemble Chair Legs (type=how)
   sublink = Cut Wood for chair (type=how)
   sublink = Measure Wood for chair (type=how)
""")

        f.expand('Built via', [wood, leather])
        self.assertEqual(f.drill_up() , asset)
        self.assertEqual(chair.drill_up() , f)

        print(wood.format_all())
        # this returns a str error type CoreDataWhat - print(f.format_all())
        #print(build_chair.format_all())


    def test_50_extract_csv_to_fact(self):
        """
        read a CSV file to facts
        and parse it to CoreData obects
        """

        import aikif.dataTools.cls_datatable as cl
        fle = cl.DataTable(os.path.join(pth, 'data', 'core', 'LOCATION_WORLD.csv'), ',')
        fle.load_to_array()

        csv_res = ''
        for row in fle.arr:
            r = mod_core.CoreDataWhy(row[1], [{'code':row[1],'name':row[2]}])
            csv_res += r.format_csv()
            self.assertEqual(r.name, row[1])
        self.assertTrue('"COD","' in csv_res)
        self.assertTrue('\'name\': \'LABEL\'' in csv_res)
        self.assertTrue('\'code\': \'COD\'' in csv_res)
        self.assertTrue('\'West Bank\'' in csv_res)
        self.assertEqual(len(csv_res), 12163)


    def test_51_map_csv_to_fact(self):
        """
        use the mapper to define how to map a CSV file to facts
        and parse it to CoreData obects
        """
        import mapper
        raw_file = os.path.join(pth, 'data', 'core', 'LOCATION_WORLD.csv')

        mapPC_Usage = mapper.Mapper(os.path.join(os.path.join(pth, 'data', 'raw'), 'country.map'))
        tot, vals, grps, events = mapPC_Usage.process_raw_file(raw_file, ["id","code","name"])
        self.assertEqual(tot, 261)
        self.assertEqual(len(vals), 785)
        self.assertEqual(len(grps), 786)
        self.assertEqual(len(events), 0)


    def test_60_example_notes(self):
        note_pc = mod_core.CoreDataWhat('PC:Install')
        note_steam = mod_core.CoreDataWhat('Games:Steam', parent=note_pc)
        note_git = mod_core.CoreDataWhat('Programming:Git', parent=note_pc)
        note_pc.expand('', [note_steam.name,note_git.name] )

        print(note_git)
        print(note_steam)
        print(note_pc)

        #print('child_nodes of note_pc = ', note_pc.child_nodes)

        for c in note_pc.child_nodes:
            #print('c  = ' , str(c))
            #print('c.parent  = ' , c.parent)
            self.assertEqual(str(c.parent), 'PC:Install (type=what)')


        res = note_pc._get_all_children()
        print(res)
        self.assertEqual(res, ' child = Games:Steam\n child = Programming:Git\n')




if __name__ == '__main__':
    unittest.main()
