# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, left, right):
        if left is None: return right
        elif right is None: return left

        if left.val <= right.val:
            head, left = left, left.next
        else:
            head, right = right, right.next

        node = head
        while left is not None or right is not None:
            if left is None:
                node.next = right
                right = right.next
            elif right is None:
                node.next = left
                left = left.next
            else:
                if left.val <= right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
            node = node.next

        return head
