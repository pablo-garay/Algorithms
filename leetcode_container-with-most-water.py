class Solution(object):  # Complexity | Space: O(1) Time: O(n) optimal as need to traverse each elem in array in worst case
    def maxArea(self, height):
        opt = float("-inf")
        left, right = (0, len(height) - 1)

        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > opt:
                opt = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return opt


print Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])
print Solution().maxArea(height = [1,1])
print Solution().maxArea(height = [4,3,2,1,4])
print Solution().maxArea(height = [1,2,1])
print Solution().maxArea([1,3,2,5,25,24,5])

#
# Idea / Proof:
#
# The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
# All other containers are less wide and thus would need a higher water level in order to hold more water.
# The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
#
# the h[i] == h[j] case.
# You need to prove that in this case, it does not matter whether you perform i++ or j--, because if h[i] == h[j], neither (i+1, j) or (i, j-1) can be potential solutions because the area obtained is necessarily smaller than (i, j).
# 