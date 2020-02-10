# class Solution(object):
#     def numRollsToTarget(self, d, f, target):
#         self.memo = {(0, 0): 1}
#         return self.opt(d, target, f)
#
#     def opt(self, curr_die, curr_target, f):
#         if (curr_die, curr_target) == (0, 0):
#             return 1
#         elif curr_die < 0 or curr_target < 0:
#             return 0
#         elif (curr_die, curr_target) in self.memo:
#             return self.memo[(curr_die, curr_target)]
#
#         self.memo[(curr_die, curr_target)] = 0
#         for v in xrange(1, f + 1):
#             self.memo[(curr_die, curr_target)] += self.opt(curr_die - 1, curr_target - v, f)
#
#         return self.memo[(curr_die, curr_target)] % (10 ** 9 + 7)


from collections import deque

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        memo = {(0, 0): 1, (d, target): 0}
        queue = deque([(0, 0)])  # (die, suma)

        while queue:
            die, suma = queue.popleft()

            if die + 1 <= d:
                for v in xrange(1, f + 1):
                    if suma + v <= target:

                        if (die + 1, suma + v) not in memo:
                            memo[(die + 1, suma + v)] = 0
                            queue.append((die + 1, suma + v))
                        memo[(die + 1, suma + v)] += memo[(die, suma)]

        return memo[(d, target)] % (10 ** 9 + 7)


print Solution().numRollsToTarget(d = 1, f = 6, target = 3)
print Solution().numRollsToTarget(d = 2, f = 6, target = 7)
print Solution().numRollsToTarget(d = 2, f = 5, target = 10)
print Solution().numRollsToTarget(d = 1, f = 2, target = 3)
print Solution().numRollsToTarget(d = 30, f = 30, target = 500)
