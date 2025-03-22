import os
import shutil
import sys
from generate_page import generate_page, generate_pages_recursive

def copy_contents(source, destination):
    if not os.path.exists(source):
        raise Exception("source path does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    children = os.listdir(source)
    for child in children:
        src_path = os.path.join(source, child)
        if os.path.isfile(src_path):
            shutil.copy(src_path, destination)
        else:
            dir_path = os.path.join(destination, child)
            os.mkdir(dir_path)
            copy_contents(src_path, dir_path)

    return children

def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    copy_contents(f"./static", f"./docs")
    generate_pages_recursive(basepath, f"./content", f"./template.html", f"./docs")

if __name__ == "__main__":
    main()