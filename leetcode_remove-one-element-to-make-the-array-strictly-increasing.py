class Solution(object):
    def canBeIncreasing(self, nums):  # Time: O(n) where n is length of array. Space: O(1)
        if len(nums) <= 2: return True
        count = 0

        prev2, prev, curr, next = (float("-inf"), nums[0], nums[1], nums[2])
        for i in xrange(1, len(nums)):
            if curr <= prev:
                count += 1

                if count > 1:
                    return False

                if not (next is None or (next is not None and next > prev) or curr > prev2):
                    return False

            prev2, prev, curr, next = (prev, curr, next, nums[i + 2] if i + 2 <= len(nums) - 1 else None)

        return True


print Solution().canBeIncreasing([2,3,1,2])
print Solution().canBeIncreasing([1,1,1])
print Solution().canBeIncreasing([512,867,904,997,403])