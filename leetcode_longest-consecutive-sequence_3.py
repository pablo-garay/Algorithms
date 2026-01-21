class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        elems = set(nums)
        max_count = 1

        print(elems)

        length = 0

        for num in elems:
            if num - 1 not in elems:

                count = 1; curr = num
                while curr + 1 in elems:
                    count += 1; curr += 1
                    max_count = max(max_count, count)
                    print(count, curr, max_count)
        
        return max_count
        