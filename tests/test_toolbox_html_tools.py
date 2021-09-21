import unittest
import sys
import os
import time

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
pth = root_folder + os.sep + 'aikif'

#sys.path.append(pth)
#import config as mod_cfg

sys.path.append(pth + os.sep + 'toolbox' )
import html_tools as mod_html
import network_tools as mod_net

"""
WARNING - remember to update Beautiful Soup when updating
to Python 3.5 - get following message running test_05_parse_page

C:\Python34\lib\site-packages\beautifulsoup4-4.3.2-py3.4.egg\bs4\builder\_htmlpa
rser.py:157: DeprecationWarning: The strict argument and mode are deprecated.
C:\Python34\lib\site-packages\beautifulsoup4-4.3.2-py3.4.egg\bs4\builder\_htmlpa
rser.py:157: DeprecationWarning: The value of convert_charrefs will become True
in 3.5. You are encouraged to set the value explicitly.
"""

class ToolboxHtmlToolsTest(unittest.TestCase):

    def test_01_extract_page_links_none(self):
        txt = '<html><body><H1>this is some html</H1>but there are no links</body></html>'
        self.assertEqual(mod_html.extract_page_links(txt, ''), [])

    def test_02_extract_page_links_one(self):
        txt = 'this is some test, and <a href=http://xkcd.com/292>this is a link</a>'
        self.assertEqual(mod_html.extract_page_links(txt, ''), ['http://xkcd.com/292'])

    def test_03_extract_content_a(self):
        txt = '<html><body><H1>this is some html</H1><BR>but there are no links</body></html>'
        self.assertEqual(mod_html.extract_content(txt), 'this is some htmlbut there are no links')

    def test_04_extract_content_b(self):
        txt = 'this is some test, and <a href=http://xkcd.com/292>this is a link</a>'
        self.assertEqual(mod_html.extract_content(txt), 'this is some test, and this is a link')


    def test_05_parse_page(self):
        url = 'http://xkcd.com/292'
        raw_text = mod_net.get_web_page(url)
        links = mod_html.extract_page_links(raw_text, '')
        self.assertEqual(len(raw_text) > 1000, True)
        self.assertEqual(len(links) > 5, True)
        #self.assertEqual(mod_html.extract_content(raw_text).strip()[0:10], 'xkcd: goto')
        self.assertEqual(mod_html.extract_content(raw_text).strip()[-13:], 'More details.')


    def test_06_extract_by_div(self):
        raw_text = '<DIV id=aa>div aa</DIV>blah blah'
        html, txt = mod_html.extract_by_div(raw_text, 'aa')
        #print('html = ', html)
        #print('txt  = ', txt)
        self.assertEqual(html, 'div aa\n')
        self.assertEqual(txt, 'div aa')

if __name__ == '__main__':
    unittest.main()
