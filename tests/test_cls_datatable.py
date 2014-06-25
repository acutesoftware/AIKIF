# test_cls_datatable.py		written by Duncan Murray 25/6/2014

import unittest
import sys
sys.path.append("..\\AI\\dataTools")
import cls_datatable as cl
					
class TestClassDataTable(unittest.TestCase):
 
	def setUp(self):
		pass

	def test_create_file(self):
		fname = 'file1.csv'
		fle = cl.DataTable('CSV Files', 'file')
		fle.save(fname, 'test data\nanother line\nfinal line\n')
		
		fle2 = cl.DataTable('Copy', 'file')
		file_contents = fle2.load(fname)
		self.assertEqual(len(file_contents), 34)  
		fle2.drop(fname)
		

		
		
if __name__ == '__main__':
	unittest.main()