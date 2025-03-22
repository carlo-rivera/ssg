import os
import shutil
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
    copy_contents("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()