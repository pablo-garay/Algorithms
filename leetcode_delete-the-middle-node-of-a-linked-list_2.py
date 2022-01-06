# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):  # Time: O(n) for n elements in linked list - optimal as need to visit all nodes in worst case
    def deleteMiddle(self, head):
        prev_head = ListNode()
        prev_head.next = head
        slow = fast = prev_head

        while fast and fast.next and fast.next.next:
            slow, fast = (slow.next, fast.next.next)

        slow.next = slow.next.next
        return prev_head.next
