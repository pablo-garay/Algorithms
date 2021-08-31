from collections import Counter

class Solution(object):  # Complexity | Time: O(1) - one pass. Optimal as need to check each elem once. Space: O(2*numsX.length)
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        out = 0
        half2 = Counter()

        for n1 in nums3:
            for n2 in nums4:
                half2[-(n1 + n2)] += 1

        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in half2:
                    out += half2[n1 + n2]

        return out


print Solution().fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
print Solution().fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0])

print Solution().fourSumCount([-1,1,1,1,-1], [0,-1,-1,0,1], [-1,-1,1,-1,-1], [0,1,0,-1,-1])

