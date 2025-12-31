"""A web-based app that either generates the meme from Meme Generator
database or takes user input in the form of image URL, quote body and
quote author to produce their own meme.
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from quote_engine import Ingestor
from meme_engine import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs

quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # Read the form
    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    if not img_url or not body or not author:
        abort(400, description="Missing required form fields")

    # Prepare file name for downloaded image
    dest = './tmp'
    os.makedirs(dest, exist_ok=True)
    filename = os.path.join(dest, f'temp_image_{random.randint(0,10000)}.jpg')

    # Load image into memory and save to filename
    response = requests.get(img_url, timeout=10)

    try:
        with open(filename, 'wb') as file:
            file.write(response.content)

        path = meme.make_meme(filename, body, author)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
