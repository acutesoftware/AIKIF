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
        self.assertEqual(str(d01), 'hello') 
        self.assertEqual(str(cls_data.Data('1')), '1') 

    def test_02_number(self):
        d02 = cls_data.Data(34.54)
        self.assertEqual(str(d02), '34.54') 
        self.assertEqual(str(cls_data.Data(0.5847593842)), '0.5847593842') 
        
    def test_03_url(self):
        d03 = cls_data.Data('https://raw.githubusercontent.com/acutesoftware/AIKIF/master/README.txt')
        self.assertTrue(len(str(d03)) > 25) 
        self.assertEqual(str(d03)[0:63], 'AIKIF - Artificial Intelligence Knowledge Information Framework') 

    def test_04_list(self):
        d04 = cls_data.Data(['this', 'is', 'a', 'list', 'of', 'words'])
        self.assertEqual(len(str(d04)), 42) 
        self.assertEqual(str(d04), "['this', 'is', 'a', 'list', 'of', 'words']") 
        
        self.assertEqual(str(cls_data.Data(['aaa', 0.4, ['a','b','c']])), "['aaa', 0.4, ['a', 'b', 'c']]")

    def test_05_csv(self):
        with open('data.csv', "w") as f:
            f.writelines(
"""Name,Gender,tot2
Frank,M,1866
John,M,124
Betty,F,67""")
        d05 = cls_data.Data('data.csv')
        self.assertEqual(str(d05), "[['Frank', 'M', '1866'], ['John', 'M', '124'], ['Betty', 'F', '67']]")
        
if __name__ == '__main__':
    unittest.main()