from abc import abstractmethod

from calculator.domain.expression import Expression

class UnaryOperator(Expression):
    def __init__(self, op1: Expression):
        self.op1 = op1

    @abstractmethod
    def calc(self) -> int:
        pass
