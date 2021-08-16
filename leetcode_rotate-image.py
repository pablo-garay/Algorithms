class Solution(object):
    def rotate(self, matrix):
        rows, cols = (len(matrix), len(matrix[0]))
        last_row, last_col = rows - 1, cols - 1

        offset = 0
        cell_moves = cols - 1

        for row in range(rows / 2):
            max_ind = last_row - offset
            min_row = min_col = offset

            for col in range(offset, cols - offset - 1):
                next_row, next_col = (row, col)

                curr_row, curr_col = (next_row, next_col)
                delta = cell_moves - (max_ind - curr_col)
                next_row, next_col = (min_row + delta, max_ind)
                curr_val, next_val = (matrix[curr_row][curr_col], matrix[next_row][next_col])
                matrix[next_row][next_col] = curr_val

                curr_row, curr_col = (next_row, next_col)
                delta = cell_moves - (max_ind - curr_row)
                next_row, next_col = (max_ind, max_ind - delta)
                curr_val, next_val = (next_val, matrix[next_row][next_col])
                matrix[next_row][next_col] = curr_val

                curr_row, curr_col = (next_row, next_col)
                delta = cell_moves - (curr_col - min_col)
                next_row, next_col = (max_ind - delta, min_col)
                curr_val, next_val = (next_val, matrix[next_row][next_col])
                matrix[next_row][next_col] = curr_val

                curr_row, curr_col = (next_row, next_col)
                delta = cell_moves - (curr_row - min_row)
                next_row, next_col = (min_row, min_col + delta)
                curr_val, next_val = (next_val, matrix[next_row][next_col])
                matrix[next_row][next_col] = curr_val

            offset += 1
            cell_moves -= 2

        print matrix


Solution().rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])
Solution().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
Solution().rotate(matrix = [[1]])
Solution().rotate(matrix = [[1,2],[3,4]])
