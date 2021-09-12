from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):  # O(n) solution as we only make one pass in buildTree2
    def buildTree(self, preorder, inorder):
        preorder = deque(preorder)
        return self.buildTree2(preorder, inorder)

    def buildTree2(self, preorder, inorder):
        if not inorder:  # empty list
            return None

        ind_root_val = inorder.index(preorder.popleft())
        root_node = TreeNode(inorder[ind_root_val])

        root_node.left  = self.buildTree2(preorder, inorder[:ind_root_val])
        root_node.right = self.buildTree2(preorder, inorder[ind_root_val + 1:])

        return root_node


print Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
