# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    @staticmethod
    def sort(head, length):
        if length == 1:
            return head
        else:
            mid_length = length / 2

            node = head
            for i in xrange(1, mid_length):
                node = node.next

            left, right = head, node.next
            node.next = None

            left = Solution.sort(left, mid_length)
            right = Solution.sort(right, length - mid_length)

            if left.val <= right.val:
                head = left
                left = left.next
            else:
                head = right
                right = right.next

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


    def sortList(self, head):
        if head is None: return head

        length = 0
        node = head

        while node is not None:
            length += 1
            node = node.next

        return Solution.sort(head, length)

