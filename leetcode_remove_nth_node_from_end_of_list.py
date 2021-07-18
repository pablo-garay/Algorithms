class Solution(object):  # O(n) as each node in linked list is traversed once only (optimal as need to visit each once at least) - only one pass
    count = 0

    def removeNthFromEnd(self, head, n):
        return self.checkNode(head, n)

    def checkNode(self, node, n):
        if node is None:
            return None

        next_node = self.checkNode(node.next, n)

        if node.next is None:
            self.count = 1
        else:
            self.count += 1

        if self.count == n:
            return node.next

        node.next = next_node

        return node


print Solution().removeNthFromEnd(head=[1, 2, 3, 4, 5], n=2)
