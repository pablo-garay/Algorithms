from collections import deque

class Solution(object):  # Complexity is linear (optimal) as each elem in matrix is visited at most twice
    def updateMatrix(self, mat):
        num_r, num_c = len(mat), len(mat[0])
        frontier = deque()

        for r in xrange(num_r):
            for c in xrange(num_c):
                if mat[r][c] == 1:
                    mat[r][c] = None

                    for r2, c2 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= r2 < num_r and 0 <= c2 < num_c and mat[r2][c2] == 0:
                            frontier.append((r, c))
                            break

        while frontier:
            (r, c) = frontier.popleft()
            label = float("inf")

            for r2, c2 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= r2 < num_r and 0 <= c2 < num_c:
                    if mat[r2][c2] is not None:
                        label = min(label, mat[r2][c2] + 1)
                        mat[r][c] = label
                    else:
                        frontier.append((r2, c2))

        return mat


print Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]])
print Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])
print Solution().updateMatrix([[0,0,1,0,1,1,1,0,1,1],
                               [1,1,1,1,0,1,1,1,1,1],
                               [1,1,1,1,1,0,0,0,1,1],
                               [1,0,1,0,1,1,1,0,1,1],
                               [0,0,1,1,1,0,1,1,1,1],
                               [1,0,1,1,1,1,1,1,1,1],
                               [1,1,1,1,0,1,0,1,0,1],
                               [0,1,0,0,0,1,0,0,1,1],
                               [1,1,1,0,1,1,0,1,0,1],
                               [1,0,1,1,1,0,1,1,1,0]])
