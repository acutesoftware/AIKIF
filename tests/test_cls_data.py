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


    def test_06_size_string(self):
        d06 = cls_data.Data('ABCDEFG')
        self.assertEqual(d06.content['data'], 'ABCDEFG')
        self.assertEqual(d06.total_records, 1)
        self.assertEqual(d06.total_length, 7)
        self.assertEqual(d06.total_nodes, 0)
        
    def test_07_size_list(self):
        d07 = cls_data.Data(['ABCDEFG', 'WWW', 'd'])
        self.assertEqual(d07.content['data'], ['ABCDEFG', 'WWW', 'd'])
        self.assertEqual(d07.total_records, 1)
        self.assertEqual(d07.total_length, 11)
        self.assertEqual(d07.total_nodes, 3)
        
    def test_08_size_nested_list(self):
        d08 = cls_data.Data(['ABCDEFG', 'WWW', ['d','e','f','g']])
        self.assertEqual(d08.content['data'], ['ABCDEFG', 'WWW', ['d','e','f','g']])
        self.assertEqual(d08.total_records, 2) # 2 records - because list is 1 rec, and subset is 2nd
        self.assertEqual(d08.total_length, 14)
        self.assertEqual(d08.total_nodes, 6)
        
    def test_09_size_dict(self):
        """
        TODO - check size of dicts and node counts
        """
        json_example = {"menu": {
          "id": "file",
          "value": "File",
          "popup": {
            "menuitem": [
              {"value": "New", "onclick": "CreateNewDoc()"},
              {"value": "Open", "onclick": "OpenDoc()"},
              {"value": "Close", "onclick": "CloseDoc()"}
            ]
          }
        }}

        d09 = cls_data.Data(json_example)
        self.assertEqual(d09.total_records, 1) 
        self.assertEqual(d09.total_length, 201)
        self.assertEqual(d09.total_nodes, 3)
        self.assertEqual(d09.content['data']['menu']['id'], 'file')
        self.assertEqual(d09.content['data']['menu']['value'], 'File')
        self.assertEqual(d09.content['data']['menu']['popup']['menuitem'][0]['value'], 'New')
        self.assertEqual(d09.content['data']['menu']['popup']['menuitem'][1]['value'], 'Open')
        self.assertEqual(d09.content['data']['menu']['popup']['menuitem'][2]['value'], 'Close')

        self.assertEqual(d09.content['data']['menu']['popup']['menuitem'], [
              {"value": "New", "onclick": "CreateNewDoc()"},
              {"value": "Open", "onclick": "OpenDoc()"},
              {"value": "Close", "onclick": "CloseDoc()"}
            ])

            
    def test_10_size_dict_flat(self):
        json_example = {
            'fruit': [{'name':'apples'}, {'name':'oranges'}, {'name':'pears'}],
            'vegetables':[{'name':'carrots'},{'name':'peas'}, {'name':'onions'}],
            'meat':[{'name':'lamb'},{'name':'beef'},{'name':'chicken'},{'name':'pork'}]
        }
        d10 = cls_data.Data(json_example)
        self.assertEqual(d10.total_records, 1) 
        self.assertEqual(d10.total_length, 231)
        self.assertEqual(d10.total_nodes, 10)
        self.assertEqual(d10.content['data']['fruit'][1], {'name':'oranges'})
        self.assertEqual(d10.content['data']['fruit'][2]['name'], 'pears')
        self.assertEqual(d10.content['data']['vegetables'][0], {'name':'carrots'})
        self.assertEqual(d10.content['data']['vegetables'][0]['name'], 'carrots')
        self.assertEqual(len(d10.content['data']['meat']), 4)

            
        
if __name__ == '__main__':
    unittest.main()