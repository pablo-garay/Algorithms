class Solution(object):  # Complexity | Time: min(mlog n, nlog m) Space: O(1)
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])

        if cols >= rows:
            for col in xrange(cols):
                if self.bin_search(0, rows - 1, col, matrix, target, is_vertical=True):
                    return True
        else:
            for row in xrange(rows):
                if self.bin_search(0, cols - 1, row, matrix, target, is_vertical=False):
                    return True

        return False

    def bin_search(self, min_i, max_i, index, matrix, target, is_vertical=False):

        while min_i <= max_i:
            mid = (min_i + max_i) / 2

            if is_vertical is False:
                if matrix[index][min_i] > target:
                    return False
                val = matrix[index][mid]
            else:
                if matrix[min_i][index] > target:
                    return False
                val = matrix[mid][index]

            if val == target:
                return True

            elif val < target:
                min_i = mid + 1
            else:
                max_i = mid - 1

        return False


print Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
print Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)

print Solution().searchMatrix([[1 ,3 ,5 , 7,9],
                               [2 ,4 ,6 , 8,10],
                               [11,13,15,17,19],
                               [12,14,16,18,20],
                               [21,22,23,24,25]], 13)