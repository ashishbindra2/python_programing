from os import path
from os import makedirs
from os import listdir
from os import walk
from pdf2image import convert_from_path

from concurrent.futures import ThreadPoolExecutor

UPLOAD_DIRECTORY = ''
POPPLER_PATH = r"C:\Users\Bindra\Downloads\Documents\Release-24.02.0-0\poppler-24.02.0\Library\bin"
def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)
def find_pdfs(directory):
    pdf_files = []
    for root, dirs, files in walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(path.join(root, file))
    return pdf_files


def save_image(image, image_path, quality=95):
    image.save(image_path, 'PNG', quality=quality)
    print(f"Image saved: {image_path}")


def pdf_2_images(pdf_path: str, dpi=300, quality=95, max_workers=4):
    try:

        print(f"This {pdf_path} will be converted to .PNG images")
        
        # pdf_name = (path.basename(pdf_path))
        # pdf_file = path.splitext(pdf_name)[0]
        
        # makedirs(output_dir, exist_ok=True)
        # print(f"File {output_dir} will store here current dir")

        # Convert PDF to images
        images = convert_from_path(pdf_path, dpi=dpi, poppler_path=POPPLER_PATH)
        image_paths = []

        print("done", images)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for i, image in enumerate(images):
                image_path = path.join('./data', f"I{i + 1}.png")
                image_paths.append(image_path)
                futures.append(executor.submit(save_image, image, image_path, quality))

            for future in futures:
                future.result()  # Wait for all threads to complete

        return "data"
    except Exception as e:
        print(e, "pdf to images failed!!!")


if __name__ == '__main__':
    pdfs = find_pdfs('./data_pdf')
    duplicates = find_duplicates(pdfs)

    for pdf in pdfs:
        pdf_2_images(pdf)
    print(f'the dublicate pdf are {duplicates}')  # Output: [2, 3]
    # pdf_2_images("./data_pdf\LEVEL\Level 1 So Real (3).pdf", dpi=300, quality=95)
