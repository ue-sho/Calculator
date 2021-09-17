import sys

from calculator.request.calculator_request import CalculatorRequest
from calculator.calculator import Calculator
from calculator.exception.calculate_error import CalculatorError


def calculator_cli():
    calculator = Calculator()

    while(True):
        print('input expression> ', end='')
        s = input()

        request = CalculatorRequest.create(s)
        if not request:
            for error in request.errors:
                value, message = error.values()
                print('{} : {}'.format(message, value))
            continue
        try:
            res = calculator.execute(request)
            if res is None:
                print('終了します')
                return
            print('>>> ', res)
        except CalculatorError as ex:
            print(ex, file=sys.stderr)
        print()

if __name__ == '__main__':
    calculator_cli()

