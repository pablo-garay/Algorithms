import graph

vertices = [0, 1, 2, 3, 4, 5]
edges = ((5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1))
adj = graph.createGraph(vertices, edges)
print adj


def bfs(s, adj):
    parent = {s: None}
    level = {s: 0}
    frontier = [s]
    curr_level = 1

    while frontier:
        next_frontier = []
        for u in frontier:
            for v in adj[u]:
                if v not in parent:
                    parent[v] = u
                    level[v] = curr_level
                    next_frontier.append(v)
        frontier = next_frontier
        curr_level += 1
    return parent, level


# try algorithm
parent, level = bfs(5, adj)
print "parent", parent, "level", level
