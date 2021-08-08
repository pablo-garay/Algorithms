class Solution(object):  # Complexity | Time: log(cols) Space: O(1) - 20 ms, faster than 98.79%
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        for row in xrange(rows):
            if matrix[row][0] <= target <= matrix[row][cols - 1]:
                return self.bin_search(0, cols - 1, row, matrix, target)

        return False

    def bin_search(self, min_i, max_i, index, matrix, target):

        while min_i <= max_i:
            mid = (min_i + max_i) / 2

            if matrix[index][min_i] > target:
                return False
            val = matrix[index][mid]

            if val == target:
                return True

            elif val < target:
                min_i = mid + 1
            else:
                max_i = mid - 1

        return False


print Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
print Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)