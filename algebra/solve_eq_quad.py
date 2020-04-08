#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:14:46 2020

@author: juse

per resoldre eq. quadrades
"""

from sympy import Symbol, solve, sympify, pprint, init_printing
from sympy.core.sympify import SympifyError

def solve_equ(eq):
    init_printing(order='rev-lex')
    x = Symbol('x')
    
    x1, x2 = solve(eq, dict=True)
    #print(solve(eq, dict=True))
    print("Primera arrel {0}".format(x1[x]))
    print("Segona arrel {0}".format(x2[x]))


if __name__ == '__main__':
    expr = input("Entra una eq. quadrada: ")
    
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        solve_equ(expr)