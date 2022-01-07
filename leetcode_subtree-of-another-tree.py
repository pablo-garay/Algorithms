# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        return self.compare(root, subRoot, True)

    def compare(self, root, subRoot, fromTheStart):
        if root is None and subRoot is None:
            return True
        elif (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        
        if root.val == subRoot.val and self.compare(root.left, subRoot.left, False) and self.compare(root.right, subRoot.right, False):
            return True

        if fromTheStart:
            if root.left is not None and self.compare(root.left, subRoot, True):
                return True
            elif root.right is not None and self.compare(root.right, subRoot, True):
                return True

        return False
