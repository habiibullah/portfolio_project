"""Create a function to read images from disk or from memory for image compression algorithm using python
"""
from PIL import Image
import io

def read_image(file_path=None, image_data=None):
    if file_path:
       # Read image from disk
       image = Image.open(file_path)
    elif image_data:
       # Read image from memory
       image = Image.open(io.BytesIO(image_data))
    else:
       # Raise an exception if neither file_path nor image_data is provided
       raise ValueError("Either file_path or image_data must be provided")
                                                                            
    return image

