class Solution(object):  # Time complexity: Linear (one pass). Optimal as need to traverse each array elem in worst case
    def maxProfit(self, prices):
        opt = [[0 for _ in [True, False]] for i in xrange(len(prices) + 1)]

        for i in reversed(xrange(len(prices))):
            opt[i][1] = max(prices[i] + opt[i + 1][0], opt[i + 1][1])
            opt[i][0] = max(-prices[i] + opt[i + 1][1], opt[i + 1][0])

        return opt[0][0]  # second index 0 means not holding stock/ownership, 1 means holding/ownership


print Solution().maxProfit(prices = [7,1,5,3,6,4])
print Solution().maxProfit(prices = [1,2,3,4,5])
print Solution().maxProfit(prices = [7,6,4,3,1])
print Solution().maxProfit(prices = [1])
print Solution().maxProfit(prices = [1, 2])
print Solution().maxProfit(prices = [2, 1])
print Solution().maxProfit(prices = [0, 2])

