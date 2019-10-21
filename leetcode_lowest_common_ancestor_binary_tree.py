# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  # O(n) where n: number of tree nodes
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        ret1, ret2 = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if ret1 is not None and ret2 is not None:
            return root

        if (root.val == p.val or root.val == q.val) and (ret1 is not None or ret2 is not None):  # case: node descendant of itself
            return root

        if ret1 is not None:
            return ret1

        if ret2 is not None:
            return ret2

        if root.val == p.val or root.val == q.val:
            return root

        return None



