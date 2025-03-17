import os 
import shutil

def dup_static(path_public, path_static):
    # Clear the destination directory
    if os.path.exists(path_public):
        shutil.rmtree(path_public) 
    os.mkdir(path_public)

    # Copy each item from source to destination
    for item in os.listdir(path_static): 
        source_item = os.path.join(path_static, item)
        dest_item = os.path.join(path_public, item)
       
        if os.path.isfile(source_item):
            # For files, just copy them
            print(f"Copying file: {source_item} to {dest_item}")
            shutil.copy(source_item, dest_item)
        else:
            # For directories, create them and recursively copy contents
            print(f"Copying directory: {source_item} to {dest_item}")
            os.mkdir(dest_item)  # Create the destination subdirectory
            dup_static(dest_item, source_item)  # Note the order of parameters

 
