class Solution:
    def encode(self, strs: List[str]) -> str:
        print("".join([word + "#EOF" for word in strs]))
        return "".join([word + "#EOF" for word in strs])

    def decode(self, s: str) -> List[str]:
        out = []
        accum = ""
        i = 0
        while i < len(s):
            char = s[i]

            if char == "#" and i + 3 < len(s) and s[i:i+4] == "#EOF":
                out.append(accum) ; accum = ""
                started = False
                i += 3
            else:
                accum += char
        
            i += 1
        return out


obj = Solution()
print obj.encode(["lint","code","love","you"])
print obj.encode(["we", "say", ":", "yes"])
obj = Solution()
print obj.decode(obj.encode(["lint","code","love","you"]))
obj = Solution()
print obj.decode(obj.encode(["we", "say", ":", "yes"]))
