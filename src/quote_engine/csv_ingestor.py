"""Transforms dog quotes from CSV file into usable QuoteModel objects."""

from typing import List
import pandas

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    """Strategic object to represent CSV processing."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """
        Parses CSV file containing quotes into universally-formatted
        list.
        
        :param path: path to CSV quotes file being processed
        :type path: str
        :return: returns list of quotes objects from the CSV file,
                stripped of quotation (") signs
        :rtype: List[QuoteModel]
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot digest this filetipe.')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'].strip('"'),
                                   row['author'].strip('"'))
            quotes.append(new_quote)
        return quotes
