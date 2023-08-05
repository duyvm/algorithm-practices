from SortingAlgorithm.Exception import InvalidComparatorEx
from typing import Literal

from .ComparatorABC import ComparatorABC
from .Comparator import GteComparator, LteComparator
from .ComparatorFactoryABC import ComparatorFactoryABC

class ComparatorFactory(ComparatorFactoryABC):
    @classmethod
    def create_comparator(cls, c_type: Literal["gte", "lte"] ) -> ComparatorABC:
        match c_type:
            case "gte":
                return GteComparator()
            case "lte":
                return LteComparator()
            case _:
                raise InvalidComparatorEx(c_type)