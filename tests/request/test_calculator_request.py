from calculator.request.calculator_request import (
    CalculatorRequest,
    CalculatorCommand
)


def test_calculator_request_base():
    request = CalculatorRequest.create("1 2 +")
    assert bool(request) is True
    assert request.cmd == CalculatorCommand.CALCULATE_CMD


def test_calculator_request_quit():
    request = CalculatorRequest.create("quit")
    assert bool(request) is True
    assert request.cmd == CalculatorCommand.QUIT_CMD


def test_calculator_request_print():
    request = CalculatorRequest.create("p")
    assert bool(request) is True
    assert request.cmd == CalculatorCommand.PRINT_CMD


def test_calculator_request_quit_exception():
    request = CalculatorRequest.create("q 10 =")
    assert bool(request) is False
    assert request.has_errors() is True


def test_calculator_request_invalid_value():
    # 現状、実行時エラーとしている
    request = CalculatorRequest.create("1abcd 5 =")
    assert bool(request) is True