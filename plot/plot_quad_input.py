'''
dibuixa funcions quadrades entrades per teclat
'''

import matplotlib.pyplot as plt

def float_range(start, final, interval):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    
    return numbers

def draw_function(a, b, c, min, max):
    intervals = float_range(min, max, 0.001)
    xs = []; ys = []
    for x in intervals:
        xs.append(x)
        ys.append(a*x*x + b*x + c)

    draw_graph(xs, ys, a, b, c)

def make_legend(a, b, c):
    legend = ""
    # a
    if a < 0:
        legend += "-{0:.0f}x^2 "
    elif a > 0:
        legend += "{0:.0f}x^2 "
    if a == 1: legend = "x^2 "
    if a == -1: legend = "-x^2 "
    # b
    if b < 0:
        legend += "- {1:.0f}x "
    elif b > 0:
        legend += "+ {1:.0f}x "
    # c
    if c < 0:
        legend += "- {2:.0f} "
    elif c > 0:
        legend += "+ {2:.0f} "
    legend = legend.format(abs(a), abs(b), abs(c))

    return legend

def draw_graph(x, y, a, b, c):
    plt.plot(x, y)
    plt.grid()
    
    plt.legend([make_legend(a, b, c)])
    plt.show()

if __name__ == '__main__':
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    # min, max = input("Entra l'interval per la gràfica (separatsper un espai): ").split()
    min, max = '-10', '10'
    draw_function(a, b, c, float(min), float(max))