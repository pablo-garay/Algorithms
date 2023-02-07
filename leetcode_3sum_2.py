from collections import Counter

class Solution(object):  # O(n^2)
    def threeSum(self, nums):
        nums.sort()  # O(n log n)
        count = Counter(nums)
        out = set()

        # handle special case of 0's
        if count[0] >= 3:
            out.add((0, 0, 0))        

        for i in xrange(len(nums) - 1):  # O(n^2)
            if nums[i] == 0: continue  # output of type: a <= b <= c, only case when a=0 is (0,0,0) which already was handled
            for j in xrange(i + 1, len(nums)):
                a, b = (nums[i], nums[j]) 
                c = -(a + b)

                if c in count and a <= b <= c:  # note any triplet can be arranged such that a <= b <= c (so we use this to filter duplicates)
                    if a == c or b == c:
                        if count[c] >= 2:
                            out.add((a, b, c))
                    
                    else:
                        out.add((a, b, c))
        
        return out
