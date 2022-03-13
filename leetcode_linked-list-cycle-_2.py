class Solution(object):  # Time: O(n) Space: O(1)  # Runtime: 44 ms, faster than 92.43%
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
            if slow == fast: return True

        return False
