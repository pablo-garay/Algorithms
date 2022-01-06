class Solution(object):  # Time: O(n) - optimal as need to traverse all n nodes in worst case. Space: O(1)
    def hasPathSum(self, root, targetSum):
        return self.visit(root, 0, targetSum)

    def visit(self, node, suma, targetSum):
        if node is None: return False
        suma += node.val
        if node.left is None and node.right is None and suma == targetSum: return True

        return bool(self.visit(node.left, suma, targetSum) or self.visit(node.right, suma, targetSum))
