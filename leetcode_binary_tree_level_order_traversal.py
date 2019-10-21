# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):  # time complexity: O(n) - n nodes have to be visited in the worst case
    def levelOrder(self, root):
        output = []

        if root is None:
            return output

        queue = deque([(root, 0)])  # init

        while queue:  # while queue not empty
            node, node_level = queue.popleft()  # get next elem in queue

            if len(output) < node_level + 1:
                output.append([])

            output[node_level].append(node.val)

            if node.left is not None:
                queue.append((node.left, node_level + 1))

            if node.right is not None:
                queue.append((node.right, node_level + 1))

        return output
