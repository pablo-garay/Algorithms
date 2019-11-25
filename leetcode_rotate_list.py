# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):  # O(n) solution. Can't be faster than O(n): need to traverse whole list in the worst case
    def rotateRight(self, head, k):
        if head is None:
            return head

        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next

        k = k % length
        if k == 0:
            return head

        node = head
        count = 0

        while node is not None:
            count += 1

            if count == length - k:
                prev_node = node
            elif count == length - k + 1:
                actual_node = node

            if count == length:
                last_node = node
            node = node.next

        prev_node.next, last_node.next = None, head

        return actual_node
