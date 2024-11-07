import os
import shutil

def move_and_rename_files(src_directory, dst_directory, file_extensions):
    file_counter = 1

    print("Scanning the folder...", src_directory)
    # Walk through the source directory
    for dirpath, dirnames, filenames in os.walk(src_directory):
        for filename in filenames:
             if filename.endswith(tuple(file_extensions)):
                # Get the file extension
                file_extension = os.path.splitext(filename)[1]
                # Construct the full file paths
                src_file = os.path.join(dirpath, filename)
                new_filename = f"{file_counter}{file_extension}"
                dst_file = os.path.join(dst_directory, new_filename)
                # Copy and rename the file
                shutil.copy(src_file, dst_file)
                print(f"Copied: {src_file} --> {dst_file}")
                file_counter += 1
        # print("Directories:",dirnames)
                

    print(f"All {file_counter - 1} files have been moved and renamed.")

# Example usage
src_directory = './static/tr/'  # Source folder path
dst_directory = './static/images/'  # Destination folder path
file_extension = ['.png', '.jpg', '.jpeg']  # You can change to any file type, e.g., '.png', '.jpg'

move_and_rename_files(src_directory, dst_directory, file_extension)
