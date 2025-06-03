from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline import split_nodes_delimiter,extract_markdown_images, extract_markdown_links


def main():
    # new_node = TextNode('This is some anchor text',TextType.LINK,  'https://www.boot.dev')
    # html_node = HTMLNode('<a>', 'Visit Google',props={'href':'www.google.com'})
    # print(new_node)
    # print(html_node)
    # leaf_node = LeafNode("p", "This is a paragraph of text.").to_html()
    # print(leaf_node)
    # another_leaf_node =LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
    # print(another_leaf_node)
    # node = LeafNode("p", "Hello, world!").to_html()
    # print(node)
    # node = LeafNode(None, "Hello, world!")
    # print(node.to_html())

    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ])
    # print(node.to_html())
    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # retu = split_nodes_delimiter([node], '`', TextType.CODE)
    # print(retu)
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    extract_markdown_images(text)
    link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    links = extract_markdown_links(link_text)
    print(links)


if __name__ == "__main__":
    main()

