from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter,extract_markdown_images, extract_markdown_links, split_nodes_link,text_to_textnodes


def main():
    nodes = text_to_textnodes('This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')
    print(nodes)


if __name__ == "__main__":
    main()

