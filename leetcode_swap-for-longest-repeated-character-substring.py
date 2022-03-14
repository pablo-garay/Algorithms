from collections import Counter
class Solution(object):  # Time: O(n) each char in string visited at most thrice. Space: O(n)
    def maxRepOpt1(self, text):
        count = Counter(text)  # O(n)
        left = 0; right = 0; out = 0
        accum = 0; other_char = None

        while left < len(text) and right < len(text):
            if text[left] == text[right]:
                if accum < count[text[left]]:
                    accum += 1
                    out = max(out, accum + 1 if (other_char is None and accum < count[text[left]]) else 0)
                right += 1

            else:
                if other_char is None and count[text[left]] > accum:
                    other_char = text[right]
                    accum += 1; out = max(out, accum)
                    right += 1

                else:
                    if other_char is None:
                        left = right
                        accum = 0
                    else:
                        while text[left] != other_char:
                            left += 1
                        right = left
                        accum = 0; other_char = None

        return out


print Solution().maxRepOpt1(text = "ababa")
print Solution().maxRepOpt1(text = "aaabaaa")
print Solution().maxRepOpt1(text = "aaaaa")
print Solution().maxRepOpt1(text = "abcdef")
print Solution().maxRepOpt1(text = "abcdef")
print Solution().maxRepOpt1(text = "aaabcbbbbb")
print Solution().maxRepOpt1(text = "aabaaabaaaba")
print Solution().maxRepOpt1(text = "acbaaa")
