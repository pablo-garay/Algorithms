# FIBONACCI O(1)
class Solution(object):
    def climbStairs(self, n):
        memo = [None for i in xrange(n + 1)]  # adding an extra element to array for convenience
        memo[n] = 1  # for convenience i.e. this makes computations right
        memo[n - 1] = 1

        for i in reversed(xrange(n - 1)):
            memo[i] = memo[i + 1] + memo[i + 2]
        return memo[0]

print Solution().climbStairs(2)
print Solution().climbStairs(3)
print Solution().climbStairs(4)
print Solution().climbStairs(5)
print Solution().climbStairs(6)
print Solution().climbStairs(7)
print Solution().climbStairs(8)
