class Solution(object):
    def reverseOddLevels(self, root):  # Runtime 849 ms Beats 98.48%
        if root is None: return None
        return self.bfs(root)
    
    def bfs(self, root):  # Time: O(n) for n nodes in the tree (each node visited once). Optimal as need to traverse whole tree in worst case
        is_odd_level = False  # Space: O(n / 2) | Beats 77.27%
        frontier = [root]

        while frontier:
            next_frontier = []

            for node in frontier:
                if node.left is not None: next_frontier.append(node.left)
                if node.right is not None: next_frontier.append(node.right)

            if is_odd_level:
                for i in xrange(len(frontier) // 2):
                    frontier[i].val, frontier[-1 - i].val = (frontier[-1 - i].val, frontier[i].val)

            frontier = next_frontier
            is_odd_level = not is_odd_level
        
        return root
