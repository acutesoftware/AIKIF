import unittest
import sys
import os

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'dataTools' 

sys.path.append(pth)


import cls_data
                    
class TestClassData(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_01_simple_string(self):
        d01 = cls_data.Data('hello')
        print(d01)
        self.assertEqual(str(d01), 'hello') 
        self.assertEqual(str(cls_data.Data('1')), '1') 

    def test_02_url(self):
        d02 = cls_data.Data('https://github.com/acutesoftware/AIKIF/blob/master/README.txt')
        print(d02)
        self.assertTrue(len(str(d02)) > 25) 
        #self.assertEqual(cls_data.Data('1'), '1') 

    def test_03_number(self):
        d03 = cls_data.Data(34.54)
        print(d03)
        self.assertEqual(str(d03), '34.54') 
        self.assertEqual(str(cls_data.Data(0.5847593842)), '0.5847593842') 
        
if __name__ == '__main__':
    unittest.main()