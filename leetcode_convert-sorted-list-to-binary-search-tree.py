# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math
class Solution(object):  # O(n) where n is length of linked list (two passes). Runtime: 112 ms, faster than 99.30%
    def sortedListToBST(self, head):
        if head is None:
            return None

        self.li = []
        node = head
        while node is not None:
            self.li.append(node.val)
            node = node.next

        return self.insert_elem(0, len(self.li) - 1)

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
