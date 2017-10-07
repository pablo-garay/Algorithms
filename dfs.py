import graph

vertices = [0, 1, 2, 3, 4, 5]
edges = ((5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1))
adj = graph.createGraph(vertices, edges)
print "Graph:", adj


parent = {}

def dfs(u, adj):
    for v in adj[u]:
        if v not in parent:
            parent[v] = u
            dfs(v, adj)

def complete_dfs(vertices, adj):
    parent = {}

    for s in vertices:
        if s not in parent:
            parent[s] = None
            dfs(s, adj)

    return parent


# try algorithm
dfs(5, adj)
print "DFS result (parent dictionary): ", parent
