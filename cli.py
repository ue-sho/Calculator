from calculator.calculator import Calculator

if __name__ == '__main__':
    calc = Calculator()

    s = input()
    print('>>> ', calc.process(s))
