from collections import defaultdict

class Solution(object):  # Runtime 64 ms Beats 99.36%
    def groupAnagrams(self, strs):  # Time: O(len(strs) * m log m). Space: O(len(strs))
        dictio = defaultdict(list)

        for s in strs: # O(len(strs) * m log m)
            dictio[tuple(sorted(s))].append(s)  # sorting: O(m log m) for longest string m; converting to tuple: O(m); appending to dictio: O(1)

        return dictio.values()
