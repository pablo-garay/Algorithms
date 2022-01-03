import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):  # Time: O(n) n: num of all elems in all lists - optimal as need to traverse all in worst case. Space: O(n)
    def mergeKLists(self, lists):
        concat = []
        for head in lists:  # O(n) where n is num of all elems in all lists
            while head is not None:
                concat.append(head.val)
                head = head.next

        if not concat: return
        heapq.heapify(concat)  # O(n)

        head = ListNode(heapq.heappop(concat)); prev = head
        while concat:  # O(n)
            prev.next = ListNode(heapq.heappop(concat))
            prev = prev.next

        return head
