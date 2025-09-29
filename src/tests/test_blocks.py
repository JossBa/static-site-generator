import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )
    
    def test_markdown_to_blocks_extra_whitespace(self):
        md = """
         This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line                          

       - This is a list
- with items              
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_new_lines(self):
        md = """
This is **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        heading_block = '# This is a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_2(self):
        heading_block = '## This is a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_3(self):
        heading_block = '### This is a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_4(self):
        heading_block = '#### This is a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_5(self):
        heading_block = '##### This is a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_6(self):
        heading_block = '###### This is a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_no_space(self):
        heading_block = '#This is NOT a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_heading_more_than_six_hastags(self):
        heading_block = '####### This is NOT a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph(self):
        heading_block = 'This is NOT a heading block'
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


    def test_code(self):
        heading_block = """```
        This is a code block
        ```"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_code_leading_new_line(self):
        heading_block = """
        ```
        This is a code block
        ```"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_OLIST(self):
        heading_block = """1. apple
2. banana
3. pear"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.OLIST)


    def test_OLIST_leading_whitespace(self):
        heading_block = """1. apple 
        2. banana
3. pear
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    

    def test_OLIST_trailing_whitespace(self):
        heading_block = """1. apple 
2. banana
3. pear """
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.OLIST)

    def test_OLIST_missing_dot(self):
        heading_block = """1 apple 
2. banana
3. pear"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_OLIST_missing_whitespace(self):
        heading_block = """1.apple 
2. banana
3. pear 
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        
    def test_unOLIST(self):
        heading_block = """- apple
- banana
- pear"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.ULIST)
    
    def test_unOLIST_missing_whitespace(self):
        heading_block = """-apple
- banana
- pear"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_unOLIST_trailing_new_line(self):
        heading_block = """- apple
- banana
- pear

"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    