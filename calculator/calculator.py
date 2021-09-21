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
    assignment,
    bitwise_operator,
    relational_operator,
    logical_operator
)
from calculator.unary_operator import (
    inc_dec,
    logical_not
)

class Calculator:
    BINARY_OPERATOR_FUNCTION_TABLE = {
       "+": lambda op1, op2: arithmetic.Add(op1, op2),
       "-": lambda op1, op2: arithmetic.Substract(op1, op2),
       "*": lambda op1, op2: arithmetic.Multiply(op1, op2),
       "/": lambda op1, op2: arithmetic.Divide(op1, op2),
       "%": lambda op1, op2: arithmetic.Modulo(op1, op2),
       "=": lambda op1, op2: assignment.SimpleAssign(op1, op2),
       "+=": lambda op1, op2: assignment.AddAssign(op1, op2),
       "-=": lambda op1, op2: assignment.SubAssign(op1, op2),
       "*=": lambda op1, op2: assignment.MulAssign(op1, op2),
       "/=": lambda op1, op2: assignment.DivAssign(op1, op2),
       "<<=": lambda op1, op2: assignment.LeftShiftAssign(op1, op2),
       ">>=": lambda op1, op2: assignment.RightShiftAssign(op1, op2),
       "%=": lambda op1, op2: assignment.ModuloAssign(op1, op2),
       "&": lambda op1, op2: bitwise_operator.And(op1, op2),
       "|": lambda op1, op2: bitwise_operator.Or(op1, op2),
       "^": lambda op1, op2: bitwise_operator.Xor(op1, op2),
       ">>": lambda op1, op2: bitwise_operator.RightShift(op1, op2),
       "<<": lambda op1, op2: bitwise_operator.LeftShift(op1, op2),
       "&&": lambda op1, op2: logical_operator.Both(op1, op2),
       "||": lambda op1, op2: logical_operator.Either(op1, op2),
       "==": lambda op1, op2: relational_operator.Equal(op1, op2),
       "!=": lambda op1, op2: relational_operator.NotEqual(op1, op2),
       "<": lambda op1, op2: relational_operator.Less(op1, op2),
       "<=": lambda op1, op2: relational_operator.LessEqual(op1, op2),
       ">": lambda op1, op2: relational_operator.Greater(op1, op2),
       ">=": lambda op1, op2: relational_operator.GreaterEqual(op1, op2),
    }
    UNARY_OPERATOR_FUNCTION_TABLE = {
       "++": lambda op1: inc_dec.Increment(op1),
       "--": lambda op1: inc_dec.Decrement(op1),
       "!": lambda op1: logical_not.LogicalNot(op1),
    }


    def __init__(self):
        self.expression_stack = []
        self.symbol_table = {}

    def execute(self, request):
        try:
            if request.cmd == CalculatorCommand.PRINT_CMD:
                ex = self.expression_stack.pop()
                return ex.calc()
            elif request.cmd == CalculatorCommand.QUIT_CMD:
                return None

            token_list = request.token_list
            for token in token_list:
                if token.isdigit():
                    ex = value.Value(int(token))
                    self.expression_stack.append(ex)
                elif token.isalpha():
                    ex = variable.Variable(token, self.symbol_table)
                    self.expression_stack.append(ex)
                elif token in self.BINARY_OPERATOR_FUNCTION_TABLE.keys():
                    op2 = self.expression_stack.pop()
                    op1 = self.expression_stack.pop()
                    ex = self.BINARY_OPERATOR_FUNCTION_TABLE[token](op1, op2)
                    self.expression_stack.append(ex)
                elif token in self.UNARY_OPERATOR_FUNCTION_TABLE.keys():
                    op1 = self.expression_stack.pop()
                    ex = self.UNARY_OPERATOR_FUNCTION_TABLE[token](op1)
                    self.expression_stack.append(ex)
                else:
                    raise CalculatorError('不正な値です: {}'.format(token))

            ex = self.expression_stack.pop()
            return ex.calc()
        except IndexError:
            raise CalculatorError('演算子と値の数が合っていません')


