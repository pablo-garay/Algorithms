class Solution(object):  # Time: O(n) Space: O(n)
    def hasCycle(self, head):
        visited = set()

        while head:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return True

        return False
