import csv
import matplotlib.pyplot as plt

MESOS = ('gener','febrer','març','abril','maig','juny','juliol','agost','setembre','octubre','novembre','desembre')
anys = []

def draw_graph(x, y):

  plt.plot(x, y)
  plt.title("PRECIPITACIÓ MENSUAL (mm)")
  plt.xlabel('mesos')
  plt.ylabel("mm")
  plt.legend(anys)


def draw_pluja(pluja_any):
    # list of x and y co-ordinates
    x = range(1, 13)
    #create the graph
    draw_graph(x, pluja_any)


def read_csv(filename):

  with open(filename, mode='r', encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
      pluja_any=[]
      anys.append(row['any'])
      
      for mes in MESOS:
        pluja_any.append(row[mes])

      draw_pluja(pluja_any)


if __name__ == '__main__':
  dades = read_csv('pluja_amposta.csv')
  plt.show()