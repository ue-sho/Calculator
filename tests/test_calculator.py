import pytest

from calculator.request.calculator_request import CalculatorRequest
from calculator.calculator import Calculator
from calculator.exception.calculate_error import CalculatorError

@pytest.fixture
def calculator():
    return Calculator()


@pytest.fixture
def assignment_x_calculator(calculator):
    calculator = Calculator()

    request = CalculatorRequest.create("x 10 =")
    res = calculator.execute(request)
    return calculator


def test_calculator_add(calculator):
    request = CalculatorRequest.create("1 2 +")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 3


def test_calculator_div_zero(calculator):
    request = CalculatorRequest.create("1 0 /")
    assert bool(request) is True

    with pytest.raises(CalculatorError):
        res = calculator.execute(request)


def test_calculator_variable(calculator):
    request = CalculatorRequest.create("x 10 =")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 10


def test_calculator_increment(assignment_x_calculator):
    request = CalculatorRequest.create("x ++")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 11


def test_calculator_decrement(assignment_x_calculator):
    request = CalculatorRequest.create("x --")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 9


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


def test_calculator_modulo(calculator):
    request = CalculatorRequest.create("13 5 %")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 3


def test_calculator_right_shift(calculator):
    request = CalculatorRequest.create("32 2 >>")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 8


def test_calculator_left_shift(calculator):
    request = CalculatorRequest.create("2 5 <<")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 64


def test_calculator_and(calculator):
    request = CalculatorRequest.create("1399 432 &")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 304


def test_calculator_or(calculator):
    request = CalculatorRequest.create("23 133 |")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 151


def test_calculator_xor(calculator):
    request = CalculatorRequest.create("234 434 ^")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 344


def test_calculator_equal(calculator):
    request = CalculatorRequest.create("5 5 ==")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 1


def test_calculator_not_equal(calculator):
    request = CalculatorRequest.create("1 0 !=")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 1


def test_calculator_less(calculator):
    request = CalculatorRequest.create("234 434 <")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 1


def test_calculator_less_equal(calculator):
    request = CalculatorRequest.create("432 432 <=")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 1


def test_calculator_greater(calculator):
    request = CalculatorRequest.create("23 133 >")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 0


def test_calculator_greater_equal(calculator):
    request = CalculatorRequest.create("234 234 >=")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 1


def test_calculator_right_shift_assign(assignment_x_calculator):
    request = CalculatorRequest.create("x 1 >>=")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 5


def test_calculator_left_shift_assign(assignment_x_calculator):
    request = CalculatorRequest.create("x 3 <<=")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 80

def test_calculator_modulo_assign(assignment_x_calculator):
    request = CalculatorRequest.create("x 4 %=")
    assert bool(request) is True

    res = assignment_x_calculator.execute(request)
    assert res == 2

def test_calculator_both(calculator):
    request = CalculatorRequest.create("432 0 &&")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 0


def test_calculator_greater(calculator):
    request = CalculatorRequest.create("23 0 ||")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 1


def test_calculator_greater_equal(calculator):
    request = CalculatorRequest.create("234 !")
    assert bool(request) is True

    res = calculator.execute(request)
    assert res == 0
