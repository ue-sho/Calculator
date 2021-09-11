from calculator.operator.binary_operator import BinaryOperator
from calculator.domain.expression import Expression
from calculator.domain.variable import Variable

class SimpleAssign(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise ValueError('op1がVariable型じゃない')
        num = self.op2.calc()
        self.op1.set_value(num)
        return num

