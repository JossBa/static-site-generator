import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = { 
            "href": "https://www.google.com",
            "target": "_blank",
            }
        html_node = HTMLNode(None,None,None,props)
        html_props = html_node.props_to_html()
        self.assertEqual(html_props, ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        html_node = HTMLNode('<a>', 'Visit Google')
        self.assertEqual(f"{html_node}", "HTMLNode(<a>, Visit Google, None, None)")
    
    def test_empty_props(self):
        html_node = HTMLNode('<H1>', 'Visit Google')
        html_props = html_node.props_to_html()
        self.assertEqual(html_props, None)
