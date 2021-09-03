import queue
from calculator.domain.add import Add

class Calculator:
    BINARY_OP = ['+', '-', '*', '/']

    def process(self, s: str):
        q = queue.LifoQueue()

        for x in s.split():
            if x in self.BINARY_OP:
                # ex = Add()
                pass