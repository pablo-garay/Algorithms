class Solution(object):  # O(n) : one pass. Optimal as we need to visit check each elem of the string at least once
    curr = 0

    def scoreOfParentheses(self, S):
        curr_sum = 0

        while self.curr < len(S):
            if S[self.curr] == ")":
                if S[self.curr - 1] == "(":
                    curr_sum += 1
                    return curr_sum

                else:
                    curr_sum *= 2
                    return curr_sum

            if S[self.curr] == "(":
                self.curr += 1
                curr_sum += self.scoreOfParentheses(S)

            self.curr += 1

        return curr_sum


print Solution().scoreOfParentheses("()")  # 1
print Solution().scoreOfParentheses("(())")  # 2
print Solution().scoreOfParentheses("()()")  # 2
print Solution().scoreOfParentheses("((())())")  # 6
print Solution().scoreOfParentheses("(()(()))")  # 6
print Solution().scoreOfParentheses("()(())")  # 3
print Solution().scoreOfParentheses("((())())((())())((())())")  # 18
