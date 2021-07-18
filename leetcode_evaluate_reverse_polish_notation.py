class Solution(object):  # O(n) as each elem in tokens is visited only once (optimal as need to visit each once at least)
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(int(eval(str(float(a)) + token + b))))
            else:
                stack.append(token)

        return stack.pop()


print Solution().evalRPN(["2","1","+","3","*"])
print Solution().evalRPN(["2"])
print Solution().evalRPN(["4","13","5","/","+"])
print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
