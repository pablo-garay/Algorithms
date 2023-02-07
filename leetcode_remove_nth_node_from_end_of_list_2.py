class Solution(object):  # Space: O(1). Time: O(n) - Optimal as need to traverse whole linked list in worst case
    def removeNthFromEnd(self, head, n):  # Runtime 17 ms Beats 82.69%
        node = head; num_nodes = 0
        while node: 
            num_nodes += 1
            node = node.next

        n = num_nodes - n
        if n == 0: return head.next  # handle special case of first node to be removed

        count = 0; node = head
        while count + 1 < n:
            count += 1
            node = node.next
        node.next = node.next.next  # node removal 

        return head
