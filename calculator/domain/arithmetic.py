from calculator.domain.binary_operator import BinaryOperator
from calculator.domain.expression import Expression

class Add(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() + self.op2.calc()

class Substract(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() - self.op2.calc()

class Multiply(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() * self.op2.calc()

class Divide(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() * self.op2.calc()