class Solution(object):  # Complexity: O(n). Optimal as n elements have to be visited
    def minRemoveToMakeValid(self, s):
        opened_parens = 0
        right = 0
        res = ""

        for i in xrange(len(s)):
            char = s[i]

            if char == "(":
                if i > right:
                    right = i
                right += 1
                while right < len(s) and s[right] != ")":
                    right += 1
                if right >= len(s):
                    continue

                opened_parens += 1

            elif char == ")":
                if opened_parens > 0:
                    opened_parens -= 1
                else:
                    continue

            res += char

        return res


print Solution().minRemoveToMakeValid("a)b(c)d")
print Solution().minRemoveToMakeValid("a(b(c)d")
print Solution().minRemoveToMakeValid("lee(t(c)o)de)")
print Solution().minRemoveToMakeValid("))((")