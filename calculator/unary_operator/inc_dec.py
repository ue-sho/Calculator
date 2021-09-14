from abc import abstractmethod

from calculator.domain.expression import Expression
from calculator.unary_operator.unary_operator import UnaryOperator

class Increment(UnaryOperator):
    def __init__(self, op1: Expression):
        super().__init__(op1)

    def calc(self) -> int:
        val = self.op1.calc()
        val += 1
        return val

class Decrement(UnaryOperator):
    def __init__(self, op1: Expression):
        super().__init__(op1)

    def calc(self) -> int:
        val = self.op1.calc()
        val -= 1
        return val
