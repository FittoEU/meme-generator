"""Transforms dog quotes from DOCX file into usable QuoteModel objects."""


from typing import List
import docx

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class DocxIngestor(IngestorInterface):
    """Strategic object to represent DOCX processing."""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses DOCX file containing quotes into universally-formatted
        list.
        
        :param path: path to DOCX quotes file being processed
        :type path: str
        :return: returns list of quotes objects from the DOCX file,
                stripped of quotation signs (")
        :rtype: List[QuoteModel]
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot digest this filetipe.')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split(' - ')
                new_quote = QuoteModel(parsed[0].strip('"'),
                                       parsed[1].strip('"'))
                quotes.append(new_quote)

        return quotes
