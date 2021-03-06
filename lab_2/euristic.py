
from matplotlib import pyplot as plt
import math

from headers.graph import Graph
from headers.vertex import Vertex
from headers.draw import draw_graph


def distance(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)


def draw_graph_euristic(begin, end):
    graph = Graph()
    draw_graph(graph)
    ax = plt.axes()
    print("start drawing euristic algorithm ...")
    current = begin
    while str(current) != str(end):
        next = current
        min_distance = math.inf
        for ady in graph.ady(current):
            if distance(ady, end) < min_distance:
                next = ady
                min_distance = distance(ady, end)

        x_values = [current.x, next.x]
        y_values = [current.y, next.y]
        plt.plot(x_values, y_values, color='red')

        ax.arrow(current.x, current.y,
                 next.x - current.x, next.y - current.y,
                 head_width=0.2, head_length=0.4, fc='k', ec='k')
        current = next

    print("end drawing euristic ...")
    plt.show()

print('Ingrese la coordenada x del primer punto')
p1_x = int(input())
print('Ingrese la coordenada y del primer punto')
p1_y = int(input())
print('Ingrese la coordenada x del segundo punto')
p2_x = int(input())
print('Ingrese la coordenada y del segundo punto')
p2_y = int(input())

vertexbegin = Vertex(p1_x, p1_y)
vertexend = Vertex(p2_x, p2_y)
draw_graph_euristic(vertexbegin, vertexend)


