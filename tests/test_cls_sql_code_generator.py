# test_cls_sql_code_generator.py	written by Duncan Murray 25/6/2014

import unittest
import sys
sys.path.append("..\\AI\\dataTools")
from cls_sql_code_generator import SQLCodeGenerator
class TestClassDataSet(unittest.TestCase):
 
	def setUp(self):
		pass

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
		tst.save('test.sql')
		#print(tst.get_sql())
		self.assertEqual(len(tst.get_sql()), 1112) 		
		
		
		
if __name__ == '__main__':
	unittest.main()