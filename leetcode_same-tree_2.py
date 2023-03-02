class Solution(object):  # Runtime 11 ms Beats 95.83%
    def isSameTree(self, p, q):
        return self.serialize(p) == self.serialize(q)
    
    def serialize(self, root):
        return str(root.val) + "]" + self.serialize(root.left) + self.serialize(root.right) if root is not None else "#"
