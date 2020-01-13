class Solution(object):
    def reverseParentheses(self, s):
        parens = ["(", ")"]
        stack = []
        li_s = list(s)

        for i in xrange(len(li_s)):
            if li_s[i] == "(":
                stack.append(i + 1)

            elif li_s[i] == ")":
                right = i
                left = stack.pop()
                li_s[left:right] = li_s[left:right][::-1]

        return "".join([c for c in li_s if c not in parens])



print Solution().reverseParentheses(s="(ed(et(oc))el)")
print Solution().reverseParentheses(s="(abcd)")
print Solution().reverseParentheses(s="(u(love)i)")
print Solution().reverseParentheses(s="a(bcdefghijkl(mno)p)q")
print Solution().reverseParentheses(s="((ab))")
print Solution().reverseParentheses(s="")
print Solution().reverseParentheses(s="12(a(bc))")

