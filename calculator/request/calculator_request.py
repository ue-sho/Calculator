from typing import List

from abc import ABCMeta, abstractmethod


class CalculatorCommand:
    QUIT_CMD = 'quit'
    PRINT_CMD = 'print'
    CALCULATE_CMD = 'calc'

class CalculatorInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, value, message):
        self.errors.append({"value": value, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class CalculatorValidRequest:
    def __init__(self, cmd, token_list: [str] = None):
        self.cmd = cmd
        self.token_list = token_list

    def __bool__(self):
        return True


class CalculatorRequest:
    QUIT_CMD_LIST = ['quit', 'q', 'exit']
    PRINT_CMD_LIST = ['print', 'p']

    @classmethod
    def create(cls, input_data: str):
        invalid_req = CalculatorInvalidRequest()

        expression_list = input_data.split()
        for ex in expression_list:
            if ex in cls.QUIT_CMD_LIST:
                if len(expression_list) == 1:
                    return CalculatorValidRequest(CalculatorCommand.QUIT_CMD)
                else:
                    invalid_req.add_error(ex, '予約語が含まれています')
            elif ex in cls.PRINT_CMD_LIST:
                if len(expression_list) == 1:
                    return CalculatorValidRequest(CalculatorCommand.PRINT_CMD)
                else:
                    invalid_req.add_error(ex, '予約語が含まれています')

        if invalid_req.has_errors():
            return invalid_req

        return CalculatorValidRequest(CalculatorCommand.CALCULATE_CMD, expression_list)
