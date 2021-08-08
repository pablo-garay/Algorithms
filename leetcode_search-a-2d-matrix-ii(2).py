class Solution(object):  # Complexity | Time: O(m + n) Space: O(1)
    def searchMatrix(self, matrix, target):
        row, col = (0, len(matrix[0]) - 1)

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True

            elif target > matrix[row][col]:
                row += 1

            elif target < matrix[row][col]:
                col -= 1

        return False


print Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
print Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)

print Solution().searchMatrix([[1 ,3 ,5 , 7,9],
                               [2 ,4 ,6 , 8,10],
                               [11,13,15,17,19],
                               [12,14,16,18,20],
                               [21,22,23,24,25]], 13)