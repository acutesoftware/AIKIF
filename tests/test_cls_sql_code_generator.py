# test_cls_sql_code_generator.py	written by Duncan Murray 25/6/2014

import unittest
import sys
import os
from aikif.dataTools.cls_sql_code_generator import SQLCodeGenerator
class TestClassDataSet(unittest.TestCase):
 
    def setUp(self):
        pass
        self.results_folder = 'test_results/'

    def test_01_full_sql_generation(self):
        
        tst = SQLCodeGenerator('C_FACT_TABLE')
        tst.set_column_list(['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'])

        tst.comment_block('Insert staging records to Fact')
        tst.trunc_fact_table()
        tst.populate_from_staging('RAW_DATA_TABLE', ['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'], 'STAGING_TABLE')

        tst.comment_block('DQ Fixes')
        tst.update_set_where("PRODUCT = 'new name'", "PRODUCT = 'old name'")
        tst.update_old_to_new("CUSTOMER_NAME", "wRong Name", "Corrected Name")
        tst.commit()
        tst.comment_block('Key to Dimensions')
        tst.key_to_dimension('PRODUCT_KEY', 'substr(op.PRODUCT, 1,10)', 'U_PRODUCT_LIST', 'product_name', 'PRODUCT_KEY')
        tst.commit()
        tst.save(self.results_folder + 'test_will_fail_full_sql_generation.sql')  # will fail
        tst.save('test_full_sql_generation.sql')
        #print(tst.get_sql())
        self.assertEqual(len(tst.get_sql()), 1060) 		
        self.assertEqual(len(str(tst)), 71)
        #print(tst)
        self.assertEqual(str(tst), """C_FACT_TABLE
col : DATE
col : PRODUCT
col : CUSTOMER_NAME
col : AMOUNT
""")
        tst.create_script_fact()
        tst.collect_stats('C_FACT_TABLE')
        tst.comment('test comment')
        tst.create_index('C_FACT_TABLE', ['DATE', 'CUSTOMER'])
        tst.save_ddl('CREATE_TEST01.SQL')
        self.assertTrue(os.path.exists('CREATE_TEST01.SQL'))
        tst.save_undo('UNDO.SQL')
        self.assertTrue(os.path.exists('UNDO.SQL'))


    def test_02_sql_code_agg_single_col(self):
        t2 = SQLCodeGenerator('C_SALES')
        t2.set_column_list(['DATE', 'PRODUCT', 'CUSTOMER_NAME'])
        t2.add_to_column_list('AMOUNT')  # pretend we forgot to declare a column
        t2.aggregate('C_AGG_PRODUCT', 'PRODUCT', 'sum(AMOUNT)')
        t2.save('test_sql_code_agg_single_col.sql')
        self.assertTrue(os.path.exists('test_sql_code_agg_single_col.sql'))
        self.assertEqual(len(t2.get_sql()), 138) 

    def test_03_aggregate_multiple_cols(self):
        t3 = SQLCodeGenerator('C_SALES')
        t3.set_column_list(['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'])
        t3.aggregate('C_AGG_PRODUCT', 'PRODUCT, CUSTOMER_NAME', 'sum(AMOUNT)')
        
        t3.extract_dimension('dim_name', ['dim_cols'], 'dim_key', 'dim_stag_table', 'src_table', ['src_cols'], ['grain_cols'], 'where_clause')
        print(t3)
        t3.save('test_sql_code_agg_multiple_cols.sql')
        self.assertTrue(os.path.exists('test_sql_code_agg_multiple_cols.sql'))
        self.assertEqual(len(t3.get_sql()), 684)
        
        



    def test_04_reverse_pivot(self):
        t4 = SQLCodeGenerator('C_SALES_UNPIVOT')
        meas_cols = ['Sales', 'Expenses']
        t4.reverse_pivot_to_fact('C_SALES_UNPIVOT', 'Question' , ['Q1', 'Q2'], ['YEAR', 'Person'], meas_cols, meas_cols, '\n')
        t4.save('test_sql_code_test_rev_piv.sql')
        self.assertTrue(os.path.exists('test_sql_code_test_rev_piv.sql'))
        self.assertEqual(len(t4.get_sql()), 401)

    def test_05_reverse_pivot_simple(self):
        t4 = SQLCodeGenerator('C_TEST_UNPIVOT')
        meas_cols = ['Car', 'Home', 'Travel', 'Study']
        t4.reverse_pivot_to_fact('C_TEST_UNPIVOT', 'Category' , meas_cols, meas_cols, meas_cols, meas_cols, '\n')
        t4.save('test_sql_code_test_rev_piv_simple.sql')
        self.assertTrue(os.path.exists('test_sql_code_test_rev_piv_simple.sql'))
        self.assertEqual(len(t4.get_sql()), 689)
        

    def test_06_get_column_list_from_select(self) :
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
        
    def test_07_create_staging_table(self) :
        t7 = SQLCodeGenerator('BLAH')
        t7.create_script_staging_table('test07', ['col1', 'col2', 'col3']) 
        #print('t7 staging = ', t7.ddl_text) # Note - one trailing space at end of col lines
        expected_result = """---------------------------------------------
-- CREATE Staging Table - test07
---------------------------------------------
DROP TABLE test07 CASCADE CONSTRAINTS;
CREATE TABLE test07 (
  col1 VARCHAR2(200), 
  col2 VARCHAR2(200), 
  col3 VARCHAR2(200), 
  UPDATE_DATE DATE 
);
"""
        self.assertEqual(t7.ddl_text, expected_result) 	
        print((t7.ddl_text))
        t7.save_ddl('CREATE_TABLE_test07.SQL')
        self.assertTrue(os.path.exists('CREATE_TABLE_test07.SQL'))
        
if __name__ == '__main__':
    unittest.main()