"""Create a function that takes a compressed image as input and returns the decompressed image."""

from PIL import Image

def decompress_image(compressed_image_path):
    # Open the compressed image
    compressed_image = Image.open(compressed_image_path)
                
    # Decompress the image
    decompressed_image = compressed_image.copy()
                            
    return decompressed_image

