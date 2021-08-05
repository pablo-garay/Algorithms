parent, size = {}, {}

def find(x):
    while parent[x] != x:
        x, parent[x] = (parent[x], parent[parent[x]])
    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if size[x] < size[y]:
        (x, y) = (y, x)

    parent[y] = x
    size[x] = size[x] + size[y]

class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0: return 0
        global parent, size
        parent, size = {}, {}

        for n in nums:
            parent[n], size[n] = (n, 1)

        for num in nums:
            if num + 1 in parent:
                union(num, num + 1)

        return max(size.values())


print Solution().longestConsecutive(nums = [100,4,200,1,3,2])
print Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])
print Solution().longestConsecutive(nums = [0])
