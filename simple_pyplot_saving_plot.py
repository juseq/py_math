'''
Simple plot using pyplot
'''
import matplotlib.pyplot as plt

def create_graph():
    x_numbers = [1, 2, 3]
    y_numbers = [2, 5, 6]

    plt.plot(x_numbers, y_numbers)
    plt.savefig('simple_plt.pdf')
    plt.show()

if __name__ == '__main__':
    create_graph()