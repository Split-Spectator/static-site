import re 
from textnode import TextNode, TextType
print(f"TextType imported: {TextType}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    # Look for markdown link syntax [text](url)
    link_regex = r"\[([^\]]+)\]\(([^)]+)\)"
    links = []
    
    # Find all matches
    for match in re.finditer(link_regex, text):
        link_text = match.group(1)
        link_url = match.group(2)
        links.append((link_text, link_url))
    
    return links


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        image_delimiters = extract_markdown_images(text)

        if not image_delimiters:
            new_nodes.append(old_node)
            continue

        remaining_text = text

        for image_alt, image_url in image_delimiters:
            
            image_markdown = f"![{image_alt}]({image_url})"
            sections = remaining_text.split(image_markdown, 1)

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
 
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        link_delimiters = extract_markdown_links(text)

        if not link_delimiters:
            new_nodes.append(old_node)
            continue

        remaining_text = text

        for link_text, link_url in link_delimiters:
            link_markdown = f"[{link_text}]({link_url})"
            sections = remaining_text.split(link_markdown, 1)

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    if not text:
        return [TextNode("", TextType.TEXT)]
     
    nodes = [TextNode(text, TextType.TEXT)]
     
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes