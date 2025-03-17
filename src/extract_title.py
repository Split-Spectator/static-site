def extract_title(markdown):
    
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    raise Exception("No h1 header found in the markdown content")