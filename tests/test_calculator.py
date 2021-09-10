import pytest

from calculator.calculator import Calculator


def test_calculator_add():
    calc = Calculator()
    assert calc.process("1 2 +".split()) == 3


def test_calculator_variable():
    calc = Calculator()
    assert calc.process("x 10 =".split()) == 10


def test_calculator_div_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.process("1 0 /".split()) == 10
