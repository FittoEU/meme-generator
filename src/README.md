# MEME GENERATOR
Hello and welcome to Meme Generator!

### ABOUT
Meme generator is a tool designed to build memes - images with quotes
overlaid on top of them.

There are three ways one can use a meme generator:
1. Using command line interface (CLI). This requires a local copy of the
Meme Generator.
2. Using the web app. This requires deploying the Meme Generator to a
server.
3. Using MemeGenerator code to implement it in your own, upgraded meme
code.

Meme Generator allows users to use their own image (if no image is picked,
one will be randomly selected from Meme Generator database). It also
allows users to input their own quote (made up from body of the quote and
author of the quote). If no quote is input, one will be randomly selected
from Meme Generator database. If accessed via CLI, the memes are output
to a user-provided file (default: /tmp/), and if accessed via web, the
memes are output directly to the browser.

### SETUP
If you have downloaded the Meme Generator, simply run the terminal from
the download folder and use
`$ python meme.py`
This will automatically generate a meme to the app's /tmp/ folder. The
image and quote to be used will be from Meme Generator's /database/ which
you are free to expand with your own files.
If you want to use your own image and/or quote by providing three
additional optional arguments to the terminal:
`$ python meme.py --path <path to image file> --body <quote text> --author <quote author>`
Please note that if you provide a body without an author, the app will
raise an exception.

If you'd like to deploy the Meme Generator to website, you can use flask
with app.py to deploy it.
When accessing the Meme Generator online, you can post a path to your
image, input your own quote and author, or let Meme Generator use its
database to fill in the missing elements required to generate a meme.

### STRUCTURE
Meme generator consists of two main modules, connected together by the
main module. The two modules are:
1. Main: connects the two sub-modules and deploys the meme generator
to web or enables use through CLI.
     - Dependencies: os, random, argparse, flask, requests; meme_generator
     and quote_generator
2. quote_generator: a module for parsing text containing quotes for memes
from different files (pdf, docx, txt, csv).
    - Dependencies: os, random, typing, subprocess, abc, docx, pandas and
    xpdf's pdftotext which a 3rd party app accessed by Meme Generator via
    subprocess.
3. meme_generator: a module for overlaying a quote (QuoteModel object from
quote_generator) on top of image.
    - Dependencies: os, random, PIL
