'''
plot funcio quadrada
'''

from pylab import plot, show

y_s = []

def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval

    return numbers

def calcula_ys(a,b,c, x_s):
    for x in x_s:
        y = a*(x**2) + b*x + c
        y_s.append(y)

if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')

    x_s = frange(-3, 3, 0.1)

    calcula_ys(a,b,c, x_s)
    plot(x_s, y_s)
    show()