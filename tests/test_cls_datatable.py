# test_cls_datatable.py		written by Duncan Murray 25/6/2014

import unittest
import sys
sys.path.append("..\\aikif\\dataTools")
import cls_datatable as cl
                    
class TestClassDataTable(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_01_create_file(self):
        fname = 'file1.csv'
        fle = cl.DataTable(fname, 'file')
        fle.save(fname, 'test data\nanother line\nfinal line\n')
        
        fle2 = cl.DataTable('Copy', 'file')
        file_contents = fle2.load(fname)
        self.assertEqual(len(file_contents), 67)  
        fle2.drop(fname)
        
    def test_02_percentile(self):
        fl3 = cl.DataTable('', '"')
        self.assertEqual(fl3.percentile([1,2,3,4,5,6], .25), 2.25)
        self.assertEqual(fl3.percentile([1,2,3,4,5,6], .5), 3.5)
        self.assertEqual(fl3.percentile([1,2,3,4,5,6], .75), 4.75)
        self.assertEqual(fl3.percentile([1,2,3,4,5,6,7,8,9,10], .25), 3.25)
        self.assertEqual(fl3.percentile([1,1,2], .5), 1)
        self.assertEqual(fl3.percentile([1,1,2], .25), 1)
        self.assertEqual(fl3.percentile([1,1,2], .75), 1.5)
        
if __name__ == '__main__':
    unittest.main()