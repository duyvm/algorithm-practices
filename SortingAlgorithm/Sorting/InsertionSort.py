from typing import Literal

from .SorterABC import SorterABC

class InsertionSorter(SorterABC):
    """
    Implementation of insertion sort algorithm
    """
    def __init__(self):
        pass
    
    def sort(self, array: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        if order not in ["asc", "desc"]:
            raise ValueError(f"Invalid order: {order}. Must be 'asc' or 'desc'")
        return self.__insertion_sort(array, order)
    
    def __insertion_sort(self, array: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        comparator = self.get_comparator(order)
        for i in range(1, len(array)):
            cur = array[i]
            for j in range(i-1, -1, -1):
                if comparator.compare(array[j], cur):
                    array[j+1] = array[j]
                else:
                    array[j+1] = cur
                    break
            else:
                array[0] = cur
                
        return array