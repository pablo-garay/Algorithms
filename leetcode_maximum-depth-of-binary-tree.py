class Solution(object):  # Time: O(n). Space: O(1)
    def maxDepth(self, root):
        self.max_depth = 0
        self.dfs(root, 1)
        return self.max_depth

    def dfs(self, node, curr):
        if node is None: return
        self.max_depth = max(self.max_depth, curr)
        self.dfs(node.left, curr + 1)
        self.dfs(node.right, curr + 1)
