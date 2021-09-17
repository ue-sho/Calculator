from abc import abstractmethod

from calculator.domain.expression import Expression
from calculator.unary_operator.unary_operator import UnaryOperator

class LogicalNot(UnaryOperator):
    def __init__(self, op1: Expression):
        super().__init__(op1)

    def calc(self) -> int:
        return not (self.op1.calc())
