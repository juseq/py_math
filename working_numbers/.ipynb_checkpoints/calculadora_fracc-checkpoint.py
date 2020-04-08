'''
Fracction calculator
'''

from fractions import Fraction

def add(a, b):
    print('Result of Addition: {0}'.format(a+b))

def subtract(a, b):
    print('Result of Subtracction: {0}'.format(a-b))

def multiply(a, b):
    print('Result of Multiplication: {0}'.format(a*b))

def divide(a, b):
    print('Result of Division: {0}'.format(a/b))


if __name__ == '__main__':
    a = Fraction(input('Enter first fraction (a/b): '))
    b = Fraction(input('Enter second fraction (a/b): '))
    op = input('Operation to perform - 1: Add, 2: Subtract, 4: Divide, 3: Multiply: ')
    if op == '1':
        add(a,b)
    elif op == '2':
        subtract(a,b)
    elif op == '3':
        multiply(a,b)
    elif op == '4':
        divide(a,b)
    else:
        print('Entrar el nombre de operació correcte')
