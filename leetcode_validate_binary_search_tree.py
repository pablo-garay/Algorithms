# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.computeIsValidBST(root, float("-inf"), float("inf"))

    def computeIsValidBST(self, root, min_val, max_val):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.val <= min_val or root.val >= max_val:
                return False

            if root.left:
                if root.left.val >= root.val or not self.computeIsValidBST(root.left, min_val, root.val):
                    return False
            if root.right:
                if root.right.val <= root.val or not self.computeIsValidBST(root.right, root.val, max_val):
                    return False

        return True
