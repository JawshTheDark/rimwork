import os
import shutil
import time
import xml.etree.ElementTree as ET

# The directory to monitor for new folders
src_dir = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\294100"

# The directory to copy new folders to
dst_dir = r"C:\Program Files (x86)\Steam\steamapps\common\RimWorld\Mods"

# Keep track of the folders in the source directory
src_folders = set(os.listdir(src_dir))

# Keep track of the folders already processed
processed_folders = set()

while True:
    # Get a list of all subdirectories in the source directory
    subdirs = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]
    
    # Check each subdirectory in the source directory
    for subdir in subdirs:
        # Ignore folders starting with ".temp_write_"
        if subdir.startswith(".temp_write_"):
            continue
        
        # Get the full path to the subdirectory
        src_path = os.path.join(src_dir, subdir)
        
        # Check if the folder has already been processed
        if subdir in processed_folders:
            continue
        
        # Check if a folder with the same name exists in the destination directory
        dst_path = os.path.join(dst_dir, subdir)
        if os.path.exists(dst_path):
            print(f"Folder {subdir} already exists in {dst_dir}, skipping.")
        else:
            # Copy the folder to the destination directory
            shutil.copytree(src_path, dst_path)
            print(f"Copied {subdir} to {dst_dir}.")
            
            # Rename the folder based on the name in About.xml
            about_dir = os.path.join(dst_path, "About")
            about_xml = os.path.join(about_dir, "About.xml")
            if os.path.exists(about_xml):
                tree = ET.parse(about_xml)
                root = tree.getroot()
                name = root.find('name').text.replace(" ", "").replace(":", "-")
                new_dst_path = os.path.join(dst_dir, name)
                os.rename(dst_path, new_dst_path)
                print(f"Renamed {dst_path} to {new_dst_path}.")
            else:
                print(f"No About.xml found in {about_dir}, skipping rename.")
        
        # Mark the folder as processed
        processed_folders.add(subdir)
    
    # Check for new folders in the source directory
    new_folders = set(os.listdir(src_dir)) - src_folders
    for folder in new_folders:
        if folder not in processed_folders and not folder.startswith(".temp_write_"):
            print(f"New folder found in {src_dir}: {folder}")
            processed_folders.add(folder)
    
    # Update the list of folders in the source directory
    src_folders = set(os.listdir(src_dir))
    
    # Wait for 1 second before checking again
    time.sleep(1)

