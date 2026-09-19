import os
from PIL import Image

photo_dir = "photos/originals"

for filename in os.listdir(photo_dir):
    if filename.startswith("photo_") and filename.endswith(".jpeg"):
        path = os.path.join(photo_dir, filename)
        try:
            img = Image.open(path)
            # Split the image into its R, G, B channels
            r, g, b = img.split()
            # Recombine them in B, G, R order to fix the BGR -> RGB issue
            fixed_img = Image.merge("RGB", (b, g, r))
            fixed_img.save(path)
            print(f"Fixed colors for {filename}")
        except Exception as e:
            print(f"Skipping {filename}: {e}")
