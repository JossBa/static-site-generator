import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href":"www.google.com", "id":"1234"})
        self.assertEqual(node.to_html(), '<a href="www.google.com" id="1234">Hello, world!</a>')
    
    def test_leaf_to_html_value(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), 'Hello, world!')