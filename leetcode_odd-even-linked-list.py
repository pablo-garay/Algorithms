class Solution(object): # Runtime 20 ms Beats 97% Memory Beats 97%
    def oddEvenList(self, head): # Time: O(n) Space: O(1) - Optimal as need to traverse whole linked list in worst case (also: one pass only)
        if head is None or head.next is None: return head

        first_link = head.next  # this is where the circling back should occur
        odd = False  # track odd or even num of nodes
        node = head

        while node.next.next is not None:  # O(n)
            visit_next = node.next
            node.next = node.next.next
            node = visit_next
            odd = not odd
        
        if odd:
            node.next.next = first_link
            node.next = None
        else: # even 
            node.next = first_link
        
        return head
