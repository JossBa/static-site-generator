import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType

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

    def test_ordered_list(self):
        heading_block = """1. apple
2. banana
3. pear
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)


    def test_ordered_list_leading_whitespace(self):
        heading_block = """1. apple 
        2. banana
3. pear
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    

    def test_ordered_list_trailing_whitespace(self):
        heading_block = """1. apple 
2. banana
3. pear 
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_missing_dot(self):
        heading_block = """1 apple 
2. banana
3. pear 
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_ordered_list_missing_whitespace(self):
        heading_block = """1.apple 
2. banana
3. pear 
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        
    def test_unordered_list(self):
        heading_block = """- apple
- banana
- pear
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_unordered_list_missing_whitespace(self):
        heading_block = """-apple
- banana
- pear
"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_unordered_list_trailing_new_line(self):
        heading_block = """- apple
- banana
- pear

"""
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


    