import shutil
import os
from pathlib import Path
from my_markdown import generate_page
from sys import argv

def clean_up(static_path, dest_path):
    path_exists = os.path.exists(dest_path)
    if path_exists:
        try:
            shutil.rmtree(dest_path)
            print(f"removed {dest_path}")
        except:
            print(f"failed to remove contents of {dest_path}")
    os.mkdir(dest_path)
    print(f"created new folder {dest_path}")
    copy_files(static_path, dest_path)
        
def copy_files(src_path, dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    for entry in os.listdir(src_path):
        current_path = os.path.join(src_path, entry)
        new_dst_path = os.path.join(dst_path, entry)
        if os.path.isfile(current_path): 
            shutil.copy(current_path, dst_path)
        else:
            copy_files(current_path, new_dst_path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        src_content_path = os.path.join(dir_path_content, entry)
        dest_content_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(src_content_path): 
            dest_content_path = Path(dest_content_path).with_suffix(".html")
            generate_page(src_content_path, template_path,dest_content_path, basepath)
        else:
            generate_pages_recursive(src_content_path,template_path,dest_content_path, basepath)

def main():
    basepath = '/'
    if len(argv) >= 1:
        basepath = argv[1]
    print(basepath)
    static_path = './static'
    dest_path = './docs'
    template_path = './template.html'
    content_path = './content'
    clean_up(static_path, dest_path)
    generate_pages_recursive(content_path, template_path, dest_path, basepath)

if __name__ == "__main__":
    main()
