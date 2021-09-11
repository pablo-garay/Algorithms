from collections import Counter, defaultdict

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()  # O(n log n)
        count = Counter(nums)
        half = defaultdict(set)
        sol = set()

        # O(n^2)
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                a, b = (nums[i], nums[j])
                half[target - (a + b)].add((a, b))

        # ~O(n^2)
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                if nums[i] + nums[j] in half:
                    c, d = (nums[i], nums[j])

                    for (a, b) in half[nums[i] + nums[j]]:
                        w, x, y, z = tuple(sorted([a, b, c, d]))

                        if w == x == y == z and count[w] < 4:
                            continue
                        elif (w == x == y and count[w] < 3) or (x == y == z and count[z] < 3):
                            continue
                        elif (w == x and count[w] < 2) or (x == y and count[x] < 2) or (y == z and count[y] < 2):
                            continue

                        sol.add((w, x, y, z))

        return [list(tup) for tup in sol]  # O(n)


print Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0)
print Solution().fourSum(nums = [2,2,2,2,2], target = 8)