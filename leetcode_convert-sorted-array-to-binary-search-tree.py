# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math
class Solution(object):  # Time complexity: O(n) one pass - optimal as need to visit all elemns in worst case. Runtime: 40 ms, faster than 98.59%
    def sortedArrayToBST(self, nums):
        self.li = nums
        return self.insert_elem(0, len(nums) - 1)

    def insert_elem(self, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(self.li[left])
        else:
            mid = int(math.ceil((left + right) / 2.0))
            root = TreeNode(self.li[mid])
            root.left = self.insert_elem(left, mid - 1)
            root.right = self.insert_elem(mid + 1, right)
            return root
