import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def check_ordered_list(block: str):
    split = block.split("\n")
    cur_num = 1

    for line in split:
        if not line.startswith(f"{cur_num}. "):
            return False
        cur_num += 1

    return True

def block_to_block_type(block: str):
    heading_pattern = r"^#{1,6} "
    if re.match(heading_pattern, block):
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if all(line.startswith("> ") or line == ">" for line in block.split("\n")):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    
    if check_ordered_list(block):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
