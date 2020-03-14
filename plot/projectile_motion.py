"""
trajectoria d'un projectil donades una velocitat inicial i un angle de
llançament
"""

import matplotlib.pyplot as plt
import math

g = 9.8

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

 # per tenir una llista de decimals en intervals regulars   
def float_range(start, final, interval):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    
    return numbers

# calculem la trajectòria i l'enviem per dibuixarla
def draw_trajectory(u, theta):
    theta = math.radians(theta)

    # temps de vol
    t_flight = 2*u*math.sin(theta)/g
    # intervala
    intervals = float_range(0, t_flight, 0.001)
    # llista de coordenades
    x = []; y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    # màxima alçada per la gràfica
    max_alt = max(y)

    # envien les dades a dibuixar
    draw_graph(x,y)
    # per no veure-ho deformat ymax
    # plt.gca().set_aspect('equal', adjustable='datalim')
    plt.gca().set_aspect('equal', adjustable='box')
    # grid
    plt.grid(b=True, which='major', axis='both')
    plt.show()

if __name__  == '__main__':
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))

    draw_trajectory(u, theta)