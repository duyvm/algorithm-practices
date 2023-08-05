from abc import ABC, abstractmethod
from SortingAlgorithm.Config import VALID_SORT_ALGORITHM

from .SorterABC import SorterABC

class SorterFactoryABC(ABC):
    @classmethod
    @abstractmethod
    def create_sorter(cls, s_type: VALID_SORT_ALGORITHM) -> SorterABC:
        pass