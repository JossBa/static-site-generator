import shutil
import os

from src.markdown import generate_page

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

def main():
    build()
    
    generate_page('./content/index.md', './template.html', './public/index.html')
    

if __name__ == "__main__":
    main()

