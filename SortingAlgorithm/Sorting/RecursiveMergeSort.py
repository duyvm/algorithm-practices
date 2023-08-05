from typing import Literal
from SortingAlgorithm.Comparator import ComparatorABC

from .SorterABC import SorterABC

class RecursiveMergeSorter(SorterABC):
    """
    Implementation of Merge Sort algorithm with recursive technique
    Time Complexity: n*log2(n)
    """
    def __init__(self):
        pass
    
    def sort(self, array: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        if order not in ["asc", "desc"]:
            raise ValueError(f"Invalid order: {order}. Must be 'asc' or 'desc'")
        return self.__merge_sort(array, order)
    
    def __merge_sort(self, array: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        comparator = self.get_comparator(order)
        self.__split_and_merge(array, comparator)
        return array
    
    def __split_and_merge(self, array: list[int], comparator: ComparatorABC) -> None:
        if len(array) <= 1:
            return
        else:
            mid = len(array) // 2
            left_array = array[0:mid]
            right_array = array[mid:]
        
        # sort left
        self.__split_and_merge(left_array, comparator)
        
        # sort right
        self.__split_and_merge(right_array, comparator)
        
        l_idx = r_idx = a_idx = 0
        
        # merge two parts
        while l_idx < len(left_array) and r_idx < len(right_array):
            if comparator.compare(right_array[r_idx], left_array[l_idx]):
                array[a_idx] = left_array[l_idx]
                l_idx += 1
            else:
                array[a_idx] = right_array[r_idx]
                r_idx += 1
            
            a_idx += 1
                
        # left over in left part, if any
        while l_idx < len(left_array):
            array[a_idx] = left_array[l_idx]
            l_idx += 1
            a_idx += 1
                
        # left over in right part, if any
        while r_idx < len(right_array):
            array[a_idx] = right_array[r_idx]
            r_idx += 1
            a_idx += 1