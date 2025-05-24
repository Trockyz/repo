import os
import shutil

# The directory to search from (current directory)
root_dir = os.getcwd()
# Destination directory
dest_dir = r"C:\Users\Trockyz\Downloads\The_Python_Project"

# Walk through the directory tree
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Check if the current directory is named 'src'
    if os.path.basename(dirpath) == 'src':
        for filename in filenames:
            if filename.endswith('.py'):
                src_file = os.path.join(dirpath, filename)
                dest_file = os.path.join(dest_dir, filename)
                print(f"Copying {src_file} to {dest_file}")
                shutil.copy2(src_file, dest_file)