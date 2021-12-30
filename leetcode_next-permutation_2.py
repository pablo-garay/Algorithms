class Solution(object):  # Time: O(n)
    def nextPermutation(self, nums):
        right = end = len(nums) - 1
        while right > 0 and not nums[right - 1] < nums[right]:
            right -= 1
        if right == 0:  # nums are in descending order
            nums.reverse()
            return
        ind = right - 1  # find the last "ascending" position

        while nums[ind] >= nums[end]:
            end -= 1
        nums[ind], nums[end] = nums[end], nums[ind]
        l, r = ind + 1, len(nums) - 1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1


Solution().nextPermutation(nums = [1,2,3])
Solution().nextPermutation(nums = [3,2,1])
Solution().nextPermutation(nums = [1,1,5])
Solution().nextPermutation(nums = [1,100,1])
Solution().nextPermutation(nums = [87,9,9,2])
Solution().nextPermutation(nums = [8,7,9,9,2])
Solution().nextPermutation(nums = [1,3,2])
