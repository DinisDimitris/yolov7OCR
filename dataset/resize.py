import argparse

from PIL import Image
import os

def resize_images(directory, target_size=(640, 640)):
    """
    Resizes all images in the specified directory to the target size.

    Args:
    directory (str): The path to the directory containing images.
    target_size (tuple): A tuple specifying the target size (width, height).

    Returns:
    None
    """
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Add more extensions if needed
            filepath = os.path.join(directory, filename)
            try:
                img = Image.open(filepath)
                img = img.resize(target_size, Image.ANTIALIAS)
                img.save(filepath)
            except Exception as e:
                print(f"Error resizing {filename}: {e}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, required=True, help='path for images to resize')
    args = vars(parser.parse_args())
    resize_images(args['dir'])