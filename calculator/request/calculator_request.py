from typing import List

from abc import ABCMeta, abstractmethod


class CalculatorInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class CalculatorValidRequest:


    def __init__(self, cmd, token_list: [Token] = None):
        self.cmd = cmd
        self.token_list = token_list

    def __bool__(self):
        return True


class CalculatorRequest:
    QUIT_CMD = ['quit', 'q', 'exit']
    PRINT_CMD = ['print', 'p']

    @classmethod
    def create(cls, input_data: str):
        invalid_req = CalculatorInvalidRequest()

        expression_list = input_data.split()
        for ex in expression_list:
            if ex in cls.QUIT_CMD:
                if len(input_data) == 1:
                    return CalculatorValidRequest('quit')
                else:
                    invalid_req.add_error(ex, '予約語が含まれています')
            elif ex in cls.PRINT_CMD:
                if len(input_data) == 1:
                    return CalculatorValidRequest('print')
                else:
                    invalid_req.add_error(ex, '予約語が含まれています')
            elif int(ex) < 0:
                invalid_req.add_error(ex, '負の値は入力できません')

        if invalid_req.has_errors():
            return invalid_req

        return CalculatorValidRequest('calc', expression_list)
