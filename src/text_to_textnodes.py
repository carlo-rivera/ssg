from textnode import TextNode, TextType
from node_split import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bolded = split_nodes_delimiter([node], "**", TextType.BOLD)
    italicized = split_nodes_delimiter(bolded, "_", TextType.ITALIC)
    coded = split_nodes_delimiter(italicized, "`", TextType.CODE)
    imaged = split_nodes_image(coded)
    final = split_nodes_link(imaged)
    return final