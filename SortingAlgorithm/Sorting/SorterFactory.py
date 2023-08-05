from SortingAlgorithm.Exception import InvalidSorterEx
from SortingAlgorithm.Config import VALID_SORT_ALGORITHM
from typing import Literal

from .CountingSort import CountingSorter
from .InsertionSort import InsertionSorter
from .QuickSort import QuickSorter
from .IterativeMergeSort import IterativeMergeSorter
from .RecursiveMergeSort import RecursiveMergeSorter
from .SorterFactoryABC import SorterFactoryABC
from .SorterABC import SorterABC

class SorterFactory(SorterFactoryABC):
    @classmethod
    def create_sorter(cls, s_type: VALID_SORT_ALGORITHM) -> SorterABC:
        match s_type:
            case "CS":
                return CountingSorter()
            case "IS":
                return InsertionSorter()
            case "QS":
                return QuickSorter()
            case "RMS":
                return RecursiveMergeSorter()
            case "IMS":
                return IterativeMergeSorter()
            case _:
                raise InvalidSorterEx(s_type)