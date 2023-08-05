from typing import Literal

from .SorterABC import SorterABC

class CountingSorter(SorterABC):
    """
    Implementation of counting sort algorithm for sorting array of intergers
    Time complexity: O(n + k)
        n (actually 2*n): one pass over arr to find min, max
             one pass over arr to fill in counting array
        k = max - min: one pass over counting array (with k elements) to create result array
    """
    def __init__(self):
        pass
    
    def sort(self, arr: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        return self.__counting_sort(arr, order)
    
    def __counting_sort(self, arr: list[int], order: Literal["asc", "desc"] = "asc") -> list[int]:
        # find max-min in arr
        min_ele = float("inf")
        max_ele = float("-inf")
        
        for i in arr:
            min_ele = min(min_ele, i)
            max_ele = max(max_ele, i)
        
        range_ele = max_ele - min_ele + 1
        offset = min_ele
        
        count_arr = [0] * range_ele
        for i in arr:
            idx = i - offset
            count_arr[idx] += 1
            
        result = []
        
        if order == "asc":
            start, end, step = 0, range_ele, 1
        else:
            start, end, step = range_ele - 1, -1, -1
        
        for i in range(start, end, step):
            count = count_arr[i]
            while count > 0:
                result.append(i+offset)
                count -= 1
                
        return result