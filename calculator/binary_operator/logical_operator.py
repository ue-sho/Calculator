from calculator.binary_operator.binary_operator import BinaryOperator
from calculator.domain.expression import Expression



class Both(BinaryOperator):
    """
    &&演算: 通称andだが、Bit演算のandと被るのでBothとする
    """
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        # and はTrueの場合、右値をそのまま返す
        # 0 か 1 にしたいので、ひと手間加える
        num = self.op1.calc() and self.op2.calc()
        return not (not num)

class Either(BinaryOperator):
    """
    ||演算: 通称orだが、Bit演算のorと被るのでEitherとする
    """
    def __init__(self, op1: Expression, op2: Expression):
        super().__init__(op1, op2)

    def calc(self) -> int:
        # or はTrueの場合、その値をそのまま返す
        # 0 か 1 にしたいので、ひと手間加える
        num = self.op1.calc() or self.op2.calc()
        return not (not num)
