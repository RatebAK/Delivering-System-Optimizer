class Graph:
    def __init__(self):
        self.point = [None] * V
def create_graph(edges, x):
    graph = Graph()
    for i in range(V):
        graph.point[i] = None
    for i in range(x):
        start = edges[i].start
        end = edges[i].end
        v = Vertex(end)
        v.next = graph.point[start]
        graph.point[start] = v
    return graph
