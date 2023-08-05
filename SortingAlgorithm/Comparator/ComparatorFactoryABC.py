from abc import ABC, abstractmethod
from typing import Literal

from .ComparatorABC import ComparatorABC

class ComparatorFactoryABC(ABC):
    @classmethod
    @abstractmethod
    def create_comparator(cls, c_type: Literal["gte", "lte"] ) -> ComparatorABC:
        pass