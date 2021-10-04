from functools import cmp_to_key
def compare(item1, item2):
    if len(item1) < len(item2): return -1
    elif len(item1) > len(item2): return 1
    elif item1 < item2: return -1
    elif item1 > item2: return 1
    else: return 0

class Solution(object):
    def kthLargestNumber(self, nums, k):
        # nums2 = [int(s) for s in nums]
        # nums2.sort(reverse=True)
        # return str(nums2[k - 1])

        nums.sort(key=cmp_to_key(compare), reverse=True)
        return nums[k - 1]


print Solution().kthLargestNumber(nums = ["3","6","7","10"], k = 4)
print Solution().kthLargestNumber(nums = ["2","21","12","1"], k = 3)
print Solution().kthLargestNumber(nums = ["0","0"], k = 2)
