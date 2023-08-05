class InvalidComparatorEx(Exception):
    def __init__(self, c_type: str):
        super().__init__(f"Invalid comparator type {c_type}")
        
class InvalidSorterEx(Exception):
    def __init__(self, s_type: str):
        super().__init__(f"Invalid sorter type {s_type}")