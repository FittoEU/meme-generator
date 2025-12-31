"""Meme generator produces extremely hilarious memes by
using quotes collected from wise dogs and nicely placing them
over handsome dog images.
There exists a database of pre-defined quotes and images which are
randomly-generated, but a user is free to provide their own quote text,
quote author, or (logical or) image.
"""

import os
import random

from PIL import Image, ImageDraw, ImageFont

# pylint: disable=too-few-public-methods
class MemeGenerator:
    """A generator putting name on the image and saving the memes."""

    def __init__(self, output_dir:str):
        """Initialise the meme generator by providing it an output folder."""
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def make_meme(self, img_path:str, text:str, author:str, width=500) -> str:
        """
        Create a memetic image accompanied by a wise quote.
        
        :param img_path: path to image to be used for meme
        :param text: text of quote to be drawn on the image
        :param author: author of said quote
        :param width: desired width of image (scaled proportionally)
        """

        with Image.open(img_path) as img:
            # Max width is 500 pixels
            width = min(500, width)

            # Resize image
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), 1)

            # Draw text on the image
            draw = ImageDraw.Draw(img)
            message = f"{text}\n- {author}"
            font = ImageFont.truetype('impact.ttf', size=20)
            draw.text((50, 30), message, font=font, fill='white')

            # Save the meme in output dir folder.
            meme_path = os.path.join(self.output_dir,
                                f'meme_{random.randint(0,100000000)}.jpg')
            img.save(meme_path)
            return meme_path

if __name__=='__main__':
    # to test
    parent_dir = os.path.abspath(__file__ + "/../../")
    meme_dir = os.path.abspath(os.path.join(parent_dir, 'tmp'))
    os.makedirs(meme_dir, exist_ok=True)
    img_dir = os.path.abspath(os.path.join(parent_dir, '_data', 'photos' ,'dog', 'xander_1.jpg'))
    mg = MemeGenerator(meme_dir)
    mg.make_meme(img_dir, 'alkohol', 'Jakov', 200)
