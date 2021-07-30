class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        group = {}
        adj = {}
        for i in xrange(len(graph)):
            adj[i] = []
            for j in graph[i]:
                adj[i].append(j)

        unvisited = {node for node in xrange(0, len(graph))}

        while unvisited:
            root = unvisited.pop()
            frontier = [root]
            group_tag = 0
            group[root] = group_tag

            while frontier:
                group_tag = 0 if group_tag == 1 else 1
                next_frontier = []
                for node in frontier:
                    if node in unvisited:
                        unvisited.remove(node)

                    for child in adj[node]:
                        if child not in group:
                            group[child] = group_tag
                            next_frontier.append(child)
                        elif group[child] == group[node]:
                            return False
                frontier = next_frontier

        return True


print Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]])
print Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])
print Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])
