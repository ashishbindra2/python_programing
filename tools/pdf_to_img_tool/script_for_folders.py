from os import path, makedirs, walk
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing

UPLOAD_DIRECTORY = './data'
POPPLER_PATH = r"C:\Users\Bindra\Downloads\Documents\Release-24.02.0-0\poppler-24.02.0\Library\bin"


# Find all PDF files in the given directory
def find_pdfs(directory):
    pdf_files = []
    for root, _, files in walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(path.join(root, file))
    return pdf_files


# Save image with threading
def save_image(image, image_path, quality=95):
    image.save(image_path, 'PNG', quality=quality)
    print(f"Image saved: {image_path}")


# Convert a single PDF to images and save using threading
def process_pdf(pdf_path, start_count=170, dpi=300, quality=95, max_workers=4):
    try:
        print(f"Converting {pdf_path} to images...")

        images = convert_from_path(pdf_path, dpi=dpi, poppler_path=POPPLER_PATH)
        image_paths = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for i, image in enumerate(images, start=start_count):  # Start counting from start_count
                image_path = path.join(UPLOAD_DIRECTORY, f"I{i + 1}.png")
                image_paths.append(image_path)
                futures.append(executor.submit(save_image, image, image_path, quality))

            for future in futures:
                future.result()  # Ensure all threads complete

        return len(images)  # Return the number of images processed for this PDF

    except Exception as e:
        print(f"Failed to convert {pdf_path}: {e}")
        return 0


# Multiprocessing to handle multiple PDFs concurrently
def pdf_to_images_multiprocessing(pdf_files, max_workers=None):
    image_counter = 0  # This will track the total number of images
    if max_workers is None:
        max_workers = multiprocessing.cpu_count()  # Use all available CPUs
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = []
        for pdf in pdf_files:
            # Pass the current image counter as the starting point for numbering
            result = executor.submit(process_pdf, pdf, image_counter)
            num_images = result.result()  # Number of images processed by the current PDF
            image_counter += num_images  # Update the counter after each PDF

    return results


if __name__ == '__main__':
    pdfs = find_pdfs('./data_pdf')

    if not path.exists(UPLOAD_DIRECTORY):
        makedirs(UPLOAD_DIRECTORY)

    num_cpus = multiprocessing.cpu_count()
    pdf_to_images_multiprocessing(pdfs, max_workers=num_cpus)
