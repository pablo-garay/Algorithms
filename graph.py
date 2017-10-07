# function to add an edge to graph
def addEdge(graph, u,v):
    graph[u].append(v)


def createGraph(vertices, edges):
    graph = {}

    for v in vertices:
        graph[v] = []

    for (u, v) in edges:
        addEdge(graph, u, v)

    return graph