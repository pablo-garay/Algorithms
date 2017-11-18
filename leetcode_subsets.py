# Interesting problem: how would you do it in C? There you will really understand what's happening
# as opposed to using built-in data structures in Python which hide what happens "behind the scenes"

class Solution(object):
    res_list = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res_list = []
        self.subsets_extended(nums, [])
        return self.res_list

    def subsets_extended(self, nums, list_so_far):
        if nums:
            nums_copy = nums[:]  # make a copy of nums - since lists are mutable and modifications in subsequent calls will change it
            elem = nums_copy.pop()

            self.subsets_extended(nums_copy, list_so_far)
            self.subsets_extended(nums_copy, list_so_far + [elem])
        else:
            self.res_list.append(list_so_far)

