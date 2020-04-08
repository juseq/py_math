'''
Solució a l'equació lineal tipus ax + b = c
'''

def equ_lineal(a, b, c):
    x = (c - b)/a
    print("x = {0}".format(x))

if __name__ == '__main__':
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')

    if a != '0':
        equ_lineal(int(a),int(b),int(c))
    else:
        print('Error ... entrar <a> diferent de zero.')
