class Solution(object):
    def get_common_prefix(self, s1, s2):
        res = ""

        for i in xrange(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return res
            else:
                res += s1[i]
        return res


    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        elif len(strs) == 1: return strs[0]
        common_prefix = self.get_common_prefix(strs[0], strs[1])

        for i in xrange(2, len(strs)):
            common_prefix = self.get_common_prefix(common_prefix, strs[i])

        return common_prefix


print Solution().longestCommonPrefix(["flower"])
print Solution().longestCommonPrefix(["flower","flow","flight"])
print Solution().longestCommonPrefix([["dog","racecar","car"]])
