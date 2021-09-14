import pytest

from calculator.request.calculator_request import CalculatorRequest
from calculator.calculator import Calculator
from calculator.exception.calculate_error import CalculatorError


def test_calculator_add():
    calculator = Calculator()

    request = CalculatorRequest.create("1 2 +")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 3


def test_calculator_div_zero():
    calculator = Calculator()

    request = CalculatorRequest.create("1 0 /")
    assert bool(request) is True

    with pytest.raises(CalculatorError):
        res = calculator.execute(request)


def test_calculator_variable():
    calculator = Calculator()

    request = CalculatorRequest.create("x 10 =")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 10

def test_calculator_increment():
    calculator = Calculator()

    request = CalculatorRequest.create("10 ++")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 11

def test_calculator_decrement():
    calculator = Calculator()

    request = CalculatorRequest.create("3 --")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 2


@pytest.fixture
def assignment_x_calculator():
    calculator = Calculator()

    request = CalculatorRequest.create("x 10 =")
    res = calculator.execute(request)
    return calculator


def test_calculator_add_assign(assignment_x_calculator):
    request = CalculatorRequest.create("x 10 +=")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 20


def test_calculator_sub_assign(assignment_x_calculator):
    request = CalculatorRequest.create("x 1 -= ")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 9


def test_calculator_mul_assign(assignment_x_calculator):
    request = CalculatorRequest.create("x 0 *=")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 0


def test_calculator_div_assign(assignment_x_calculator):
    request = CalculatorRequest.create("x 5 /=")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 2

