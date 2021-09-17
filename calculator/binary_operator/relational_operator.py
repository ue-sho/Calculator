from calculator.binary_operator.binary_operator import BinaryOperator
from calculator.domain.expression import Expression
from calculator.exception.calculate_error import CalculatorError

class Equal(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() == self.op2.calc()

class NotEqual(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() != self.op2.calc()

class Less(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() < self.op2.calc()

class LessEqual(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() <= self.op2.calc()

class Greater(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() > self.op2.calc()

class GreaterEqual(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        return self.op1.calc() >= self.op2.calc()
