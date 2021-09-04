from calculator.domain.expression import Expression

class Value(Expression):
    def __init__(self, num: int):
        self.num = num

    def calc(self) -> int:
        return self.num
