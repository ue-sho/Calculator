import queue
from typing import List

from calculator.domain import (
    value,
    variable
)
from calculator.operator import (
    arithmetic,
    assignment
)

class CalculateUseCase:
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'
    SimpleAssign = '='

    def __init__(self):
        self.expression_queue = queue.LifoQueue()
        self.symbol_table = {}

    def handle(self, s: List[str]) -> int:
        for x in s:

            if x.isdigit():
                ex = value.Value(int(x))
                self.expression_queue.put(ex)
            elif x is self.PLUS:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Add(op1, op2)
                self.expression_queue.put(ex)
            elif x is self.MINUS:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Substract(op1, op2)
                self.expression_queue.put(ex)
            elif x is self.MUL:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Multiply(op1, op2)
                self.expression_queue.put(ex)
            elif x is self.DIV:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Divide(op1, op2)
                self.expression_queue.put(ex)
            elif x is self.SimpleAssign:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = assignment.SimpleAssign(op1, op2)
                self.expression_queue.put(ex)
            elif x.isalpha():
                ex = variable.Variable(x, self.symbol_table)
                self.expression_queue.put(ex)
            else:
                raise ValueError('processエラー: %s', x)


        ex = self.expression_queue.get()
        return ex.calc()

