class Solution(object):  # O(n^2) as each elem of squared matrix visited once. Optimal as need to visit each in worst case
    def minFallingPathSum(self, A):
        dim = len(A)
        if dim == 0: return 0
        memo = [[None for _ in xrange(dim)] for _ in xrange(dim)]

        for i in xrange(len(A)):
            memo[0][i] = A[0][i]

        for r in xrange(1, len(A)):
            for c in xrange(len(A)):
                memo[r][c] = A[r][c] + memo[r - 1][c]

                for r2, c2 in [(r - 1, c - 1), (r - 1, c + 1)]:
                    if 0 <= c2 <= dim - 1 and (A[r][c] + memo[r2][c2]) < memo[r][c]:
                        memo[r][c] = A[r][c] + memo[r2][c2]

        return min(memo[dim - 1])


print Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])
print Solution().minFallingPathSum([])
print Solution().minFallingPathSum([[0]])
print Solution().minFallingPathSum([[1, 3],
                                    [4, 2]])
print Solution().minFallingPathSum([[1, 3, 6],
                                    [2, 4, 1],
                                    [5, 5, 1]])
print Solution().minFallingPathSum([[-62,-63, 23, 31],
                                    [-5 ,-82, 52, 76],
                                    [ 85, 69, 80, 85],
                                    [  8,-22, 41,-45]])

