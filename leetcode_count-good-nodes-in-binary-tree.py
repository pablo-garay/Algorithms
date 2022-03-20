class Solution(object):  # Runtime: 296 ms, faster than 83.53%. Memory Usage: less than 85.33%
    def goodNodes(self, root):  # O(n) for n nodes in bin tree. Space: Callstack, O(n) in worst case, O(log n) if balanced binary tree
        self.count = 0
        self.inorder(root, float("-inf"))
        return self.count

    def inorder(self, node, upper):
        if node is None: return
        if node.val >= upper: self.count += 1

        upper = max(upper, node.val)
        self.inorder(node.left, upper); self.inorder(node.right, upper)
