class Solution(object):  # Runtime 228 ms Beats 99.54% Memory Beats 85.55%
    def longestConsecutive(self, nums):  # Time: O(n) as each num is visited at most twice (optimal as need to traverse whole array in worst case)
        numset = set(nums); out = 0  # Space: O(n)

        for num in numset:
            if num - 1 in numset: continue

            streak = 1; nextt = num + 1
            while nextt in numset:
                streak += 1; nextt += 1
            out = max(out, streak)
        
        return out
