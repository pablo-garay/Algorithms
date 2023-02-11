# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution(object):  # Runtime 65 ms Beats 99.27%
    def mergeKLists(self, lists):  # O(n log n)
        li = []
        for head in lists:  # O(n)
            while head:
                li.append(head.val)
                head = head.next        
        if not li: return None # no elems

        li.sort()  # O(n log n)
        li = deque(li)  # O(n)

        head = node = ListNode(li.popleft())
        while li:  # O(n)
            node.next = ListNode(li.popleft())
            node = node.next
        
        return head
