class Solution(object):  # Runtime 80 ms Beats 100%
    def canJump(self, nums):  # Time: O(n) for n elems in nums. Optimal as need to traverse whole array in worst case. Space: O(1)
        reach = [0] * len(nums)
        reach[-1] = 1
        times_reached = 0

        for i in reversed(xrange(len(nums) - 1)):
            if times_reached <= 0 and i + nums[i] < len(nums) - 1:
                continue

            for index in xrange(i + 1, i + 1 + nums[i]):
                if reach[index] == 1:
                    reach[i] = 1
                    times_reached += 1
                    break

        return reach[0]
