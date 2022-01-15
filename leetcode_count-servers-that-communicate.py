class Solution(object):  # Runtime: 412 ms, faster than 83.33%
    def countServers(self, grid):  # Time: O(mxn) - optimal as need to traverse whole matrix in worse case. Space: O(mxn)
        m, n = len(grid), len(grid[0])
        res_set = set()

        for r in xrange(m):  # O(mxn)
            partial_set = set()
            for c in xrange(n):
                if grid[r][c] == 1:
                    partial_set.add((r, c))
            if len(partial_set) > 1:
                res_set.update(partial_set)

        for c in xrange(n):  # O(mxn)
            partial_set = set()
            for r in xrange(m):
                if grid[r][c] == 1:
                    partial_set.add((r, c))
            if len(partial_set) > 1:
                res_set.update(partial_set)

        return len(res_set)


print Solution().countServers(grid = [[1,0],[0,1]])
print Solution().countServers(grid = [[1,0],[1,1]])
print Solution().countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])
print Solution().countServers(grid = [[1]])
print Solution().countServers(grid = [[1,0]])
print Solution().countServers(grid = [[1,1]])
print Solution().countServers(grid = [[1],[0]])
print Solution().countServers(grid = [[1],[1]])
