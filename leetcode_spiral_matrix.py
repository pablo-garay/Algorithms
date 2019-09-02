class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        output = [matrix[0][0]]
        col_max, row_max = len(matrix[0]) - 1, len(matrix) - 1

        seq = [col_max]
        min_val = min(col_max, row_max)

        for val in xrange(min_val):
            seq.append(row_max - val)
            seq.append(col_max - val)
        if row_max > col_max:
            seq.append(row_max - col_max)

        row, col = (0, 0)
        direc = 0

        for num_moves in seq:
            if direc == 0:  # right
                for moves in xrange(num_moves):
                    col += 1
                    output.append(matrix[row][col])

            elif direc == 1:  # down
                for moves in xrange(num_moves):
                    row += 1
                    output.append(matrix[row][col])

            elif direc == 2:  # left
                for moves in xrange(num_moves):
                    col -= 1
                    output.append(matrix[row][col])

            elif direc == 3:  # up
                for moves in xrange(num_moves):
                    row -= 1
                    output.append(matrix[row][col])

            direc = (direc + 1) % 4

        return output


print Solution().spiralOrder(
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
)

print Solution().spiralOrder(
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]]
)

print Solution().spiralOrder(
[[1]]
)

print Solution().spiralOrder(
[[1, 2]]
)

print Solution().spiralOrder(
[[ 1,  2,  3,  4,  5],
 [ 6,  7,  8,  9, 10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25]
 ]
)

print Solution().spiralOrder(
[[ 1,  2,  3,  4,  5],
 [ 6,  7,  8,  9, 10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25],
 [26, 27, 28, 29, 30],
 [31, 32, 33, 34, 35],
 [36, 37, 38, 39, 40]
 ]
)

print Solution().spiralOrder(
[[1],
 [2],
 [3]]
)
