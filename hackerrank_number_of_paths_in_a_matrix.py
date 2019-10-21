def numberOfPaths(a):   # DP solution. O(m*n) where m, n are input matrix dimensions
    m, n = len(a), len(a[0])
    if m == 0 or n == 0 or a[m - 1][n - 1] == 0: return 0

    memo = [[None for c in xrange(n)] for r in xrange(m)]

    memo[m - 1][n - 1] = 1
    for r in reversed(xrange(m - 1)):
        memo[r][n - 1] = memo[r + 1][n - 1] if a[r][n - 1] == 1 else 0
    for c in reversed(xrange(n - 1)):
        memo[m - 1][c] = memo[m - 1][c + 1] if a[m - 1][c] == 1 else 0

    for r in reversed(xrange(m - 1)):
        for c in reversed(xrange(n - 1)):
            memo[r][c] = 0

            if a[r][c] == 0:  # blocked cell
                continue

            if r + 1 <= m:
                memo[r][c] += memo[r + 1][c]
            if c + 1 <= n:
                memo[r][c] += memo[r][c + 1]

    return memo[0][0] % (10**9 + 7)  # array elem which contains the final answer


print numberOfPaths([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]])

print numberOfPaths([[1, 1],
                     [0, 1]])

print numberOfPaths([[0, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]])

print numberOfPaths([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 0]])

print numberOfPaths([[1, 1, 1, 1],
                     [1, 1, 1, 0],
                     [1, 1, 0, 1]])

print numberOfPaths([[1, 1, 0, 1],
                     [1, 1, 1, 1]])
