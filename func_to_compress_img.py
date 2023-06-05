"""Create a function that takes an image as input and returns the compressed image."""

from PIL import Image

def compress_image(image):
    # Copy the image to avoid modifying the original
    compressed_image = image.copy()
                
    # Compress the image
    compressed_image.save("compressed_image.jpg", optimize=True, quality=50)
                            
    return compressed_image

