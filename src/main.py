import sys 
import os 
from textnode import TextNode, TextType
from dup_static import dup_static 
from generate_pages_recursive import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    public_path = "docs" 
    static_path = "static"
         
    dup_static(public_path, static_path)

    from_path = "content"
    template_path = "template.html"
    dest_path = "docs"
    generate_pages_recursive(from_path, template_path, dest_path, basepath)
 
if __name__ == "__main__":
    main()

