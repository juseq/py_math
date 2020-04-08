#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:09:28 2020

@author: juse

imprimeix la sèrie x + ... + (x**n)/n
"""

from sympy import Symbol, pprint, init_printing

def print_series(n):
    init_printing(order='rev-lex')
    
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    
    pprint(series)
    
if __name__ == '__main__':
    n = input('entra el nombre de termes de la sèrie: ')
    print_series(int(n))