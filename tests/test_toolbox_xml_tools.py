import unittest
import sys
import os
import time
import aikif.config as mod_cfg
import aikif.lib.cls_filelist as fl 

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'toolbox' )
import xml_tools

small_file = root_folder + os.sep + 'aikif' + os.sep + 'ontology' + os.sep + 'mindOntology.xml'
large_file = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' + os.sep + 'ANC__WhereToHongKong.xml'
print('small_file = ', small_file)

class ToolboxXmlToolsTest(unittest.TestCase):
    def test_01_xml_class(self):
        x = xml_tools.XmlFile(small_file)
        self.assertEqual(x.name, 'mindOntology.xml') 
        self.assertEqual(x.lines, 5890) 
        print(x)

    def test_02_xml_breaker(self):
        """
        this wont work with large XML file on travis-ci
        """
        #xml_tools.split_xml(small_file, 'MindOntology_Definition', 5)
        print(large_file)
        if os.path.exists(large_file):   # for travis_ci not having large file
            print('testing large file')
            xml_tools.split_xml(large_file, 'sentence', 500)
    
    def test_03_get_xml_stats(self):
        s = xml_tools.get_xml_stats(small_file)
        self.assertEqual(s['num_lines'], '5890 lines') 
        self.assertEqual(s['shortname'], 'mindOntology.xml') 
            
    
if __name__ == '__main__':
	unittest.main()