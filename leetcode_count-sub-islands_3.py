from collections import defaultdict
class Solution(object):
    def countSubIslands(self, grid1, grid2):  # Time: O(m x n). Space: O(m x n)
        global parent; parent = {}
        self.rows, self.cols = (len(grid2), len(grid2[0]))
        self.tag = {}

        tag_num = 0
        for r in xrange(self.rows):  # O(m x n) : each elem in grid2 will be visited at most once
            for c in xrange(self.cols):
                if (r, c) not in self.tag and grid2[r][c] == 1:
                    tag_num += 1
                    self.tag[(r, c)] = tag_num
                    self.dfs(grid2, r, c, tag_num)

        islands = defaultdict(list)  # O(m x n)
        for key, val in self.tag.iteritems():
            islands[val].append(key)

        out = 0
        for island in islands.values():  # O(m x n)
            subIsland = True
            for (r, c) in island:
                if grid1[r][c] != 1:
                    subIsland = False
                    break
            if subIsland: out += 1
        return out

    def dfs(self, grid2, r, c, tag_num):
        for (r2, c2) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= r2 < self.rows and 0 <= c2 < self.cols and grid2[r2][c2] == 1 and (r2, c2) not in self.tag:
                self.tag[(r2, c2)] = tag_num
                self.dfs(grid2, r2, c2, tag_num)


print Solution().countSubIslands(
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
)
print Solution().countSubIslands(
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
)





