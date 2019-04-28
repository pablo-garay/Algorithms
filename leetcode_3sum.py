from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        count = Counter(nums)
        sol = set()

        # handle special case of 0's
        if count[0] >= 3:
            sol.add((0, 0, 0))

        # O(n^2)
        for i in xrange(len(nums)):
            a = nums[i]
            if a == 0: continue

            for j in xrange(i + 1, len(nums)):
                b = nums[j]
                if b == 0: continue
                c = -(a + b)

                if c in count:
                    sorted_tup = tuple(sorted((a, b, c)))
                    if a == c:
                        if count[a] >= 2: sol.add(sorted_tup)
                    elif b == c:
                        if count[c] >= 2: sol.add(sorted_tup)
                    else:
                        sol.add(sorted_tup)

        formatted_sol = [list(tup) for tup in sol]  # O(n)
        return formatted_sol


print Solution().threeSum([-1, 0, 1, 2, -1, -4])
