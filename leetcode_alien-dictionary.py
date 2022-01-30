from collections import defaultdict
TEMP_MARk, PERM_MARK = (1, 2)

class Solution:  # Time : O(n) where n is the sum of lengths of all the words - optimal as need to check each char in worst case
    def alienOrder(self, words):  # Space: O(|v| + |e|) # |v| <= 27, |e| = len(words)
        self.adj = defaultdict(list); nodes = set()

        for i in xrange(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            length = min(len(w1), len(w2))

            if len(w2) < len(w1) and w2 == w1[:length]:
                return ""

            for c in w1: nodes.add(c)
            for c in w2: nodes.add(c)

            for j in xrange(length):
                if w1[j] != w2[j]:
                    self.adj[w1[j]] = w2[j]
                    break

        self.res = ""; self.visited = {}; self.cycle = False

        for node in sorted(nodes, reverse=True):
            if node not in self.visited:
                self.dfs(node)

        if self.cycle: return ""
        return self.res[::-1]

    def dfs(self, node):
        if node in self.visited:
            if self.visited[node] == TEMP_MARk:
                self.cycle = True
            return

        self.visited[node] = TEMP_MARk

        for neigh in self.adj[node]:
            self.dfs(neigh)

        self.res += node
        self.visited[node] = PERM_MARK


print Solution().alienOrder(["wrt","wrf","er","ett","rftt"])
print Solution().alienOrder(["wwa", "wwb"])
print Solution().alienOrder(["wwac", "wwbc"])
print Solution().alienOrder(["abc","ab"])
