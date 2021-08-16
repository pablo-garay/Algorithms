class Solution(object):
    def productExceptSelf(self, nums):
        count_zeros = nums.count(0)

        if count_zeros > 1:
            return [0 for _ in xrange(len(nums))]

        prod = 1
        for num in nums:
            if num != 0:
                prod *= num

        if count_zeros == 1:
            return [0 if num != 0 else prod for num in nums]

        answer = []
        for num in nums:
            answer.append(int(prod * num ** -1))

        return answer


print Solution().productExceptSelf(nums = [1,2,3,4])
print Solution().productExceptSelf(nums = [-1,1,0,-3,3])
print Solution().productExceptSelf(nums = [-1,1,0,-3,0])
