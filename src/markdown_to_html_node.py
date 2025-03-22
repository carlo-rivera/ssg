from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnodes import text_to_textnodes
from text import text_node_to_html_node
from markdown_blocks import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks

def get_heading_level(block: str):
    level = 0
    for char in block:
        if char == "#":
            level += 1
    return level

def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(
            text_node_to_html_node(text_node)
        )

    return html_nodes
        
def make_html_node(block: str, block_type: BlockType):
    if block_type == BlockType.PARAGRAPH:
        node = ParentNode("p", text_to_children(
            block.replace("\n", " ")
        ))
        return node
    if block_type == BlockType.HEADING:
        inline = block.lstrip("# ")
        node = ParentNode(f"h{get_heading_level(block)}", text_to_children(inline.replace("\n", " ")))
        return node
    if block_type == BlockType.CODE:
        inline = block.strip("`").lstrip()
        node = ParentNode("pre", 
            [LeafNode("code", inline)]
        )
        return node
    if block_type == BlockType.QUOTE:
        inlines = []

        for line in block.split("\n"):
            inlines.append(line.lstrip("> "))

        inline = "\n".join(inlines)

        node = ParentNode("blockquote", text_to_children(inline))
        return node
    if block_type == BlockType.UNORDERED_LIST:
        items = []

        for line in block.split("\n"):
            items.append(
                ParentNode("li", text_to_children(
                    line.lstrip("- ")
                ))
            )

        node = ParentNode("ul", items)
        return node
    if block_type == BlockType.ORDERED_LIST:
        items = []
        cur_num = 1

        for line in block.split("\n"):
            items.append(
                ParentNode("li", text_to_children(
                    line.lstrip(f"{cur_num}. ")
                ))
            )
            cur_num += 1

        node = ParentNode("ol", items)
        return node

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        node = make_html_node(block, block_type)
        block_nodes.append(node)
    parent = ParentNode("div", block_nodes)
    return parent