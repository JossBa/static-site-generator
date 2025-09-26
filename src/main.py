import shutil
import os 

def build():
    # It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    public_path = './public'
    path_exists = os.path.exists(public_path)
    if path_exists:
        try:
            # remove public folder
            shutil.rmtree(public_path)
            print(f"removed {public_path}")
        except:
            print(f"failed to remove contents of {public_path}")
    # create public folder
    os.mkdir(public_path)
    print(f"created new folder {public_path}")
    copy_files('./static', './public')
        


def copy_files(src_path, dst_path):
    entries = os.listdir(src_path)
    if len(entries) == 0:
        return
    for entry in entries:
        current_path = os.path.join(src_path, entry)
        if os.path.isdir(current_path): 
            new_dst_path = os.path.join(dst_path, entry)
            os.mkdir(new_dst_path)
            copy_files(current_path, new_dst_path)
        if os.path.isfile(current_path):
            shutil.copy(current_path, dst_path)

def main():
    print("...")
    build()


if __name__ == "__main__":
    main()

