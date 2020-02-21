from collections import defaultdict

class Solution(object):
    def eventualSafeNodes(self, graph):
        outgoing = defaultdict(set)
        to = [[] for dest in xrange(len(graph))]
        dest_list = defaultdict(set)
        output = []

        for orig in xrange(len(graph)):
            dest_list[orig] = set(graph[orig])
            outgoing[len(dest_list[orig])].add(orig)

            for dest in dest_list[orig]:
                to[dest].append(orig)

        while outgoing[0]:
            dest = outgoing[0].pop()
            output.append(dest)

            for orig in to[dest]:
                prev, curr = (len(dest_list[orig]), len(dest_list[orig]) - 1)
                outgoing[prev].remove(orig)
                dest_list[orig].remove(dest)
                outgoing[curr].add(orig)

        return sorted(output)


print Solution().eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []])
print Solution().eventualSafeNodes(graph=[])
print Solution().eventualSafeNodes(graph=[[]])
print Solution().eventualSafeNodes(graph=[[], [], []])
print Solution().eventualSafeNodes(graph=[[], [2], [1]])
print Solution().eventualSafeNodes(graph=[[], [0]])

print Solution().eventualSafeNodes(graph=[[], [0, 2, 3, 4], [3], [4], []])
