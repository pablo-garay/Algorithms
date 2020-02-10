class Solution(object):  # O(len(cost)). Optimal as we need to traverse all elements of cost in the worst case
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        cost += [0, 0]

        for i in reversed(xrange(length)):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])



print Solution().minCostClimbingStairs([10, 15, 20])
print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print Solution().minCostClimbingStairs([1, 1])
print Solution().minCostClimbingStairs([2, 1])
print Solution().minCostClimbingStairs([2, 1, 2, 1])
print Solution().minCostClimbingStairs([2, 1, 2, 1, 0, 0])
print Solution().minCostClimbingStairs([3, 6, 3, 1, 2, 1000])
