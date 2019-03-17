class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char == "{" or char == "(" or char == "[":
                stack.append(char)
            else:  # char is a closing bracket
                if not stack:  # empty stack
                    return False
                else:
                    top_stack = stack.pop()
                    if (top_stack == "(" and char != ")") or (top_stack == "{" and char != "}") or (top_stack == "[" and char != "]"):
                        return False

        if not stack:  # stack is empty
            return True
        return False
