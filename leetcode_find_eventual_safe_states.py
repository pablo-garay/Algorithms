class Solution(object):
    def eventualSafeNodes(self, graph):  # O(m + n) as each edge and node in graph times visit is in linear order
        outgoing = [0 for _ in xrange(len(graph))]
        to = [[] for dest in xrange(len(graph))]
        safe_state = set()
        output = []
        output_set = set()

        for orig in xrange(len(graph)):
            outgoing[orig] = len(graph[orig])
            if outgoing[orig] == 0:
                safe_state.add(orig)

            for dest in graph[orig]:
                to[dest].append(orig)

        while safe_state:
            dest = safe_state.pop()
            output_set.add(dest)

            for orig in to[dest]:
                outgoing[orig] -= 1

                if outgoing[orig] == 0:
                    safe_state.add(orig)

        for node in xrange(len(graph)):  # O(n) as opposed to sorting - which would take O(n log n)
            if node in output_set:
                output.append(node)

        return output


print Solution().eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []])
print Solution().eventualSafeNodes(graph=[])
print Solution().eventualSafeNodes(graph=[[]])
print Solution().eventualSafeNodes(graph=[[], [], []])
print Solution().eventualSafeNodes(graph=[[], [2], [1]])
print Solution().eventualSafeNodes(graph=[[], [0]])

print Solution().eventualSafeNodes(graph=[[], [0, 2, 3, 4], [3], [4], []])
