import queue

from calculator.exception.calculate_error import CalculatorError
from calculator.request.calculator_request import (
    CalculatorValidRequest,
    CalculatorCommand
)
from calculator.domain import (
    value,
    variable
)
from calculator.binary_operator import (
    arithmetic,
    assignment
)
from calculator.unary_operator import (
    inc_dec,
)

class Calculator:
    def __init__(self):
        self.expression_queue = queue.LifoQueue()
        self.symbol_table = {}

    def execute(self, request):
        if request.cmd == CalculatorCommand.PRINT_CMD:
            ex = self.expression_queue.get()
            return ex.calc()
        elif request.cmd == CalculatorCommand.QUIT_CMD:
            return None

        token_list = request.token_list
        for token in token_list:
            if token.isdigit():
                ex = value.Value(int(token))
                self.expression_queue.put(ex)
            elif token == '+':
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Add(op1, op2)
                self.expression_queue.put(ex)
            elif token == '-':
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Substract(op1, op2)
                self.expression_queue.put(ex)
            elif token == '*':
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Multiply(op1, op2)
                self.expression_queue.put(ex)
            elif token == '/':
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = arithmetic.Divide(op1, op2)
                self.expression_queue.put(ex)
            elif token == '=':
                op2 = self.expression_queue.get()
                op1 = self.expression_queue.get()
                ex = assignment.SimpleAssign(op1, op2)
                self.expression_queue.put(ex)
            elif token == '++':
                op1 = self.expression_queue.get()
                ex = inc_dec.Increment(op1)
                self.expression_queue.put(ex)
            elif token == '--':
                op1 = self.expression_queue.get()
                ex = inc_dec.Decrement(op1)
                self.expression_queue.put(ex)
            elif token.isalpha():
                ex = variable.Variable(token, self.symbol_table)
                self.expression_queue.put(ex)
            else:
                raise CalculatorError('不正な値です: {}'.format(token))

        ex = self.expression_queue.get()
        return ex.calc()

