# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):  # Time complexity: O(n)
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        index_root = inorder.index(postorder.pop())
        root = TreeNode(inorder[index_root])

        root.right = self.buildTree(inorder[index_root + 1:], postorder)
        root.left = self.buildTree(inorder[:index_root], postorder)

        return root


print Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print Solution().buildTree(inorder = [-1], postorder = [-1])
