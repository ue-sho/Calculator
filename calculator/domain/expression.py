from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def calc(self) -> int:
        pass
