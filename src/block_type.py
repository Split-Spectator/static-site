from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith('#'):
        pound_count = 0
        for char in block:
            if char == '#':
                pound_count += 1
            else:
                break
        if 1 <= pound_count <= 6 and block[pound_count] == ' ':
            return BlockType.HEADING

    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    # Check for quote blocks
    lines = block.split('\n')
    if lines and lines[0].startswith('> '):
        return BlockType.QUOTE
    
    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST

    if lines and lines[0].startswith('1. '):
        expected_number = 1
        is_ordered_list = True
        for line in lines:
            expected_number_str = f"{expected_number}. "
            if not line.startswith(expected_number_str):
                is_ordered_list = False
                break
            expected_number += 1
        if is_ordered_list:
            return BlockType.ORDERED_LIST
     
    return BlockType.PARAGRAPH