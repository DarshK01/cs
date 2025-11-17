import shutil
import os

source = "original.txt"
copies = 5

if not os.path.isfile(source):
    print(f"Error: Source file not found at '{source}'")
    print("No files were copied.")
else:
    print(f"Source file '{source}' found. Starting to copy...")
    for i in range(1, copies + 1):
        dest = f"copy_{i}.txt"
        
        try:
            shutil.copy(source, dest)
            print(f"Created {dest}")
        except Exception as e:
            print(f"Failed to create {dest}: {e}")

    print("Copying complete.")