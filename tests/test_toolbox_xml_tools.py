#!/usr/bin/python3
# coding: utf-8
import unittest
import sys
import os
import time
import aikif.config as mod_cfg
import aikif.lib.cls_filelist as fl 
import xml.dom.minidom
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'toolbox' )
import xml_tools

#small_file = root_folder + os.sep + 'aikif' + os.sep + 'ontology' + os.sep + 'mindOntology.xml'
#large_file = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' + os.sep + '__ANC__WhereToHongKong.xml'
small_file = os.getcwd() + os.sep + 'sample_small.xml'
large_file = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' + os.sep + '__ANC__WhereToHongKong.xml'
print('small_file = ', small_file)

class ToolboxXmlToolsTest(unittest.TestCase):
    def test_01_create_xml_file_from_text(self):
        document = """<slideshow>
        <title>Demo slideshow</title>
        <slide><title>Slide title</title>
        <point>This is a demo</point>
        <point>Of a program for processing slides</point>
        </slide>

        <slide><title>Another demo slide</title>
        <point>It is important</point>
        <point>To have more than</point>
        <point>one slide</point>
        </slide>
        </slideshow>
        """
        dom = xml.dom.minidom.parseString(document)
        pretty_xml_as_string = dom.toprettyxml()
        #print(pretty_xml_as_string)
        self.assertEqual(len(pretty_xml_as_string), 490) 
        self.assertEqual(pretty_xml_as_string[0:34], '<?xml version="1.0" ?>\n<slideshow>') 
        self.assertEqual(pretty_xml_as_string[-13:],'</slideshow>\n')
        #print('small_file = ' + small_file)
        with open(small_file, 'w') as f:
            f.write(pretty_xml_as_string)
            
        self.assertEqual(xml_tools.count_elements(small_file, 'slideshow'), (1,11))
        self.assertEqual(xml_tools.count_elements(small_file, 'title'), (3,11))
        self.assertEqual(xml_tools.count_elements(small_file, 'slide'), (3,11))
        self.assertEqual(xml_tools.count_elements(small_file, 'point'), (5,11))
        
    def test_11_xml_class(self):
        x = xml_tools.XmlFile(small_file)
        self.assertEqual(x.name, 'sample_small.xml') 
        self.assertEqual(x.lines, 38) 
        #print(x)

             
    def test_13_get_xml_stats(self):
        s = xml_tools.get_xml_stats(small_file)
        self.assertEqual(s['num_lines'], '38 lines') 
        self.assertEqual(s['shortname'], 'sample_small.xml') 
        
    def test_14_xml_breaker(self):
        """
        this wont work with large XML file on travis-ci, so 
        ensure a small file splits with at least the first one
        """
        self.assertFalse(os.path.exists('sample_small1.xml'))
        xml_tools.split_xml(small_file, 'sentence', 500)
        self.assertTrue(os.path.exists('sample_small1.xml'))
        os.remove('sample_small1.xml')    
    
if __name__ == '__main__':
	unittest.main()