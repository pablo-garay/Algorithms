class Solution(object):  # (DP) Time complexity: Linear, computation on each node takes constant time. Optimal as need to traverse each node in worst case
    def rob(self, root):
        self.memo = {}
        return self.opt(root, 1)

    def opt(self, node, id, children_op=False):
        if node is None:
            return 0

        if children_op:
            return self.opt(node.left, id * 2) + self.opt(node.right, id * 2 + 1)

        if id in self.memo:
            return self.memo[id]

        if node.left is None and node.right is None:  # leaf node
            return node.val

        best = max(self.opt(node.left, id * 2) + self.opt(node.right, id * 2 + 1),
                   node.val + self.opt(node.left, id * 2, children_op=True) + self.opt(node.right, id * 2 + 1, children_op=True))
        self.memo[id] = best

        return best

