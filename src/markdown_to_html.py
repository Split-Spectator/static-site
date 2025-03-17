from block_type import BlockType, block_to_block_type 
from blocks import markdown_to_blocks
from htmlnode import HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline import text_to_textnodes

def text_to_children(text):
    # Normalize whitespace: Replace newlines and multiple spaces with a single space
    normalized_text = ' '.join(text.split())
    text_nodes = text_to_textnodes(normalized_text)
    
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    
    return html_nodes

     
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        if not block.strip():
            continue  # Skip empty blocks
            
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.CODE:
            # Extract the content between the triple backticks
            lines = block.strip().split("\n")
            
            # Get the content lines (exclude the triple backtick lines)
            content_lines = lines[1:-1] if len(lines) > 2 else []
            
            # Find the common indentation to remove
            non_empty_lines = [line for line in content_lines if line.strip()]
            common_indent = min([len(line) - len(line.lstrip()) for line in non_empty_lines]) if non_empty_lines else 0
            
            # Remove common indentation from each line
            cleaned_lines = [line[common_indent:] if len(line) >= common_indent else line for line in content_lines]
            
            # Join the lines with newlines
            code_content = "\n".join(cleaned_lines) + "\n"
            
            # Create text node directly (no inline parsing)
            text_node = TextNode(code_content, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            code_node = HTMLNode("code", None, [html_node], {})
            pre_node = HTMLNode("pre", None, [code_node], {})
            children.append(pre_node)

        elif block_type == BlockType.PARAGRAPH:
            p_node = HTMLNode("p", None, text_to_children(block), {}) # here 
            children.append(p_node)
        elif block_type == BlockType.HEADING:
            level = block.count("#", 0, 6)   
            heading_node = HTMLNode(f"h{level}", None, text_to_children(block.lstrip("# ").strip()), {})

            children.append(heading_node)
        
        elif block_type == BlockType.UNORDERED_LIST:
            # Process list items
            items = []
            for line in block.strip().split("\n"):
                item_text = line.strip()[2:].strip()  # Remove the "- " and any extra whitespace
                li_node = HTMLNode("li", None, text_to_children(item_text), {})
                items.append(li_node)
            ul_node = HTMLNode("ul", None, items, {})
            children.append(ul_node) 

        elif block_type == BlockType.ORDERED_LIST:
        # Process ordered list items
            items = []
            for line in block.strip().split("\n"):
             # Get text after the digit and period
                item_text = line.strip()
               # Find the first period to skip the number
                period_index = item_text.find('.')
                if period_index != -1:
                    item_text = item_text[period_index + 1:].strip()
                li_node = HTMLNode("li", None, text_to_children(item_text), {})
                items.append(li_node)
            ol_node = HTMLNode("ol", None, items, {})
            children.append(ol_node)
        
        elif block_type == BlockType.QUOTE:
        # Process quote - strip the ">" from the beginning of each line
            lines = []
            for line in block.strip().split("\n"):
                if line.startswith("> "):
                    lines.append(line[2:])  # Remove "> "
                elif line.startswith(">"):
                    lines.append(line[1:])  # Remove ">"
                else:
                    lines.append(line)  # Keep as is
            
            quote_text = " ".join(lines)
            quote_node = HTMLNode("blockquote", None, text_to_children(quote_text), {})
            children.append(quote_node)

    

    return HTMLNode("div", None, children, {})
