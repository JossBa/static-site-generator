from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    new_node = TextNode('This is some anchor text',TextType.LINK,  'https://www.boot.dev')
    html_node = HTMLNode('<a>', 'Visit Google',props={'href':'www.google.com'})
    print(new_node)
    print(html_node)

if __name__ == "__main__":
    main()

