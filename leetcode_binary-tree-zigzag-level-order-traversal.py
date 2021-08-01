class Solution(object):  # BFS: linear time. Optimal as need to traverse each node
    def zigzagLevelOrder(self, root):
        if root is None: return []
        frontier = [root]
        left_to_right = False
        res = []

        while frontier:
            res.append([v.val for v in frontier])
            next_frontier = []

            for node in reversed(frontier):
                if left_to_right:
                    if node.left is not None:
                        next_frontier.append(node.left)
                    if node.right is not None:
                        next_frontier.append(node.right)
                else:
                    if node.right is not None:
                        next_frontier.append(node.right)
                    if node.left is not None:
                        next_frontier.append(node.left)

            frontier = next_frontier
            left_to_right = False if left_to_right else True

        return res
