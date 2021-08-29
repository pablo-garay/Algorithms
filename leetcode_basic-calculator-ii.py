import re
from collections import deque

class Solution(object):  # O(n)
    def calc(self, tokens, mult_ops=False, sum_ops=False):
        new_tokens = deque()

        while tokens:
            token = tokens.popleft()
            if   mult_ops and token == "*": new_tokens.append(int(new_tokens.pop()) * int(tokens.popleft()))
            elif mult_ops and token == "/": new_tokens.append(int(new_tokens.pop()) / int(tokens.popleft()))
            elif sum_ops  and token == "+": new_tokens.append(int(new_tokens.pop()) + int(tokens.popleft()))
            elif sum_ops  and token == "-": new_tokens.append(int(new_tokens.pop()) - int(tokens.popleft()))
            else: new_tokens.append(token)

        return new_tokens

    def calculate(self, s):
        tokens = deque(re.findall('\d+|\S', s))

        if any(op in tokens for op in "*/"):
            tokens = self.calc(tokens, mult_ops=True)

        if any(op in tokens for op in "+-"):
            tokens = self.calc(tokens, sum_ops=True)

        return tokens[0]

    # def tokenize(self, s):
    #     operators = set("*/+-")
    #     tokens = deque()
    #     buffer = ""
    #
    #     for c in s:
    #         if c.isspace():
    #             continue
    #         elif c in operators:
    #             tokens.append(int(buffer))
    #             tokens.append(c)
    #             buffer = ""
    #         else:
    #             buffer += c
    #     if buffer:
    #         tokens.append(int(buffer))
    #
    #     return tokens


print Solution().calculate(s = "3+2*2")
print Solution().calculate(s = "3+2*2*2*2/4")
print Solution().calculate(s = " 3/2 ")
print Solution().calculate(s = " 3+5 / 2 ")
print Solution().calculate(s = "33+222*222")
print Solution().calculate(s = "1")
print Solution().calculate(s = "111")
