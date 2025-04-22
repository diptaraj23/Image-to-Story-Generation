import os
from app.captioning import generate_caption

# Build image path relative to this file
file_name = "IMG_3736.jpg"
image_path = os.path.join(os.path.dirname(__file__), file_name)

caption = generate_caption(image_path)  # Put a real image path here
print("Caption:", caption)