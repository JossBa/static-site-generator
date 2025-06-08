from textnode import TextNode, TextType
import re

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

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    if len(old_nodes) == 0:
        raise ValueError('Must provide node array')
    new_nodes = []
    for old_node in old_nodes:
        # print(f"TEXT TYPE{old_node.text_type} old_node: {old_node}")
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # extract possible image from old_node string --> returns a list of tuples
        # print(f"old_node.text: {old_node.text}")
        old_node_text = old_node.text
        extracted_images = extract_markdown_images(old_node_text)
        for img in extracted_images:
            if len(img) != 2:
                raise Exception("Invalid image md due to unclosed section")
            # 1. part of split_text is Text, 2. part is the remaining text without the current link
            split_text = old_node_text.split(f"![{img[0]}]({img[1]})", 1)
            # Assign the remaining text to old_node_text for next iteration
            old_node_text = split_text[1]
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            if img[0] != "" and img[1] != "":
                new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
        # add remaining text at the end to new_nodes 
        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    if len(old_nodes) == 0:
        raise ValueError('Must provide node array')
    new_nodes = []
    for old_node in old_nodes:
        # print(f"TEXT TYPE IN LINK: {old_node.text_type}")
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # extract possible links from old_node string --> returns a list of tuples
        old_node_text = old_node.text
        extracted_links = extract_markdown_links(old_node_text)
        for link in extracted_links:
            if len(link) != 2:
                raise Exception("Invalid link markdwon due to unclosed section")
            # 1. part of split_text is Text, 2. part is the remaining text without the current link
            split_text = old_node_text.split(f"[{link[0]}]({link[1]})", 1)
            # Assign the remaining text to old_node_text for next iteration
            old_node_text = split_text[1]
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            if link[0] != "" and link[1] != "":
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        # add remaining text at the end to new_nodes 
        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    image_nodes  = split_nodes_image(node)
    link_nodes = split_nodes_link(image_nodes)
    code_nodes = split_nodes_delimiter(link_nodes, '`', TextType.CODE)
    bold_nodes = split_nodes_delimiter(code_nodes,'**', TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, '_', TextType.ITALIC)
    return italic_nodes