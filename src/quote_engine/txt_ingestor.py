"""Transforms dog quotes from TXT file into usable QuoteModel objects."""

from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class TxtIngestor(IngestorInterface):
    """Strategic object to represent TXT processing."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses TXT file containing quotes into universally-formatted
        list.
        
        :param path: path to TXT quotes file being processed
        :type path: str
        :return: returns list of quotes objects from the TXT file,
                stripped of quotation signs (")
        :rtype: List[QuoteModel]
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot digest this filetipe.')

        quotes = []
        with open(path, encoding='utf-8') as infile:
            contents = infile.readlines()
            for line in contents:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split(' - ')
                    new_quote = QuoteModel(parsed[0].strip('"'),
                                           parsed[1].strip('"'))
                    quotes.append(new_quote)
            return quotes
