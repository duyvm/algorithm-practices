from abc import ABC, abstractmethod

class ComparatorABC(ABC):
    @classmethod
    @abstractmethod
    def compare(cls, a: int, b: int) -> bool:
        pass