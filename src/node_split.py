from typing import List
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text == "":
            new_nodes.append(TextNode("", TextType.TEXT))

        split_by_delimiter = node.text.split(delimiter)

        if len(split_by_delimiter) % 2 == 0:
            raise Exception("no matching closing delimiter found for opening delimiter")

        for i in range(len(split_by_delimiter)):
            part = split_by_delimiter[i]

            if part == "":
                continue

            special = i % 2 != 0
            text_t = text_type if special else TextType.TEXT
            new_nodes.append(
                TextNode(part, text_t)
            )

    return new_nodes


