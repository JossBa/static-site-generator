from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    new_node = TextNode('This is some anchor text',TextType.LINK,  'https://www.boot.dev')
    html_node = HTMLNode('<a>', 'Visit Google',props={'href':'www.google.com'})
    print(new_node)
    print(html_node)
    leaf_node = LeafNode("p", "This is a paragraph of text.").to_html()
    print(leaf_node)
    another_leaf_node =LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
    print(another_leaf_node)
    node = LeafNode("p", "Hello, world!").to_html()
    print(node)
    node = LeafNode(None, "Hello, world!")
    print(node.to_html())

if __name__ == "__main__":
    main()

