class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in dict:
                dict[sorted_s].append(s)
            else:
                dict[sorted_s] = [s]

        return dict.values()


sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
