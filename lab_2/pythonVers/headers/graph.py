
from pythonVers.settings import base as settings
from pythonVers.headers.vertex import Vertex
from pythonVers.headers.vertex import VertexList
from pythonVers.headers.vertex import generate_rand_vertices


class Graph():
    ady_graph = {}
    vertices = []
    deleted_vertices = VertexList()

    def __init__(self):
        self.deleted_vertices = generate_rand_vertices()
        for x in range(settings.size_w):
            for y in range(settings.size_h):
                vertex = Vertex(x, y)
                if not (self.deleted_vertices.is_inside(vertex)):
                    ady_list = []
                    for ady_vertex in vertex.near_vertices():
                        if not (self.deleted_vertices.is_inside(ady_vertex)):
                            ady_list.append(ady_vertex)
                    self.vertices.append(vertex)
                    self.ady_graph[str(vertex)] = ady_list

    def is_inside(self, vertex):
        return not self.deleted_vertices.is_inside(vertex)

    def ady(self, vertex):
        return self.ady_graph[str(vertex)]
