class Solution(object):  # Time: O(n) for n elements in linked list - optimal as need to visit all nodes in worst case
    def deleteMiddle(self, head):
        if head is None or head.next is None: return None
        self.visit(None, head, 0, 1)
        return head

    def visit(self, prev, curr, num_node, total_nodes):
        if curr.next is None:
            if num_node == total_nodes / 2: prev.next = curr.next
            return total_nodes

        total_nodes = self.visit(curr, curr.next, num_node + 1, total_nodes + 1)
        if num_node == total_nodes / 2: prev.next = curr.next

        return total_nodes
