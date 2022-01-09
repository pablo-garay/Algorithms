class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return "/".join(strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        out = []
        i = 0; accum = ""
        while i < len(str):
            if str[i] != "/":
                accum += str[i]
            else:
                out.append(accum)
                accum = ""
                if i + 1 < len(str) and str[i + 1] == "/":
                    i += 1
            i += 1
        out.append(accum)

        return out

obj = Solution()
print obj.encode(["lint","code","love","you"])
print obj.encode(["we", "say", ":", "yes"])
obj = Solution()
print obj.decode(obj.encode(["lint","code","love","you"]))
obj = Solution()
print obj.decode(obj.encode(["we", "say", ":", "yes"]))
