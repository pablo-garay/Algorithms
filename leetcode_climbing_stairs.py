# FIBONACCI O(n)
class Solution(object):
    def climbStairs(self, n):
        memo = [None for i in xrange(n + 1)]  # adding an extra element to array for convenience
        memo[0] = memo[1] = 1  # for convenience i.e. this makes computations right

        for i in xrange(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]


print Solution().climbStairs(2)
print Solution().climbStairs(3)
print Solution().climbStairs(4)
print Solution().climbStairs(5)
print Solution().climbStairs(6)
print Solution().climbStairs(7)
print Solution().climbStairs(8)
