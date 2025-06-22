import re

from enum import Enum
from typing import Dict

class BlockType(Enum):
    PARAGRAPH = 0
    HEADING = 1
    CODE = 2
    QUOTE = 3
    UNORDERED_LIST = 4
    ORDERED_LIST = 5

heading = r'((^[#]{1,6})\s).*'
code = r'^```[\s\S]*```$'
quote = r'^(>.*\n?)*$'
unordered_list = r'^(?:-\s.*(?:\n|$))+\Z'
ordered_list = r'(?:^\d+\.\s.*(?:\n|$))+'
# paragraph = r'[\s\S]*'

block_type_patterns: Dict[str, BlockType] = {
    heading: BlockType.HEADING,
    code: BlockType.CODE,
    quote: BlockType.QUOTE,
    unordered_list: BlockType.UNORDERED_LIST,
    ordered_list: BlockType.ORDERED_LIST
}

def block_to_block_type(block):
    for pattern in block_type_patterns:
        maybe_match = re.fullmatch(pattern, block, re.MULTILINE)
        if maybe_match:
            return block_type_patterns[pattern]
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = [str.strip() for str in markdown.split("\n\n")]
    return list(filter(lambda b: b != '', blocks))
