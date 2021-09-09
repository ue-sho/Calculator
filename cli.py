from calculator.calculator import Calculator

END_CMD = ['q', 'quit', 'exit']

if __name__ == '__main__':
    calc = Calculator()

    while(True):
        print('input expression> ', end='')
        s = input()

        if s in END_CMD:
            exit

        # TODO: インプットが正しいかのチェックを別クラスにする
        print(calc.process(s.split()))

