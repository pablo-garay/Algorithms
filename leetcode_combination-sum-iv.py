class Solution(object):  # Runtime 12 ms Beats 99.68% | Memory Beats 99.68%
    def combinationSum4(self, nums, target):  # O(target * |nums|)
        count = [0 for i in xrange(target + 1)]; count[0] = 1

        for i in xrange(target):
            if count[i] > 0:
                for num in nums:
                    if i + num <= target: count[i + num] += count[i]        
        
        return count[target]


print Solution().combinationSum4(nums = [1,2,3], target = 4)
print Solution().combinationSum4(nums = [9], target = 3)
