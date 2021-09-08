import queue
from typing import List

from calculator.domain import arithmetic, value


class Calculator:
    NUMBER_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'

    def __init__(self):
        self.expression_queue = queue.LifoQueue()

    def process(self, s: List[str]) -> int:
        for x in s:

            if x in Calculator.NUMBER_LIST:
                ex = value.Value(int(x))
                self.expression_queue.put(ex)
            elif x is Calculator.PLUS:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Add(op1, op2)
                self.expression_queue.put(ex)
            elif x is Calculator.MINUS:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Substract(op1, op2)
                self.expression_queue.put(ex)
            elif x is Calculator.MUL:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Multiply(op1, op2)
                self.expression_queue.put(ex)
            elif x is Calculator.DIV:
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Divide(op1, op2)
                self.expression_queue.put(ex)
            else:
                raise ValueError

        ex = self.expression_queue.get()
        return ex.calc()

