class Solution(object):  # Runtime: 88 ms, faster than 76.17%
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}

        for s in strs:  # Total: O(|strs|) * O(|s| log |s|)
            sorted_s = "".join(sorted(s))  # O(|s| log |s|)
            if sorted_s in dict:  # O(1)
                dict[sorted_s].append(s)
            else:
                dict[sorted_s] = [s]  # O(1)

        return dict.values()


sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
