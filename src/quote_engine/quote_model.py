"""Useful quote object that can be used for things like meme
generation and similar uses.
"""

class QuoteModel():
    """A class representing a quote, with text and author."""

    def __init__(self, body:str, author:str):
        self.body = body
        self.author = author

    def __str__(self):
        return f"{self.body} - {self.author}"

    def __repr__(self):
        return f"<QuoteModel; text: \"{self.body}\"; " \
                f"author: \"{self.author}\">"
