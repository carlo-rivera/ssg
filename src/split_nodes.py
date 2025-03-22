from extract_markdown import extract_markdown_links, extract_markdown_images
from typing import List
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: List[TextNode]):
    new_nodes = []
    for node in old_nodes:
        text: str = node.text
        images = extract_markdown_images(text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            alt, link = image
            image_text = f"![{alt}]({link})"
            split = text.split(image_text, 1)
            first_text = split[0]

            if first_text != "":
                new_nodes.append(
                    TextNode(first_text, TextType.TEXT)
                )

            if alt != "":
                new_nodes.append(
                    TextNode(alt, TextType.IMAGE, link)
                )

            text = split[1]

        if text != "":
            new_nodes.append(
                TextNode(text, TextType.TEXT)
            )
    
    return new_nodes
                
def split_nodes_link(old_nodes: List[TextNode]):
    new_nodes = []
    for node in old_nodes:
        text: str = node.text
        links = extract_markdown_links(text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            hyperlink, url = link
            link_text = f"[{hyperlink}]({url})"
            split = text.split(link_text, 1)
            first_text = split[0]
            
            if first_text != "":
                new_nodes.append(
                TextNode(first_text, TextType.TEXT)
            )

            if hyperlink != "":
                new_nodes.append(
                TextNode(hyperlink, TextType.LINK, url)
            )

            text = split[1]

        if text != "":
            new_nodes.append(
                TextNode(text, TextType.TEXT)
            )
    
    return new_nodes