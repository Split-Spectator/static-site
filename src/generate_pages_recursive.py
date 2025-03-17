import os 
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    os.makedirs(dest_dir_path, exist_ok=True)
    for entry in os.listdir(dir_path_content):
        
        source_path = os.path.join(dir_path_content, entry)
        if entry.endswith(".md"):
             
                html_filename = entry[:-3] + ".html"   
                dest_path = os.path.join(dest_dir_path, html_filename)
                
                generate_page(source_path, template_path, dest_path)
                
                print("generated singualar page")
                
        elif os.path.isdir(source_path):
 
            dest_subdir = os.path.join(dest_dir_path, entry)
            
            print("recursive call utilized")
            
            generate_pages_recursive(source_path, template_path, dest_subdir)