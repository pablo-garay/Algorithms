class Solution(object):  # Time: O(n log n) - runtime beats 88.70 %
    def nextPermutation(self, nums):
        if len(nums) <= 1: return

        right = len(nums) - 2
        swap = False

        while right >= 0:
            if nums[right] < nums[right + 1]:
                mini, ind = (nums[right + 1], right + 1)

                for i in xrange(right + 2, len(nums)):
                    if nums[right] < nums[i] < mini:
                        mini, ind = (nums[i], i)
                swap = True
                break
            right -= 1

        if not swap:
            nums.sort()
        else:
            nums[right], nums[ind] = (nums[ind], nums[right])
            nums[right + 1:] = sorted(nums[right + 1:])


Solution().nextPermutation(nums = [1,2,3])
Solution().nextPermutation(nums = [3,2,1])
Solution().nextPermutation(nums = [1,1,5])
Solution().nextPermutation(nums = [1,100,1])
Solution().nextPermutation(nums = [87,9,9,2])
Solution().nextPermutation(nums = [8,7,9,9,2])
Solution().nextPermutation(nums = [1,3,2])
