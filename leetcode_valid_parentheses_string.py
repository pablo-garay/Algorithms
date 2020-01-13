class Solution(object):
    def checkValidString(self, s):
        open_min, open_max = (0, 0)

        for char in s:
            if char == "(":
                open_min += 1
                open_max += 1
            elif char == ")":
                if open_max == 0:
                    return False

                open_max -= 1
                open_min = max(open_min - 1, 0)

            else:
                open_max += 1
                open_min = max(open_min - 1, 0)

        return (open_min == 0)


print Solution().checkValidString("()")  # True
print Solution().checkValidString("(*)")  # True
print Solution().checkValidString("(*))")  # True
print Solution().checkValidString("*()(")  # False

print Solution().checkValidString("")  # True
print Solution().checkValidString("((*))")  # True
print Solution().checkValidString("(*))")  # True
print Solution().checkValidString("((*)")  # True
print Solution().checkValidString("((**))")  # True
print Solution().checkValidString("())***")  # False

print Solution().checkValidString("(((*(**))(*))")  # True
print Solution().checkValidString("()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))")  # True
print Solution().checkValidString("(*())(()*((*(((()*())*()())(((((()*)()(((((()()))*)()))((())((((())))**(())()()()())((())(*())()*)()")  # True


print Solution().checkValidString("((*)(*))((*")  # False

