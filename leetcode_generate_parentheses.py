class Solution(object):
    def genNextStep(self, s, to_open, to_close):
        if to_close > 0:
            s.append(")")
            if to_close - 1 == 0 and to_open == 0:
                    self.res.append("".join(s))
            else:
                self.genNextStep(s, to_open, to_close - 1)
            s.pop()

        if to_open > 0:
            s.append("(")
            to_close += 1
            self.genNextStep(s, to_open - 1, to_close)
            s.pop()


    def generateParenthesis(self, n):
        to_open, to_close = (n, 0)
        self.res = []

        self.genNextStep([], to_open, to_close)
        return self.res


print Solution().generateParenthesis(0)
print Solution().generateParenthesis(1)
print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
print Solution().generateParenthesis(4)
print Solution().generateParenthesis(5)
print Solution().generateParenthesis(10)

