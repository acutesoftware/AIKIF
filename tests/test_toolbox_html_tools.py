import unittest
import sys
import os
import time
import aikif.config as mod_cfg
import aikif.toolbox.html_tools as mod_html
import aikif.toolbox.network_tools as mod_net

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
        print(len(raw_text))
        self.assertEqual(len(raw_text) > 6000, True) 
        self.assertEqual(len(links) > 10, True)
        self.assertEqual(mod_html.extract_content(raw_text).strip()[0:10], 'xkcd: goto')
        self.assertEqual(mod_html.extract_content(raw_text).strip()[-13:], 'More details.')

        
if __name__ == '__main__':
    unittest.main()
