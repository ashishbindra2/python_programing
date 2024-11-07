import os
import glob

def rename_images(directory, new_name_prefix):
    # Get all image files in the directory with common image extensions
    image_extensions = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff')
    image_files = []
    
    # Loop through all image extensions and collect image file paths
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(directory, ext)))

    print(image_files)
    
    if not image_files:
        print("No images found in the directory.")
        return

    # Rename each image
    for index, image_path in enumerate(image_files, start=1757):
        # Extract file extension
        file_extension = os.path.splitext(image_path)[1]
        # Create new file name using the new_name_prefix and index
        new_name = f"{new_name_prefix}{index}{file_extension}"
        # Construct the new full file path
        new_path = os.path.join(directory, new_name)
        # Rename the image
        os.rename(image_path, new_path)
        print(f"Renamed {image_path} to {new_name}")

# Usage Example
directory = r"./data/"  # Replace with your folder path
new_name_prefix = "I"  # Set the prefix for the new image names
rename_images(directory, new_name_prefix)
