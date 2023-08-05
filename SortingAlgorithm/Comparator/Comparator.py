from .ComparatorABC import ComparatorABC

class GteComparator(ComparatorABC):
    @classmethod
    def compare(cls, a: int, b: int) -> bool:
        return a >= b
    
class LteComparator(ComparatorABC):
    @classmethod
    def compare(cls, a: int, b: int) -> bool:
        return a <= b    