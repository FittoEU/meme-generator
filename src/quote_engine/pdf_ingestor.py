"""Transforms dog quotes from PDF file into usable QuoteModel objects."""

from typing import List
import subprocess
import os
import random

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .txt_ingestor import TxtIngestor

class PDFIngestor(IngestorInterface):
    """Strategic object to represent TXT processing."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses PDF file containing quotes into universally-formatted
        list in two steps:
            1. Using xpdf CLI produce a TXT file
            2. Pass this into TxtIngestor.
        
        :param path: path to PDF quotes file being processed
        :type path: str
        :return: returns list of quotes objects from the PDF file,
                stripped of quotation signs (")
        :rtype: List[QuoteModel]
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot digest this filetipe.')

        base_dir = os.path.dirname(__file__)
        tmp_dir = os.path.abspath(os.path.join(base_dir, '..', 'tmp'))
        os.makedirs(tmp_dir, exist_ok=True)

        tmp_path = os.path.join(tmp_dir,
                                f'{random.randint(0,100000000)}.txt')
        call = subprocess.call(f'pdftotext -layout "{path}" "{tmp_path}"',
                               shell=True)

        quotes = TxtIngestor.parse(tmp_path)
        os.remove(tmp_path)
        return quotes
