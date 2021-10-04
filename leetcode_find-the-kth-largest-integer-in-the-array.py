class Solution(object):  # O(nlog n) runtime beats 97.11 %
    def kthLargestNumber(self, nums, k):
        nums2 = [int(s) for s in nums]
        nums2.sort(reverse=True)
        return str(nums2[k - 1])

print Solution().kthLargestNumber(nums = ["3","6","7","10"], k = 4)
print Solution().kthLargestNumber(nums = ["2","21","12","1"], k = 3)
print Solution().kthLargestNumber(nums = ["0","0"], k = 2)
