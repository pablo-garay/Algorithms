class Solution(object):
    def visit_node(self, i, assigned_color, current_color, adj):
        assigned_color[i] = current_color

        for j in adj[i]:
            if assigned_color[j] is None:
                if self.visit_node(j, assigned_color, 1 - current_color, adj) == False:
                    return False
            elif assigned_color[i] == assigned_color[j]:
                return False
        return True


    def possibleBipartition(self, N, dislikes):
        if not dislikes:  # graph has no edges
            return True

        assigned_color = [None for _ in xrange(N)]

        adj = {}
        for i in xrange(N):
            adj[i] = []
        for i, j in dislikes:
            adj[i - 1].append(j - 1)
            adj[j - 1].append(i - 1)  # undirected graph

        for root in xrange(N):
            init_color = 0
            if assigned_color[root] is None and self.visit_node(root, assigned_color, init_color, adj) == False:
                return False

        return True
