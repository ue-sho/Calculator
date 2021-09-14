from calculator.binary_operator.binary_operator import BinaryOperator
from calculator.domain.expression import Expression
from calculator.domain.variable import Variable
from calculator.exception.calculate_error import CalculatorError

class SimpleAssign(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise CalculatorError('オペランド1がVariable型ではありません')
        num = self.op2.calc()
        self.op1.set_value(num)
        return num

class AddAssign(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise CalculatorError('オペランド1がVariable型ではありません')
        num = self.op1.calc() + self.op2.calc()
        self.op1.set_value(num)
        return num

class SubAssign(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise CalculatorError('オペランド1がVariable型ではありません')
        num = self.op1.calc() - self.op2.calc()
        self.op1.set_value(num)
        return num

class MulAssign(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise CalculatorError('オペランド1がVariable型ではありません')
        num = self.op1.calc() * self.op2.calc()
        self.op1.set_value(num)
        return num

class DivAssign(BinaryOperator):
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        if type(self.op1) == type(Variable):
            raise CalculatorError('オペランド1がVariable型ではありません')
        num = self.op1.calc() / self.op2.calc()
        self.op1.set_value(num)
        return num
