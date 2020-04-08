# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Plot d'una expressió entrada en termes d'x i d'y: x**2 -3*y -5
"""

from sympy import Symbol, solve, sympify, pprint, init_printing
from sympy.core.sympify import SympifyError
from sympy.plotting import plot

def plot_expression(expr):
    y = Symbol('y')
    x = Symbol('x')
    solutions  = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)
    
if __name__ == '__main__':
    expr = input("Entra una expressió en termes d'x i d'y: ")

    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        plot_expression(expr)