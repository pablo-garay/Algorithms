from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(s)
        count2 = Counter(t)

        for item in count1:
            if count1[item] != count2[item]:
                return False
        
        for item in count2:
            if count1[item] != count2[item]:
                return False
        
        return True
