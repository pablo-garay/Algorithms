from heapq import *

class Solution(object):  # Runtime 11 ms Beats 100% Memory Beats 81.88%
    def combinationSum4(self, nums, target):
        count = [0 for i in xrange(target + 1)]; count[0] = 1
        
        q = [0]; heapify(q); prev_added_to_q = {0}

        while q:
            i = heappop(q)

            for num in nums:
                i_next = i + num
                if i_next <= target:
                    count[i_next] += count[i]
                    if i_next not in prev_added_to_q and i_next != target:
                        heappush(q, i_next)
                        prev_added_to_q.add(i_next)
        
        return count[target]


print Solution().combinationSum4(nums = [1,2,3], target = 4)
print Solution().combinationSum4(nums = [9], target = 3)
