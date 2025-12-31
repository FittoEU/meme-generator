"""Interface that serves as template to standardise individual
file ingestors.
"""

from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel

class IngestorInterface(ABC):
    """An abstract class to represent ingestor interface.
    
    allowed_extensions: List(str)
    """
    allowed_extensions: List[str] = []

    @classmethod
    def can_ingest(cls, path:str) -> bool:
        """Checks if extension is digestible by strategy object."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """An abstract method developed in strategy objects."""
        pass
