"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):  # BFS: Time complexity is linear. Optimal as need to visit each node once in worst case.
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return

        frontier = [root]

        while frontier:
            next_frontier = []

            for i in xrange(len(frontier)):
                if i < len(frontier) - 1:
                    frontier[i].next = frontier[i + 1]
                else:
                    frontier[i].next = None

                if frontier[i].left is not None:
                    next_frontier.append(frontier[i].left)
                if frontier[i].right is not None:
                    next_frontier.append(frontier[i].right)

            frontier = next_frontier

        return root

    ## O(1) space solution - linear in time
    # def connect(self, root):
    #     while root and root.left:
    #         next = root.left
    #         while root:
    #             root.left.next = root.right
    #             root.right.next = root.next and root.next.left
    #             root = root.next
    #         root = next

