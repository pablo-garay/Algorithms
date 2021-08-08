class Solution(object):  # Complexity | Time: Linear (one pass only, optimal as need to traverse each elem once in worst case). Space: O(1)
    def oddEvenList(self, head):
        if head is None or head.next is None: return head

        curr_odd, curr_even, next_odd = (head, head.next, head.next.next)
        first, second = (curr_odd.next, curr_even.next)

        while second is not None:
            third = second.next
            curr_odd.next, next_odd.next, curr_even.next = (second, first, third)

            if third is not None:
                second = curr_even.next.next
                curr_odd, curr_even, next_odd = (curr_odd.next, third, third.next)
            else:
                break

        return head
