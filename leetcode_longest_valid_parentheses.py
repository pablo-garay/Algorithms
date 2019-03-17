# Time Complexity: O(n) solution
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        second_stack = [0]
        max_count = 0

        for char in s:
            if char == "(":
                stack.append(char)
                second_stack.append(0)
            else:  # closing parens
                if not stack:  # empty stack
                    second_stack[-1] = 0
                else:
                    stack.pop()
                    prev_count = second_stack.pop()
                    second_stack[-1] += 2 + prev_count

                    if second_stack[-1] > max_count:
                        max_count = second_stack[-1]

        return max_count


print Solution().longestValidParentheses("(()")  # 2
print Solution().longestValidParentheses(")()())")  # 4
print Solution().longestValidParentheses("(()(()")  # 2
print Solution().longestValidParentheses("(()(()(((()")  # 2
print Solution().longestValidParentheses("(()(())")  # 6
print Solution().longestValidParentheses("(()(())())")  # 10
print Solution().longestValidParentheses("(()(())())(()))()")   # 14

print Solution().longestValidParentheses(")(())))(())())")  # 6

