from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # print tuple(count)
            ans[tuple(count)].append(s)
        return ans.values()


print Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print Solution().groupAnagrams([""])
print Solution().groupAnagrams(["a"])
