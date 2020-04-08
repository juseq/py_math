#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:51:13 2020

@author: juse

producte de dues expressions
"""

from sympy import expand, sympify
from sympy.core.sympify import SympifyError

def product(ex1, ex2):
    producte = expand(ex1*2*x +4ex2)
    print(producte)
    
if __name__ == '__main__':
    ex1 = input("Entra la primera expressió: ")
    ex2 = input("Entra la segona expressió: ")
    
    try:
        ex1 = sympify(ex1)
        ex2 = sympify(ex2)
    except SympifyError:
        print('Invalid input')
    else:
        product(ex1, ex2)