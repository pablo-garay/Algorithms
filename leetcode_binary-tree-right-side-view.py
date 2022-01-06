class Solution(object):  # Time: O(n) - optimal as need to traverse all n nodes in worst case. Space: height of tree
    def rightSideView(self, root):
        self.heights = set()
        return self.visit(root, 1, [])
        
    def visit(self, node, height, partial):
        if node is None:
            return
        
        if height not in self.heights:
            partial.append(node.val)
            self.heights.add(height)
        
        self.visit(node.right, height + 1, partial)
        self.visit(node.left, height + 1, partial)
        return partial
