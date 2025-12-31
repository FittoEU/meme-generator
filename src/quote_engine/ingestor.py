"""Unviersal ingestor capable of identifying file type and applying
suitable individual ingestor to produce QuoteModel objects
from list of quotes.
"""

from typing import List

from .quote_model import QuoteModel
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .txt_ingestor import TxtIngestor
from .ingestor_interface import IngestorInterface

class Ingestor(IngestorInterface):
    """A class representing universal ingestor invoking individual
    ingestors suitable for the identified filetype.
    """
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Iterate through what individual ingestors can ingest
        and return the suitable one.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise Exception("No ingestor found for this filetype.")
