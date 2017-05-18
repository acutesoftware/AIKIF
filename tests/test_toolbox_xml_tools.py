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
med_file   = os.getcwd() + os.sep + 'sample_med.xml'
big_file   = os.getcwd() + os.sep + 'sample_big.xml'

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
        with open(small_file, 'w') as f:
            f.write(pretty_xml_as_string)
            
        self.assertEqual(xml_tools.count_elements(small_file, 'slideshow'), (1,11))
        self.assertEqual(xml_tools.count_elements(small_file, 'title'), (3,11))
        self.assertEqual(xml_tools.count_elements(small_file, 'slide'), (3,11))
        self.assertEqual(xml_tools.count_elements(small_file, 'point'), (5,11))
    
    
    def test_02_make_med_xml_file(self):
        document = """<slideshow>
        <title>Demo slideshow</title>
        <slide><title>Slide 1</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 2</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 3</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 4</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 5</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 6</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 7</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 8</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 9</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 10</title><point>point 1</point><point>point 2</point></slide>
        <slide><title>Slide 11</title><point>point 1</point><point>point 2</point></slide>
        </slideshow>
        """
        with open(med_file, 'w') as f:
            f.write(document)
    
    
    
    
    def test_11_xml_class(self):
        x = xml_tools.XmlFile(small_file)
        self.assertEqual(x.name, 'sample_small.xml') 
        self.assertEqual(x.lines, 38) 
        #print(x)
        self.assertEqual(str(x)[46:75], '| name     = sample_small.xml')
        self.assertTrue(len(str(x)) > 271) # 272 on Win, 276 on Linux - this test will do for now
             
    def test_13_get_xml_stats(self):
        s = xml_tools.get_xml_stats(small_file)
        self.assertEqual(s['num_lines'], '38 lines') 
        self.assertEqual(s['shortname'], 'sample_small.xml') 
        
    def test_14_xml_breaker(self):
        """
        this currently doesnt work with large XML file on travis-ci, so 
        ensure a small file splits with at least the first one
        """
        self.assertFalse(os.path.exists('sample_small1.xml'))
        xml_tools.split_xml(small_file, 'slide', 2)
        self.assertTrue(os.path.exists('sample_small1.xml'))
        
    def test_15_make_random_xml_file(self):
        #self.assertFalse(os.path.exists(big_file))
        xml_tools.make_random_xml_file(big_file, 20, 15)
        self.assertTrue(os.path.exists(big_file))
        self.assertTrue(os.path.getsize(big_file) > 3000)
     
    def test_16_break_big_file(self):
        xml_tools.split_xml(med_file, 'slide', 5)
        self.assertTrue(os.path.exists(med_file))
        print((xml_tools.get_xml_stats(med_file)))
        print(('title', xml_tools.count_via_minidom(med_file, 'title') ))   
        print(('slide', xml_tools.count_via_minidom(med_file, 'slide') ))   
        self.assertEqual(xml_tools.count_via_minidom(med_file, 'title'), 12)
        self.assertEqual(xml_tools.count_via_minidom(med_file, 'slide'), 11)
   
    
if __name__ == '__main__':
	unittest.main()