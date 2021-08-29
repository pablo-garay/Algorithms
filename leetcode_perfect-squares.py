from collections import deque

class Solution(object):  # BFS | Time Complexity: O( (sqrt(n) - int(sqrt(n))*sqrt(n) ) + O( sqrt(n) )
    def numSquares(self, n):
        options = deque([1])

        option = 2
        while option * option <= n:
            options.appendleft(option * option)
            option += 1

        frontier = {n}
        level = 0

        while frontier:
            # print options, frontier
            next_frontier = set()
            level += 1

            for item in frontier:
                for option in options:
                    if item - option == 0:
                        return level

                    if item - option > 0:
                        next_frontier.add(item - option)

            frontier = next_frontier

        return level


print Solution().numSquares(12)
print Solution().numSquares(13)
print Solution().numSquares(14)
print Solution().numSquares(15)
print Solution().numSquares(16)
print Solution().numSquares(17)
print Solution().numSquares(10000)
print Solution().numSquares(9999)
print Solution().numSquares(1)
print Solution().numSquares(2)
print Solution().numSquares(3)
print Solution().numSquares(4)
