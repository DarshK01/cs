import shutil
import os

def replicate_file_increment(source_file_path, num_copies):
    if not os.path.isfile(source_file_path):
        print(f"File not found: {source_file_path}")
        return

    folder, filename = os.path.split(source_file_path)
    name, ext = os.path.splitext(filename)

    # Create a safe output folder to avoid spamming the original directory
    output_folder = os.path.join(folder, "replication_demo")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Find highest existing copy number
    existing_numbers = []

    for file in os.listdir(output_folder):
        if file.startswith(f"{name}_copy_") and file.endswith(ext):
            num_part = file[len(name) + 6 : -len(ext)]
            if num_part.isdigit():
                existing_numbers.append(int(num_part))

    start = max(existing_numbers) + 1 if existing_numbers else 1

    # Create copies with incrementing numbers
    for i in range(start, start + num_copies):
        new_filename = f"{name}_copy_{i}{ext}"
        new_file_path = os.path.join(output_folder, new_filename)

        try:
            shutil.copy2(source_file_path, new_file_path)
            print(f"Created: {new_filename}")
        except Exception as e:
            print(f"Failed to copy file: {e}")


# Example usage
file_path = r"E:\Replication\hello.txt"
copies = 3
replicate_file_increment(file_path, copies)
