def between_limits(n, m, i, j):
    if 0 <= i < n and 0 <= j < m:
        return True
    else:
        return False

def check_contiguous(grid, n, m, i, j):
    count = 0

    if between_limits(n, m, i, j):
        if grid[i][j] == 1:
            count += 1
            grid[i][j] = 0
            count += check_contiguous(grid, n, m, i - 1, j - 1) + \
                     check_contiguous(grid, n, m, i - 1, j) + \
                     check_contiguous(grid, n, m, i - 1, j + 1) + \
                     check_contiguous(grid, n, m, i, j - 1) + \
                     check_contiguous(grid, n, m, i, j + 1) + \
                     check_contiguous(grid, n, m, i + 1, j - 1) + \
                     check_contiguous(grid, n, m, i + 1, j) + \
                     check_contiguous(grid, n, m, i + 1, j + 1)

    return count


def get_biggest_region(grid, n, m):
    max_num = 0

    for i in xrange(m):
        for j in xrange(n):
            num_cells = check_contiguous(grid, n, m, i, j)

            if num_cells > max_num:
                max_num = num_cells
    return max_num


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid, n, m)
