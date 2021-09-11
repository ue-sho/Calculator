from calculator.calculator import Calculator

END_CMD = ['q', 'quit', 'exit']

def calculator_cli():
    calc = Calculator()

    while(True):
        print('input expression> ', end='')
        s = input()

        if s in END_CMD:
            return

        # TODO: インプットが正しいかのチェックを別クラスにする
        print(calc.process(s.split()))

if __name__ == '__main__':
    calculator_cli()

