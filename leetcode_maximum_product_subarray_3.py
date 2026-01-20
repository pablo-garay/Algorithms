class Solution:  # Time: O(n) - optimal as we need to traverse all the n elems of list in the worst case. Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return None

        max_accum = nums[0]
        min_accum = nums[0]
        maxprod = nums[0]

        for i in range(1, len(nums)):
            prod1, prod2 = (max_accum * nums[i], min_accum * nums[i])

            maxprod = max(maxprod, prod1, prod2, nums[i])
            
            max_accum = max(prod1, prod2, nums[i])
            min_accum = min(prod1, prod2, nums[i])
        
        return maxprod
