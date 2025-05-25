import unittest

from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_grandchildren_and_greatgrandchildren(self):
        geeat_grandchild_node = LeafNode("b", "grandchild")
        grandchild_node = ParentNode("p", [geeat_grandchild_node,geeat_grandchild_node], {"id":"1234"})
        child_node = ParentNode("span", [grandchild_node,geeat_grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),'<div><span><p id="1234"><b>grandchild</b><b>grandchild</b></p><b>grandchild</b></span></div>')

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError, msg='invalid HTML: no children'):
            ParentNode("div", None).to_html()

    def test_to_html_without_tag(self):
        with self.assertRaises(ValueError, msg='invalid HTML: no tag'):
            ParentNode(None, [LeafNode("b", "grandchild")]).to_html()
    
    def test_to_html_without_tag_children(self):
        with self.assertRaises(ValueError, msg='invalid HTML: no children'):
            ParentNode(None, None).to_html()