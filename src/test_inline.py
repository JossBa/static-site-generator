
import unittest

from inline import split_nodes_delimiter,extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertEqual(str(new_nodes), "[TextNode(This is text with a , TextType.TEXT), TextNode(code block, TextType.CODE), TextNode( word, TextType.TEXT)]")

    def test_bold(self):
        node = TextNode("This is text with a **bold text** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertEqual(str(new_nodes), "[TextNode(This is text with a , TextType.TEXT), TextNode(bold text, TextType.BOLD), TextNode( word, TextType.TEXT)]")
    
    def test_italic(self):
        node = TextNode("This is a text with _italic_ parts", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"_", TextType.ITALIC)
        self.assertEqual(str(new_nodes), "[TextNode(This is a text with , TextType.TEXT), TextNode(italic, TextType.ITALIC), TextNode( parts, TextType.TEXT)]")

    def test_empty_node(self):
        with self.assertRaises(ValueError, msg='Must provide node array'):
            split_nodes_delimiter([], "*", TextType.BOLD)
    
    def test_empty(self):
        node = TextNode("This is a text with _italic_ parts", TextType.ITALIC)
        with self.assertRaises(ValueError, msg='Must provide delimiter'):
            split_nodes_delimiter([], "", TextType.BOLD)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_one(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images(
            "This is text with nothing in there"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_two(self):
        matches = extract_markdown_images(
            "This is text with ![image](https://i.imgur.com/zjjcJKZ.png) and another ![another image](https://i.bla.com/zjjcJKZ.jpg)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("another image", "https://i.bla.com/zjjcJKZ.jpg")], matches)
    
    #shouldn't this fail?
    def test_extract_markdown_images_empty_description(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)

    #shouldn't this fail?
    def test_extract_markdown_images_empty_url(self):
        matches = extract_markdown_images(
            "This is text with an ![]()"
        )
        self.assertListEqual([("", "")], matches)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links_one(self):
        matches = extract_markdown_links(
            "This is text with an [youtube](https://youtube.com)"
        )
        self.assertListEqual([("youtube", "https://youtube.com")], matches)

    def test_extract_markdown_links_two(self):
        matches = extract_markdown_links(
            "This is text with an [youtube](https://youtube.com) and [youtube](https://youtube.com)"
        )
        self.assertListEqual([("youtube", "https://youtube.com"),("youtube", "https://youtube.com")], matches)

    def test_extract_markdown_links_malformed(self):
        matches = extract_markdown_links(
            "This is text with an [malformed]](httpsss://youtube.com)"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links_malformed_brakets(self):
        matches = extract_markdown_links(
            "This is text with an (wrong brackets)(httpsss://youtube.com)"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_empty(self):
        matches = extract_markdown_links(
            "This is text with an []()"
        )
        self.assertListEqual([("", "")], matches)
