class Solution(object):  # O(logn * n^2)
    # *A + B > C
    # *B + C > A (satisfied when sorted)
    # *A + C > B (satisfied when sorted)

    def bin_search(self, nums, searched):
        start, end = 0, len(nums) - 1

        while start < end:
            if searched < nums[(start + end) / 2]:
                end = (start + end) / 2 - 1

            elif searched >= nums[(start + end) / 2]:
                start = (start + end) / 2 + 1

        if start > 0 and nums[start] > searched:
            start -= 1

        return start


    def triangleNumber(self, nums):
        if len(nums) < 3:
            return 0

        nums.sort()  # O(nlogn)
        count = 0

        for i in xrange(len(nums) - 2):
            for j in xrange(i + 1, len(nums) - 1):
                search_for = nums[i] + nums[j] - 1
                index = self.bin_search(nums, search_for)
                count += max(0, index - j)

        return count


print Solution().triangleNumber([2,2,3,4])
print Solution().triangleNumber([48,66,61,46,94,75])
# print Solution().bin_search([1, 3, 5, 5, 7], 6)
# print Solution().bin_search([1, 3, 5, 5, 7], 5)
# print Solution().bin_search([1, 3, 5, 5, 7], 0)
# print Solution().bin_search([1, 3, 5, 5, 7], 9)
# print Solution().bin_search([1, 3, 5, 5, 7, 7], 9)
# print Solution().bin_search([1, 3, 5, 5, 5, 7, 7], 5)
# print Solution().bin_search([46, 48, 61, 66, 75, 94], 93)
# print Solution().bin_search([46, 48, 61, 66, 75, 94], 93)
