# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        self.ret = True
        self.left_ind, self.right_ind = (0, 0)
        self.f(head, head)
        return self.ret

    def f(self, left, right):
        if right.next is not None:
            self.right_ind += 1
            left = self.f(left, right.next)

        if left is None or self.left_ind >= self.right_ind:
            return None

        if left.val != right.val:
            self.ret = False
            return None

        self.left_ind += 1; self.right_ind -= 1
        return left.next
