from abc import ABC, abstractmethod
from typing import Literal
from SortingAlgorithm.Comparator import ComparatorABC, ComparatorFactory

class SorterABC(ABC):
    @abstractmethod
    def sort(self, array: list, order: Literal["asc", "desc"] = "asc") -> list:
        pass
    
    @staticmethod
    def get_comparator(order: Literal["asc", "desc"] = "asc") -> ComparatorABC:
        if order == "asc":
            return ComparatorFactory.create_comparator("gte")
        else:
            return ComparatorFactory.create_comparator("lte")