class Solution(object):
    def decodeAtIndex(self, S, K):
        stack = []
        elems = 0

        i = 0
        while i < len(S):
            char = S[i]

            if char.isalpha():  # letter
                stack.append(char)
                i += 1
                elems += 1

                if elems == K:
                    return stack.pop()

            else:  # digit
                num = int(char)
                i += 1
                while i < len(S) and S[i].isdigit():
                    num *= int(S[i])
                    i += 1

                stack.append(str(num))
                elems *= num

                if elems >= K:
                    break

        while elems > K and K > 0:
            # print "elems", elems, "K", K, "stack", stack
            char = stack.pop()

            if char.isdigit():
                elems /= int(char)
                K = K % elems
            else:
                elems -= 1

        while stack[-1].isdigit():
            stack.pop()

        return stack[-1]


print Solution().decodeAtIndex(S = "leet2code3", K = 1) # l
print Solution().decodeAtIndex(S = "leet2code3", K = 10) # o
print Solution().decodeAtIndex(S = "leet2code3", K = 9) # c
print Solution().decodeAtIndex(S = "ha22", K = 5) # h
print Solution().decodeAtIndex(S = "a2b3c4d5e6f7g8h9", K = 10) # c
print Solution().decodeAtIndex("aa3", 6) # a
print Solution().decodeAtIndex("a23", 6) # a
print Solution().decodeAtIndex("a23b", 6) # a
print Solution().decodeAtIndex("y959q969u3hb22odq595", 222280369)
