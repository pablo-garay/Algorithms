# Runtime: 11 ms, faster than 96.89%. Memory usage beats 96.48 % of python submissions
class Solution(object):  # Space: O(n) where n=number of tree nodes - optimal as need to traverse whole tree. Space: O(1).
    def invertTree(self, root):
        if root is None: return root
        root.left, root.right = (root.right, root.left)
        self.invertTree(root.left); self.invertTree(root.right)
        return root
