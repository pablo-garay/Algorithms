class Solution(object):  # One pass. Optimal as need to traverse whole tree in the worst case. Runtime beats 91.91 % of python submissions.
    def longestUnivaluePath(self, root):
        self.longest = 0
        self.dfs(root)

        return self.longest

    def dfs(self, curr):
        if curr is None:
            return 0

        count_left = self.dfs(curr.left)
        count_right = self.dfs(curr.right)

        left_side = count_left + 1 if curr.left and curr.val == curr.left.val else 0
        right_side = count_right + 1 if curr.right and curr.val == curr.right.val else 0

        self.longest = max(self.longest, left_side + right_side)
        return max(left_side, right_side)
