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
