import fitz
import os

pdf_path = "suhaniiiii.pdf.pdf"
output_dir = "suhani-birthday/photos/originals"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

doc = fitz.open(pdf_path)
count = 1
for i in range(len(doc)):
    for img in doc.get_page_images(i):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = os.path.join(output_dir, f"photo_{count:03d}.{image_ext}")
        with open(image_filename, "wb") as f:
            f.write(image_bytes)
        count += 1

print(f"Extracted {count-1} images.")
