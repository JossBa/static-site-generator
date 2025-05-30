from textnode import TextNode, TextType
from typing import List


def split_nodes_delimiter(old_node, delimiter, text_type):
    if len(old_node) == 0:
        raise ValueError('Must provide node array')
    if delimiter is None or delimiter == '':
        raise ValueError('Must define valid delimiter')
    new_nodes = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
    split_nodes = []
    split_str = node.text.split(delimiter)
    if len(split_str) % 2 == 0:
        raise ValueError('none closing delimiter')
    for i, str in enumerate(split_str):
        if str == "":
            continue
        elif i % 2 == 0:
            split_nodes.append(TextNode(str, TextType.TEXT))
        else:
            split_nodes.append(TextNode(str, text_type))
    new_nodes.extend(split_nodes)
    return new_nodes