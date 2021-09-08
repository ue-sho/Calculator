from calculator.calculator import Calculator

END_CMD = ['q', 'quit', 'exit']

if __name__ == '__main__':
    calc = Calculator()

    print('input expression> ', end='')
    s = input()

    # TODO: インプットが正しいかのチェックを別クラスにする
    print(calc.process(s.split()))
