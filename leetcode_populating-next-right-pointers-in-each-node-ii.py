class Solution(object):  # BFS: Time complexity is linear. Optimal as need to visit each node once in worst case.
    def connect(self, root):  # Runtime: 32 ms, faster than 98.01%
        if root == None: return

        frontier = [root]

        while frontier:
            next_frontier = []

            for i in xrange(len(frontier)):
                if i < len(frontier) - 1:
                    frontier[i].next = frontier[i + 1]
                else:
                    frontier[i].next = None

                if frontier[i].left is not None:
                    next_frontier.append(frontier[i].left)
                if frontier[i].right is not None:
                    next_frontier.append(frontier[i].right)

            frontier = next_frontier

        return root
