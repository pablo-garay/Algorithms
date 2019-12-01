# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque

class Solution(object):
    @staticmethod
    def mergeTwoSortedLists(left, right):
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
                break
            elif right is None:
                node.next = left
                break
            else:
                if left.val <= right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
            node = node.next

        return head

    def mergeKLists(self, lists):
        if len(lists) < 1: return None
        elif len(lists) == 1: return lists[0]

        queue = deque(lists)

        while len(queue) > 1:
            queue.append(Solution.mergeTwoSortedLists(queue.popleft(), queue.popleft()))

        return queue[0]
