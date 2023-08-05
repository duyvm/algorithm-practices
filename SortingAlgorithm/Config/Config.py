from typing import Literal, get_args
from enum import Enum

class SortAlgorithmEnum(Enum):
    CS = "Counting Sort"
    IS = "Insertion Sort"
    QS = "Quick Sort"
    RMS = "Recursive Merge Sort"
    IMS = "Iterative Merge Sort"
    
SORT_ALGORITHM_NAME: dict[str, str] = {i.name: i.value for i in SortAlgorithmEnum}

VALID_SORT_ALGORITHM: list[str] = [ i.name for i in SortAlgorithmEnum ]