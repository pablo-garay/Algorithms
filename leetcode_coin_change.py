INFINITE = float("inf")


# Complexity: O(amount * #coins)
class Solution(object):
    def coinChange(self, coins, total_amount):
        """
        :type coins: List[int]
        :type total_amount: int
        :rtype: int
        """
        opt = [INFINITE for amount in xrange(total_amount + 1)]
        opt[0] = 0

        for amount in xrange(1, total_amount + 1):
            opt[amount] = INFINITE
            for coin in coins:
                num = 1 + self.computeOpt(amount - coin, opt)
                if num < opt[amount]:
                    opt[amount] = num

        if opt[total_amount] == INFINITE:
            return -1
        else:
            return opt[total_amount]

    def computeOpt(self, amount, opt):
        if amount < 0:
            return INFINITE
        else:
            return opt[amount]


print Solution().coinChange([1, 2, 5], 11)  # 3
print Solution().coinChange([2], 3)  # -1
print Solution().coinChange([1], 2)  # 2
print Solution().coinChange([186, 419, 83, 408], 6249)  # 20
