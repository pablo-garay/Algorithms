from collections import Counter, defaultdict


class Solution(object):
    def loudAndRich(self, richer, quiet):
        count = [0 for _ in xrange(len(quiet))]
        self.adj = defaultdict(set)
        self.res = [None for _ in  xrange(len(quiet))]
        self.visited = [False for _ in  xrange(len(quiet))]

        for (v, u) in richer:
            self.adj[u].add(v)
            count[v] += 1

        for node in xrange(len(quiet)):
            if count[node] == 0:
                self.dfs(node, quiet)

        return self.res

    def dfs(self, node, quiet):
        if self.visited[node]:
            return self.res[node], quiet[self.res[node]]
        self.visited[node] = True

        greater = [node]
        levels = [quiet[node]]

        for v in self.adj[node]:
            partial_greater, partial_level = self.dfs(v, quiet)

            greater.append(partial_greater)
            levels.append(partial_level)

        min_val = min(levels)
        min_index = levels.index(min_val)
        self.res[node] = greater[min_index]

        # print "For node: " + str(node) + " consider nodes: " + str(greater) + " with quiet levels: " + str(levels)
        # print "Min is: " + str(min_val) + " which corresponds to node: " + str(greater[min_index])
        # print

        return greater[min_index], min_val


print Solution().loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0])
# print Solution().loudAndRich(richer = [], quiet = [0])