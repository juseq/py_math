#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:07:12 2020

@author: juse

per resoldre eqs. lineals entrades per teclat: 'x - 5 -7'
x = 12

"""

from sympy import Symbol, solve, sympify
from sympy.core.sympify import SympifyError

x = Symbol('x')

expr = input("Entra una expressió: ")

try:
    expr = sympify(expr)
except SympifyError:
    print('Invalid input')
else:
    print(solve(expr))
