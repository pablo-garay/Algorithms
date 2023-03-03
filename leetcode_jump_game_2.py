class Solution(object):  # Runtime 364 ms Beats 90%
    def canJump(self, nums):  # Time: O(n) for n elems in nums. Optimal as need to traverse whole array in worst case. Space: O(1)
        if len(nums) <= 1: return True
        i = reachable = 0

        while i < len(nums) and i <= reachable:
            if i + nums[i] > reachable: reachable = i + nums[i]
            if reachable >= len(nums) - 1: return True
            i += 1
        return False
