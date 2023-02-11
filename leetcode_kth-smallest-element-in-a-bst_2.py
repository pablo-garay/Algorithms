class Solution(object):  # Runtime 31 ms Beats 93.32%
    def kthSmallest(self, root, k):
        if root is None: return
        self.count = 0
        return self.inorder(root, k)
    
    def inorder(self, root, k):
        if root.left is not None:  # left
            ret = self.inorder(root.left, k)
            if ret is not None: return ret

        self.count += 1  # mid
        if self.count == k: return root.val

        if root.right is not None:  # right
            ret = self.inorder(root.right, k)
            if ret is not None: return ret
        
        return None
