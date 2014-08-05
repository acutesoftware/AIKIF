# test_cls_dataset.py	written by Duncan Murray 25/6/2014

import unittest
import sys
sys.path.append("..\\AI\\dataTools")
import cls_dataset as cl
					
class TestClassDataSet(unittest.TestCase):
 
	def setUp(self):
		pass

	def test_create_folder(self):
		fldr = cl.DataSet('Folder of CSV Files', 'folder')
		fldr.add('file1.csv')
		fldr.add('file2.csv')
		print("test 1")
		self.assertEqual(len(fldr.datatables), 2) 
		self.assertEqual(len(fldr.list_tables('\n')), 19) 		
		
	def test_create_database(self):
		schema = cl.DataSet('schema', 'database')
		schema.add('C_CUSTOMERS')
		schema.add('C_PRODUCTS')
		schema.add('C_SALES')
		print("test 1")
		self.assertEqual(len(schema.datatables), 3)  
		self.assertEqual(len(schema.list_tables('')), 28)  

		
		
if __name__ == '__main__':
	unittest.main()