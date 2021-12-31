class Solution(object):  # Time: O(n) - optimal as need to traverse all elems in array in worst case. Space: O(1)
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        maxi, profit = (prices[-1], 0)

        for i in reversed(xrange(len(prices) - 1)):
            profit = max(profit, maxi - prices[i])
            maxi = max(maxi, prices[i])

        return profit

print Solution().maxProfit([7,1,5,3,6,4])
print Solution().maxProfit([7,6,4,3,1])
print Solution().maxProfit([1])
print Solution().maxProfit([1, 2])
print Solution().maxProfit([2, 1])
