
from typing import Literal
from SortingAlgorithm.Comparator import ComparatorABC

from .SorterABC import SorterABC

class QuickSorter(SorterABC):
    """
    Implementation of quick sort algorithm
    """
    def __init__(self):
        pass
    
    def sort(self, array: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        if order not in ["asc", "desc"]:
            raise ValueError(f"Invalid order: {order}. Must be 'asc' or 'desc'")
        return self.__quick_sort(array, order)
    
    def __quick_sort(self, array: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        comparator = self.get_comparator(order)
        return self.__partition(array, 0, len(array)-1, comparator)
    
    def __partition(self, array: list[int], low: int, high: int, comparator: ComparatorABC) -> list[int]:
        """
        low, high: inclusive indices of array
        pick element at high index as pivot
        """
        if low >= high:
            return array
        
        # set pivot
        pivot = array[low]
        mid_index = low
        
        for i in range(low+1, high+1):
            if comparator.compare(array[i], pivot):
                continue
            else:
                # swap
                mid_index += 1
                array[i], array[mid_index] = array[mid_index], array[i]
        else:
            # final swap with pivot
            array[low], array[mid_index] = array[mid_index], array[low]
        
        # sort left side
        array = self.__partition(array, low, mid_index-1, comparator)
        
        # sort right side
        array = self.__partition(array, mid_index+1, high, comparator)
        
        return array    
