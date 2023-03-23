class Solution(object):  # Runtime 67 ms Beats 96.38% Memory Beats 93.13%
    def findAnagrams(self, s, p):  # Time: O (|s|). Space: O(1)
        if len(p) > len(s): return []
        output = []
        
        array_s = [0 for _ in xrange(27)]
        array_p = [0 for _ in xrange(27)]
        index = 0; window = len(p) - 1
        
        for char in p:
            array_p[ord(char) - ord('a')] += 1
        
        for char in s[:window]:
            array_s[ord(char) - ord('a')] += 1
        
        while index + window < len(s):
            curr_char = s[index + window]
            array_s[ord(curr_char) - ord('a')] += 1  # add
            
            if array_s == array_p:
                output.append(index)
            
            array_s[ord(s[index]) - ord('a')] -= 1  # remove
            index += 1
        
        return output


print Solution().anagrams_indexes(s = "cbaebabacd", p = "abc")
print Solution().anagrams_indexes(s = "abab", p = "ab")
print Solution().anagrams_indexes(s = "abab", p = "ababa")
print Solution().anagrams_indexes(s = "aba", p = "aab")
# window = len(p) - 1 = 3 - 1 = 2
