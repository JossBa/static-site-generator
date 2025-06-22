from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter,extract_markdown_images, extract_markdown_links, split_nodes_link,text_to_textnodes
from blocks import markdown_to_blocks, block_to_block_type

def main():
    # nodes = text_to_textnodes('This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')
    # print(nodes)
    blocks = markdown_to_blocks(
        """
# Heading Text 1


## Heading Text 2


````
some code part
```

- asdasd
- asdpmasdasd

1. aspd
2. paosd
3. asodk

-apos
1.2s;;s
sdsdls[d

]

-s


- sssss
""")
    block_types = []
    for block in blocks:
        block_types.append(block_to_block_type(block))
    
    print(f"block types: {block_types}")


if __name__ == "__main__":
    main()

