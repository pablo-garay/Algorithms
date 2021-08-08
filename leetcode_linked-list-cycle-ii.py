class Solution(object):  # Linear time and constant space complexity (two passes at most) - 36 ms, faster than 91.85 %
    def detectCycle(self, head):
        if head is None or head.next is None: return None

        slow = head.next
        fast = head.next.next

        while fast is not None and slow != fast:
            slow = slow.next
            if fast.next is None:
                break
            fast = fast.next.next

        if fast is None:
            return None

        fast = head
        while slow is not None and slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
