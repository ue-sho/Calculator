from calculator.calculator import Calculator


def test_calculator_add():
    calc = Calculator()
    assert calc.process("1 2 +") == 3
