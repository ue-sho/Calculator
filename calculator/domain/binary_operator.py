from abc import abstractmethod

from calculator.domain.expression import Expression

class BinaryOperator(Expression):
    def __init__(self, op1: Expression, op2: Expression):
        self.op1 = op1
        self.op2 = op2

    @abstractmethod
    def calc(self):
        return
