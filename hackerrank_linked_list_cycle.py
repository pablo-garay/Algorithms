"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):  # Time: O(n) Space: O(n)
    curr = head
    visited = set()

    while curr is not None:
        # print("Curr", curr)
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next

    return False


def has_cycle2(head):  # Time: O(n) Space: O(1)
    slow = fast = head

    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
        if slow == fast: return False

    return True
