from collections import Counter

class Solution(object):  # O(m + n) as each edge and node in graph is visited at most twice
    def findOrder(self, numCourses, prerequisites):
        incoming = {0: set()}
        edges_to = Counter()
        adj = [set() for _ in xrange(numCourses)]
        topolog_order = []
        removed_courses = 0

        for (dest, orig) in prerequisites:
            adj[orig].add(dest)
            edges_to[dest] += 1
            incoming[edges_to[dest]] = set()

        for dest in xrange(numCourses):
            incoming[edges_to[dest]].add(dest)

        while incoming[0]:
            orig = incoming[0].pop()
            topolog_order.append(orig)
            removed_courses += 1

            for dest in adj[orig]:
                prev, curr = (edges_to[dest], edges_to[dest] - 1)
                incoming[prev].remove(dest)
                edges_to[dest] -= 1
                incoming[curr].add(dest)

        if removed_courses == numCourses:
            return topolog_order
        else:
            return []


print Solution().findOrder(2, [[1, 0]])
print Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
print Solution().findOrder(4, [[1, 0], [0, 1], [2, 0], [3, 1], [3, 2]])
print Solution().findOrder(4, [])
print Solution().findOrder(0, [])
print Solution().findOrder(1, [])
print Solution().findOrder(3, [(0, 1)])

print Solution().findOrder(8, [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]])
print Solution().findOrder(3, [[0, 1], [2, 0]])
print Solution().findOrder(3, [[2, 0], [0, 1]])
print Solution().findOrder(3, [[2, 0], [1, 0]])

print Solution().findOrder(4, [[0, 1], [0, 2], [0, 3]])
