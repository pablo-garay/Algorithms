class Solution(object):  # Runtime: 20 ms, faster than 93.27%
    # Recursive. Time: O(n) for n elems in linked list - optimal as need to traverse all elems. Space: O(1)
    # def reverseList(self, head):
    #     return self.revert(head, None)
    #
    # def revert(self, curr, prev):
    #     if curr is None:
    #         return prev
    #
    #     next = curr.next
    #     curr.next = prev
    #
    #     return self.revert(next, curr)

    # Iterative. Time: O(n) for n elems in linked list - optimal as need to traverse all elems. Space: O(1)
    def reverseList(self, head):
        prev, curr = None, head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev, curr = (curr, next)

        return prev
