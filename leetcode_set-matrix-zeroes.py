class Solution(object):  # constant space
    def setZeroes(self, matrix):
        rows, cols = (len(matrix), len(matrix[0]))

        for r in xrange(rows):
            for c in xrange(cols):
                if matrix[r][c] == 0:
                    for c1 in xrange(cols):
                        if matrix[r][c1] == "r" or matrix[r][c1] == "rc":
                            break

                        if matrix[r][c1] != 0:
                            if matrix[r][c1] == "c" or matrix[r][c1] == "rc":
                                matrix[r][c1] = "rc"
                            else:
                                matrix[r][c1] = "r"

                    for r1 in xrange(rows):
                        if matrix[r1][c] == "c" or matrix[r1][c] == "rc":
                            break

                        if matrix[r1][c] != 0:
                            if matrix[r1][c] == "r" or matrix[r1][c] == "rc":
                                matrix[r1][c] = "rc"
                            else:
                                matrix[r1][c] = "c"

        for r in xrange(rows):
            for c in xrange(cols):
                if matrix[r][c] in ("r", "c", "rc"):
                    matrix[r][c] = 0


print Solution().setZeroes(matrix = [[1,1,1],
                                     [1,0,1],
                                     [1,1,1]])
print Solution().setZeroes(matrix = [[0,1,2,0],
                                     [3,4,5,2],
                                     [1,3,1,5]])
print Solution().setZeroes(matrix = [[1,0,1],
                                     [0,1,1],
                                     [1,1,1]])
print Solution().setZeroes(matrix = [[0,0,0],
                                     [0,0,0],
                                     [0,0,0]])

