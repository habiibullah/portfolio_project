"""Create a function to write compressed images to disk or memory for image compression algorithm.
"""
from PIL import Image
import io

def write_compressed_image(image, file_path=None, image_data=None):
    if file_path:
        # Write compressed image to disk
        image.save(file_path, optimize=True, quality=50)
    elif image_data:
        # Write compressed image to memory
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", optimize=True, quality=50)
        image_data = buffer.getvalue()
    else:
        # Raise an exception if neither file_path nor image_data is provided
        raise ValueError("Either file_path or image_data must be provided")
                                                                                            
    return image_data


