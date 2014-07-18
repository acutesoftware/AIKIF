# test_cls_sql_code_generator.py	written by Duncan Murray 25/6/2014

import unittest
import sys
sys.path.append("..\\AI\\dataTools")
from cls_sql_code_generator import SQLCodeGenerator
class TestClassDataSet(unittest.TestCase):
 
    def setUp(self):
        pass
        self.results_folder = 'test_results/'

    def test_full_sql_generation(self):
        
        tst = SQLCodeGenerator('C_FACT_TABLE')
        tst.set_column_list(['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'])

        tst.comment_block('Insert staging records to Fact')
        tst.trunc_fact_table()
        tst.populate_from_staging('RAW_DATA_TABLE', ['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'])

        tst.comment_block('DQ Fixes')
        tst.update_set_where("PRODUCT = 'new name'", "PRODUCT = 'old name'")
        tst.update_old_to_new("CUSTOMER_NAME", "wRong Name", "Corrected Name")
        tst.commit()
        tst.comment_block('Key to Dimensions')
        tst.key_to_dimension('PRODUCT_KEY', 'substr(op.PRODUCT, 1,10)', 'U_PRODUCT_LIST', 'product_name', 'PRODUCT_KEY')
        tst.commit()
        tst.save(self.results_folder + 'test_full_sql_generation.sql')
        #print(tst.get_sql())
        self.assertEqual(len(tst.get_sql()), 1059) 		
    

    def test_sql_code_agg_single_col(self):
        t2 = SQLCodeGenerator('C_SALES')
        t2.set_column_list(['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'])
        t2.aggregate('C_AGG_PRODUCT', 'PRODUCT', 'sum(AMOUNT)')
        t2.save(self.results_folder + 'test_sql_code_agg_single_col.sql')
        self.assertEqual(len(t2.get_sql()), 138) 		

    def test_aggregate_multiple_cols(self):
        t3 = SQLCodeGenerator('C_SALES')
        t3.set_column_list(['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'])
        t3.aggregate('C_AGG_PRODUCT', 'PRODUCT, CUSTOMER_NAME', 'sum(AMOUNT)')
        t3.save(self.results_folder + 'test_sql_code_agg_multiple_cols.sql')
        self.assertEqual(len(t3.get_sql()), 168) 		


    def test_reverse_pivot(self):
        t4 = SQLCodeGenerator('C_SALES_UNPIVOT')
        t4.reverse_pivot_to_fact('C_SALES_UNPIVOT', ['Q1', 'Q2'], ['YEAR', 'Person'], ['Question', 'Result'])
        t4.save(self.results_folder + 'test_sql_code_test_rev_piv.sql')
        self.assertEqual(len(t4.get_sql()), 365) 		

    def test_get_column_list_from_select(self) :
        t5 = SQLCodeGenerator('BLAH')
        cols = t5.get_column_list_from_select('col1, col2, col3' , ',')
        self.assertEqual(len(cols), 3) 	
        cols = t5.get_column_list_from_select('col1,Col2,;col3' , ',')
        self.assertEqual(len(cols), 3) 	
        cols = t5.get_column_list_from_select('c' , ',')
        self.assertEqual(len(cols), 1) 	
        cols = t5.get_column_list_from_select('a,b,c,d,e,f,g' , ',')
        self.assertEqual(len(cols), 7) 	
        cols = t5.get_column_list_from_select('a;c,d:e,f_g' , ',')
        self.assertEqual(len(cols), 3) 	
        cols = t5.get_column_list_from_select('my_column:2nd_col, not a col' , ':')
        self.assertEqual(cols[0], 'my_column') 	
        

if __name__ == '__main__':
    unittest.main()