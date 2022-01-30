class Solution(object):  # Runtime: 16 ms, faster than 88.08%
    def uniquePaths(self, m, n):  # Time: O(m x n) - optimal as need to traverse whole matrix in worst case. Space: O(m x n)
        if m == 0 or n == 0: return 0
        memo = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for c in xrange(n):
            memo[0][c] = 1
        for r in xrange(m):
            memo[r][0] = 1

        for r in xrange(1, m):
            for c in xrange(1, n):
                memo[r][c] = memo[r][c - 1] + memo[r - 1][c]

        return memo[m - 1][n - 1]


print Solution().uniquePaths(3, 2)
print Solution().uniquePaths(7, 3)
print Solution().uniquePaths(0, 0)
print Solution().uniquePaths(0, 1)
print Solution().uniquePaths(5, 0)
print Solution().uniquePaths(1, 1)
print Solution().uniquePaths(1, 10)
print Solution().uniquePaths(10, 1)
print Solution().uniquePaths(10, 2)
print Solution().uniquePaths(10, 10)
