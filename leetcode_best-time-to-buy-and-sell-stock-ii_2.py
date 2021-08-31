class Solution(object):  # Time complexity: Linear (one pass). Optimal as need to traverse each array elem in worst case
    def maxProfit(self, prices):
        profit = 0

        for i in xrange(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit


print Solution().maxProfit(prices = [7,1,5,3,6,4])
print Solution().maxProfit(prices = [1,2,3,4,5])
print Solution().maxProfit(prices = [7,6,4,3,1])
print Solution().maxProfit(prices = [1])
print Solution().maxProfit(prices = [1, 2])
print Solution().maxProfit(prices = [2, 1])
print Solution().maxProfit(prices = [0, 2])

