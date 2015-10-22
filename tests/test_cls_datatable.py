#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_cls_datatable.py

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder + os.sep + 'dataTools')

import cls_datatable as cl


#root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
save_folder = 'test_results' + os.sep
save_folder = ''  # to get the damn build passing
fname =  save_folder + 'datatable_sample.csv'    
fname2 = save_folder + 'datatable_output.csv'                  
fname3 = save_folder + 'datatable_calcs.csv'     
             
class TestClassDataTable(unittest.TestCase):
    def setUp(self):
        with open(fname, "w") as f:
            f.writelines(
"""TERM,GENDER,ID,tot1,tot2
5300,F,00078,18,66
7310,M,00078,10,12
7310,M,00078,18,465
7310,F,00078,30,2
7310,F,00016,25,12
5300,M,00016,31,0
7310,F,00016,67,873""")
                            
    def test_01_create_file(self):
        
        fle2 = cl.DataTable(fname2, 'file')
        # test edge case first
        fle2.save(fname2, 9)
        
        fle2.save(fname2, ['test data','another line','final line'])
        
         
        fle3 = cl.DataTable(fname3, 'file')
        file_contents = fle2.load(fname)
        self.assertEqual(len(file_contents), 157)  
        fle3.drop(fname)
        
        # try to drop non existant file
        fle3.drop('no such file.bla')
        
    def test_02_percentile(self):
        fl3 = cl.DataTable('', '"')
        self.assertEqual(fl3.percentile([1,2,3,4,5,6], .25), 2.25)
        self.assertEqual(fl3.percentile([1,2,3,4,5,6], .5), 3.5)
        self.assertEqual(fl3.percentile([1,2,3,4,5,6], .75), 4.75)
        self.assertEqual(fl3.percentile([1,2,3,4,5,6,7,8,9,10], .25), 3.25)
        self.assertEqual(fl3.percentile([1,1,2], .5), 1)
        self.assertEqual(fl3.percentile([1,1,2], .25), 1)
        self.assertEqual(fl3.percentile([1,1,2], .75), 1.5)
        
    
    def test_03_get_distinct_values_from_cols1(self):
        fle = cl.DataTable(fname, ',')
        fle.load_to_array()
        dist_cols = fle.get_distinct_values_from_cols(['GENDER'])
        self.assertEqual(sorted(dist_cols), [{'F', 'M'}])

    def test_03_get_distinct_values_from_cols2(self):
        fle = cl.DataTable(fname, ',')
        fle.load_to_array()
        dist_cols = fle.get_distinct_values_from_cols(['TERM'])
        self.assertEqual(sorted(dist_cols), [{'5300','7310'}])

    def test_03_get_distinct_values_from_cols3(self):
        fle = cl.DataTable(fname, ',')
        fle.load_to_array()
        dist_cols = fle.get_distinct_values_from_cols(['TERM', 'ID'])
        self.assertEqual(sorted(dist_cols), sorted([('5300', '00016'), ('5300', '00078'), ('7310', '00016'), ('7310', '00078')]))
        
        # test edge cases
        empty_cols = fle.get_distinct_values_from_cols([])
        self.assertEqual(empty_cols, [])
        
        unimplemented_function = fle.get_distinct_values_from_cols(['a','b','c','d'])
        self.assertEqual(unimplemented_function, -44)

    def test_04_add_cols(self):
        fle = cl.DataTable(fname, ',')
        fle.load_to_array()
        fle.add_cols(['NEW1', 'NEW2'])
        #fle.describe_contents()
        self.assertEqual(fle.get_header(), ['TERM', 'GENDER', 'ID', 'tot1', 'tot2', 'NEW1', 'NEW2'])

    def test_05_update_where1(self):
        fle = cl.DataTable(fname, ',')
        fle.load_to_array()
        dist_cols = fle.get_distinct_values_from_cols(['TERM', 'ID'])
        fle.add_cols(['RNK_tot1', 'RNK_tot2'])
        for new_col in ['tot1', 'tot2']:
            for i in dist_cols:
                first, third, median = fle.calc_percentiles(new_col, ['TERM', 'ID'], [str(i[0]), str(i[1])])
                fle.update_where('RNK_' + new_col, first, ['TERM', 'ID'], [str(i[0]), str(i[1])])
        fle.save_csv(fname3)
        """
        ===========================================================
        TERM    GENDER  ID      tot1    tot2    RNK_tot1RNK_tot2
        5300    F       00078   18      66      18      66
        7310    M       00078   10      12      14.0    7.0
        7310    M       00078   18      465     14.0    7.0
        7310    F       00078   30      2       14.0    7.0
        7310    F       00016   25      12      35.5    227.25
        5300    M       00016   31      0       31      0
        7310    F       00016   67      873     35.5    227.25
        """        
        self.assertEqual(fle.get_header(), ['TERM', 'GENDER', 'ID', 'tot1', 'tot2', 'RNK_tot1', 'RNK_tot2'])
        self.assertEqual(fle.arr[0][3],'18')
        self.assertEqual(fle.arr[0][4],'66')
        self.assertEqual(fle.arr[1][5],14.0)
        self.assertEqual(fle.arr[1][6],7.0)
        self.assertEqual(fle.arr[6][6],227.25)
        
        # update where using col index (updates same column)
        fle.update_where(5, first, ['TERM', 'ID'], [str(i[0]), str(i[1])])
        
        # check edge case for calc_percentiles
        first, third, median = fle.calc_percentiles(new_col, ['TERM', 'ID'], ['dummy', 'no_data'])
        print(first, third, median)
        self.assertEqual(first, 0)
        self.assertEqual(third, 0)
        self.assertEqual(median, 0)
        
        
    def test_06_create_blank_data_structure(self):
        dat = cl.DataTable('sales.csv', ',', col_names=['date', 'amount', 'details'])
        self.assertEqual(dat.col_names[0], 'date')
        self.assertEqual(dat.col_names[1], 'amount')
        self.assertEqual(dat.col_names[2], 'details')
        
 
    def test_07_add_data(self):
        dat = cl.DataTable('sales.csv', ',', col_names=['date', 'amount', 'details'])
        dat.add(['2015-01-09', 24.95, 'Timer'])
        dat.add(['2015-02-17', 45.00, 'Diary'])
        dat.add(['2015-02-19', 24.95, 'Timer'])
        self.assertEqual(len(dat.arr), 3)
        self.assertEqual(len(dat.count_unique_values(0, 'date')), 3)
        self.assertEqual(len(dat.count_unique_values(2, 'details')), 2)
        self.assertEqual(str(dat)[0:23], 'date    amount  details')
        op_rst = dat.format_rst()
        #print(op_rst)
        self.assertEqual(len(op_rst) > 55, True)
        self.assertEqual(dat.get_col_width('date'), 10)

    def test_08_describe_contents(self):
        dat = cl.DataTable('sales.csv', ',', col_names=['date', 'amount', 'details'])
        dat.describe_contents()
        
    def test_09_force_to_string(self):
        dat = cl.DataTable('dud.csv', ',', col_names=['date'])
        self.assertEqual(dat.force_to_string("hi"), 'hi')
        self.assertEqual(dat.force_to_string(123), '123')
        self.assertEqual(dat.force_to_string(0.554554523), '0.554554523')
        self.assertEqual(dat.force_to_string({"a": 5}), '{a=5,}')
        self.assertEqual(dat.force_to_string(['asda', 'ddd']), '[asda,ddd]')
        self.assertEqual(dat.force_to_string(['asda', 213123, 0.55, 'HI']), '[asda,213123,0.55,HI]')
        self.assertEqual(dat.force_to_string(['a',['b','c'], 'd']), '[a,[b,c],d]')

        
        
 
    def test_10_dict_2_string(self):
        dat = cl.DataTable('dud.csv', ',', col_names=['date'])
        self.assertEqual(dat.Dict2String({"a": 5}), 'a=5,')
        
    def test_11_TodayAsString(self):
        self.assertEqual(len(cl.TodayAsString()) > 9, True)
        
    def test_12_get_arr(self):
        fle = cl.DataTable(fname, ',')
        fle.load_to_array()
        self.assertEqual(fle.arr, fle.get_arr())
            
        
        
if __name__ == '__main__':
    unittest.main()
