class Solution(object):  # Linear time complexity. Optimal as each elem in array has to be visited at least once in worst case
    def rotate(self, matrix):
        def rotate_pos_clockwise(row, col):
            return col, self.max_ind - row

        n = len(matrix)
        self.max_ind = n - 1

        for row in range(n / 2):
            for col in range(row, n - row - 1):
                up_val = matrix[row][col]
                row_right, col_right = rotate_pos_clockwise(row, col)
                row_bottom, col_bottom = rotate_pos_clockwise(row_right, col_right)
                row_left, col_left = rotate_pos_clockwise(row_bottom, col_bottom)
                matrix[row][col] = matrix[row_left][col_left]
                matrix[row_left][col_left] = matrix[row_bottom][col_bottom]
                matrix[row_bottom][col_bottom] = matrix[row_right][col_right]
                matrix[row_right][col_right] = up_val

        print matrix


Solution().rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])
Solution().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
Solution().rotate(matrix = [[1]])
Solution().rotate(matrix = [[1,2],[3,4]])
