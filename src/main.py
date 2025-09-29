import shutil
import os
from pathlib import Path
from my_markdown import generate_page

def build():
    public_path = './public'
    path_exists = os.path.exists(public_path)
    if path_exists:
        try:
            shutil.rmtree(public_path)
            print(f"removed {public_path}")
        except:
            print(f"failed to remove contents of {public_path}")
    os.mkdir(public_path)
    print(f"created new folder {public_path}")
    copy_files('./static', './public')
        
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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        src_content_path = os.path.join(dir_path_content, entry)
        dest_content_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(src_content_path): 
            dest_content_path = Path(dest_content_path).with_suffix(".html")
            generate_page(src_content_path, template_path,dest_content_path)
        else:
            generate_pages_recursive(src_content_path,template_path,dest_content_path)

def main():
    build()
    generate_pages_recursive('./content', './template.html', './public')
    

if __name__ == "__main__":
    main()

