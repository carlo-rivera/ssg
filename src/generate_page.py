import os
import shutil
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as from_file:
        content = from_file.read()

    with open(template_path, 'r') as template_file:
        template = template_file.read()

    title = extract_title(content)
    html_str = markdown_to_html_node(content).to_html()

    grand_file = template.replace("{{ Title }}", title).replace("{{ Content }}", html_str)

    if not os.path.exists(dest_path):
        os.makedirs(
            os.path.dirname(dest_path),
            exist_ok=True
        )
    
    with open(dest_path, 'w+') as dest_file:
        dest_file.write(grand_file)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    children = os.listdir(dir_path_content)
    for child in children:
        file_path = os.path.join(dir_path_content, child)
        if os.path.isfile(file_path):
            page_path = os.path.join(dest_dir_path, child.replace("md", "html"))
            generate_page(file_path, template_path, page_path)
        if os.path.isdir(file_path):
            dest_path = os.path.join(dest_dir_path, child)
            os.mkdir(dest_path)
            generate_pages_recursive(file_path, template_path, dest_path)