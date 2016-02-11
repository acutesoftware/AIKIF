#!/usr/bin/python3
# coding: utf-8
# test_mapper.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)
print(root_fldr)

fldr_raw_data = os.path.join(root_fldr, 'data', 'raw')
print(fldr_raw_data)

import config as mod_cfg
import mapper as mod_map

class MapTest(unittest.TestCase):
    
    def setUp(self):
        """ gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.mymap = mod_map.Mapper(mod_map.map_file)
        
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    """ 
    tests for maps go below - use mymap instantiated object
    """
    def test_01_instantiate(self):
        self.assertEqual(len(str(self.mymap)) > 500, True)

    def test_11_process_text_1(self):
        res = self.mymap.identify_data('text', 'hello world')
        self.assertEqual(res , 4)

    def test_12_process_file_1(self):
        res = self.mymap.identify_data('file', 'test.csv')
        self.assertEqual(res , 10)

    def test_13_process_unknown(self):
        res = self.mymap.identify_data('blah blah', 'SOME_STUFF')
        #print(res)
        self.assertEqual(res , 0)
        
        
    def test_20_save_mapping(self):
        self.mymap.save_rules('rules_saved.txt')
        self.assertTrue(os.path.exists('rules_saved.txt'))
    
    def test_24_create_map_from_file(self):
        self.mymap.create_map_from_file(mod_map.sample_datafile)
        self.assertTrue(os.path.exists(mod_map.sample_datafile + '.rule' ))
     
    def test_30_map_columns(self):
        mc = mod_map.MapColumns(mod_map.map_file)
        self.assertTrue(len(str(mc)) > 10)
        
    
    def test_31_MapColumn(self):
        mc = mod_map.MapColumn('table,column,data_type,aikif_map,aikif_map_name,extract,format,where,index,')
        #print(mc)
        self.assertEqual(mc.table, 'table')
        self.assertEqual(mc.column, 'column')
        self.assertEqual(mc.data_type, 'data_type')
        self.assertEqual(mc.aikif_map, 'aikif_map')
        self.assertEqual(mc.aikif_map_name, 'aikif_map_name')
        self.assertEqual(mc.extract, 'extract')
        self.assertEqual(mc.format, 'format')
        self.assertEqual(mc.where, 'where')
        self.assertEqual(mc.index, 'index')
        
        self.assertEqual(str(mc)[0:41], ' Map Column\ntable : table\ncolumn : column')
        self.assertEqual(len(str(mc)), 180)
      
    
    def test_90_get_maps_stats(self):
        mc = mod_map.Mapper(mod_map.map_file)
        #print(mc)
        stats = mc.get_maps_stats()
        #print(stats)
        self.assertTrue(stats,  {'file': 10, 'text': 4})
    

    def test_40_read_raw_file(self):
        mapPC_Usage = mod_map.Mapper(os.path.join(fldr_raw_data, 'PC_Usage.map'))
        flds = ['Date', 'Time', 'Length', 'Caption']
        tot, vals = mapPC_Usage.process_raw_file(os.path.join(fldr_raw_data, 'sample_PC_usage.txt'), flds)
        print(tot, vals)
        self.assertEqual(tot, 17)  # note that tot starts from zero, meaning 18 lines in file
        self.assertEqual(len(vals), 8)
        self.assertEqual(vals[0], 'C:\\Windows\\system32\\cmd.exe')
    
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        #print(str(self.mymap))
        pass
    
if __name__ == '__main__':
    unittest.main()
