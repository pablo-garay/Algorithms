class Solution(object):  # Time: O(n) where n is num elems of trees with more nodes. Space: O(1). Runtime: 12 ms, faster than 95.40%
    def isSameTree(self, p, q):
        if p is None and q is None: return True
        if (p is None and q is not None) or (p is not None and q is None): return False

        if p.val != q.val or not self.isSameTree(p.left, q.left) or not self.isSameTree(p.right, q.right):
            return False

        return True
