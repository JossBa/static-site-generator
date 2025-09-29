
from blocks import markdown_to_html_node
import os

def extract_title(markdown):
    # It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
    lines = markdown.read().split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    else:
        raise Exception('Markdown needs to start with # title')


def generate_page(from_path:str, template_path:str, dest_path:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    title = extract_title(markdown_file)
    markdown_file.close()

    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()
    
    html_node = markdown_to_html_node(markdown)
    html_str = html_node.to_html()
    template = template.replace('{{ Title }}', title).replace('{{ Content }}', html_str)

    dir_name = os.path.dirname(dest_path)
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)

    html_page_file = open(dest_path, 'w')
    html_page_file.write(template)
    html_page_file.close()