# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        self.ret = True
        self.f(head, head)
        return self.ret

    def f(self, left, right):
        if right.next is not None:
            left = self.f(left, right.next)

        if left is None or left == right or right.next == left:
            return None

        if left.val != right.val:
            self.ret = False
            return None

        return left.next
