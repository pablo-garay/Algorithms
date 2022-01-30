class Solution(object):  # Runtime: 16 ms, faster than 88.08%
    def uniquePaths(self, m, n):  # Time: O(m x n) - optimal as need to traverse whole matrix in worst case. Space: O(m x n)
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0: return 0
        memo = [[None for c in xrange(n)] for r in xrange(m)]

        for r in reversed(xrange(m)):
            memo[r][n - 1] = 1

        for c in reversed(xrange(n)):
            memo[m - 1][c] = 1

        for r in reversed(xrange(m - 1)):
            for c in reversed(xrange(n - 1)):
                memo[r][c] = 0
                if r + 1 <= m:
                    memo[r][c] += memo[r + 1][c]
                if c + 1 <= n:
                    memo[r][c] += memo[r][c + 1]

        return memo[0][0] # array elem which contains the final answer


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
