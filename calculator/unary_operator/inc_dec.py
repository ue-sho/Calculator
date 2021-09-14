from abc import abstractmethod

from calculator.domain.expression import Expression
from calculator.domain.variable import Variable
from calculator.unary_operator.unary_operator import UnaryOperator

class Increment(UnaryOperator):
    def __init__(self, op1: Expression):
        super().__init__(op1)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise CalculatorError('オペランドがVariable型ではありません')
        num = self.op1.calc()
        num += 1
        self.op1.set_value(num)
        return num

class Decrement(UnaryOperator):
    def __init__(self, op1: Expression):
        super().__init__(op1)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise CalculatorError('オペランドがVariable型ではありません')
        num = self.op1.calc()
        num -= 1
        self.op1.set_value(num)
        return num
