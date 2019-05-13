from collections import Counter

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count = Counter(A)
        num_doubles = 0

        if 0 in count:
            if count[0] % 2 != 0:
                return False
            else:
                del count[0]

        for num in sorted(count.keys(), cmp=lambda x,y: cmp(abs(x), abs(y))):
            if count[num] > 0 and count[num * 2] > 0:
                count[num * 2] -= count[num]
                del count[num]
                if count[num * 2] == 0: del count[num * 2]

        if count:
            return False

        return True



print Solution().canReorderDoubled([3,1,3,6])
print Solution().canReorderDoubled([2,1,2,6])
print Solution().canReorderDoubled([1,2,4,16,8,4])
print Solution().canReorderDoubled([0])
print Solution().canReorderDoubled([0, 0, 0])
print Solution().canReorderDoubled([2, 4, 8, 15])
print Solution().canReorderDoubled([1,2,4,4,8])
print Solution().canReorderDoubled([1,2,4,4,4,8])

print
print Solution().canReorderDoubled([])
print Solution().canReorderDoubled([0, 0])
print Solution().canReorderDoubled([0, 0, 0, 0])
print Solution().canReorderDoubled([1,2,4,8])
print Solution().canReorderDoubled([1,2,2,4,4,8])
print Solution().canReorderDoubled([1,2,2,4,4,4,8,8])
print Solution().canReorderDoubled([4,-2,2,-4])
print Solution().canReorderDoubled([1,2,1,-8,8,-4,4,-4,2,-2])
