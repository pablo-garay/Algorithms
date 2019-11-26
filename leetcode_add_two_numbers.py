# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remnant = 0
        l1_head = l1

        if l1 is None:
            return l2

        while l1 is not None:
            if l2 is None:
                suma = l1.val + remnant
                l1.val, remnant = (suma % 10, suma / 10)

            else:
                suma = (l1.val + l2.val + remnant)
                l1.val, remnant = (suma % 10, suma / 10)
                l2 = l2.next

            if l1.next is None and l2 is None and remnant:
                l1.next = ListNode(remnant)
                remnant = 0

            if l1.next is None:
                l1.next, l2 = (l2, None)

            l1 = l1.next


        return l1_head

