class Solution(object):  # Time: O(n) for n elements in linked list - optimal as need to visit all in worst case
    def reorderList(self, head):  # RECURSIVE VERSION
        if head is None or head.next is None or head.next.next is None: return
        self.f(head, head)

    def f(self, left, right):
        if right.next is None:
            left_next = left.next
            left.next, right.next = (right, left_next)
            return left_next

        left = self.f(left, right.next)
        if left is None:
            return None
        if left == right or left.next == right:
            right.next = None
            return None

        left_next = left.next
        left.next, right.next = (right, left_next)
        return left_next

    # def reorderList(self, head):  # ITERATIVE VERSION
    #     if head is None: return
    #     left = head
    #     stack = []
    #
    #     while left:
    #         stack.append(left)
    #         left = left.next
    #
    #     left, right = (head, stack.pop())
    #     while left != right and left.next != right:
    #         left_next = left.next
    #         left.next, right.next = (right, left_next)
    #         left, right = (left_next, stack.pop())
    #
    #     right.next = None
