import copy
from typing import Literal
from SortingAlgorithm.Comparator import ComparatorABC

from .SorterABC import SorterABC

class IterativeMergeSorter(SorterABC):
    """
    Implementation of Merge Sort algorithm with iterative technique
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
        return self.__split_and_merge(array, comparator)
    
    def __split_and_merge(self, array: list[int], comparator: ComparatorABC) -> list[int]:
        n = len(array)
        auxiliary_array = copy.deepcopy(array)
        pair_range = IterativeMergeSorter.get_pair_range(n)
        while len(pair_range) > 0:
            left, right = pair_range.pop()
            left_start, left_end = left
            right_start, right_end = right
            aux_arr_start = left_start

            # compare and assign value to auxiliary array
            while left_start <= left_end and right_start <= right_end:
                if comparator.compare(array[right_start], array[left_start]):
                    auxiliary_array[aux_arr_start] = array[left_start]
                    left_start += 1
                else:
                    auxiliary_array[aux_arr_start] = array[right_start]
                    right_start += 1
                    
                aux_arr_start += 1
                
            # left over in left part, if any
            while left_start <= left_end:
                auxiliary_array[aux_arr_start] = array[left_start]
                left_start += 1
                aux_arr_start += 1
                
            # left over in right part, if any
            while right_start <= right_end:
                auxiliary_array[aux_arr_start] = array[right_start]
                right_start += 1
                aux_arr_start += 1
            
            # update array with auxiliary_array
            array = copy.deepcopy(auxiliary_array)

        return array
    
    @classmethod
    def get_pair_range(cls, n: int) -> list[tuple[int]]:
        pair_range = []
        
        # init pair, pair is inclusive
        pair_range.append([(0, n//2-1), (n//2, n-1)])
        
        i = 0
        while True:
            left, right = pair_range[i]
    
            # left part
            if left[1] != left[0]:
                left_mid = (left[1] + left[0]) // 2
                pair_range.append([(left[0], left_mid), (left_mid+1, left[1])])
            
            # right
            if right[1] != right[0]:
                right_mid = (right[1] + right[0]) // 2
                pair_range.append([(right[0], right_mid), (right_mid+1, right[1])])
            
            i += 1
            
            if i >= len(pair_range):
                break
        
        return pair_range