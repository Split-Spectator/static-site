def markdown_to_blocks(markdown):
     
    start_blocks = markdown.split("\n\n")  
    blocks = []
    for block in start_blocks:
        end_block = block.strip()
        if end_block:
            blocks.append(end_block)
    return blocks