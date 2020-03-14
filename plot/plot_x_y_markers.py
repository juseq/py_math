from pylab import plot, show

x_numbers = [1, 2, 3]
y_numbers = [2, 3, 6]

# marcadors units per una línia
plot(x_numbers, y_numbers, marker='o')
show()

#només marcadors
plot(x_numbers, y_numbers, 'o')
show()