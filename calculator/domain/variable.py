from typing import Dict

from calculator.domain.expression import Expression
from calculator.exception.calculate_error import CalculatorError

class Variable(Expression):
    def __init__(self, symbol: str, symbol_table: Dict):
        self.symbol = symbol
        self.symbol_table = symbol_table

    def set_value(self, num: int):
        self.symbol_table[self.symbol] = num

    def calc(self):
        val = self.symbol_table.get(self.symbol)
        if val is None:
            raise CalculatorError('symbol_tableに{}が見つかりませんでした'.format(val))
        return val