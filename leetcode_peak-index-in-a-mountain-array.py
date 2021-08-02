class Solution(object):  # O(log n). It's binary search time complexity.
    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) / 2

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return str(mid)
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                right = mid - 1

        return -1


print Solution().peakIndexInMountainArray(arr = [0,1,0])
print Solution().peakIndexInMountainArray(arr = [0,2,1,0])
print Solution().peakIndexInMountainArray(arr = [0,10,5,2])
print Solution().peakIndexInMountainArray(arr = [3,4,5,1])
print Solution().peakIndexInMountainArray(arr = [24,69,100,99,79,78,67,36,26,19])
