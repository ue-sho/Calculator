import queue
from calculator.domain.arithmetic import Add
from calculator.domain.value import Value

class Calculator:
    BINARY_OP = ['+', '-', '*', '/']

    def process(self, s: str):
        q = queue.LifoQueue()

        for x in s.split():
            if x in self.BINARY_OP:
                op2 = q.get()
                op1 = q.get()
                ex = Add(op1, op2)
                q.put(ex)
            else:
                ex = Value(int(x))
                q.put(ex)

        ex = q.get()
        return ex.calc()

