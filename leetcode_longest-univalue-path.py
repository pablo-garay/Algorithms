class Solution(object):  # One pass. Optimal as need to traverse whole tree in the worst case. Runtime beats 91.91 % of python submissions.
    def longestUnivaluePath(self, root):
        self.longest = 0
        self.dfs(root)

        return max(self.longest - 1, 0)

    def dfs(self, curr):
        if curr is None:
            return 0

        count_left = self.dfs(curr.left)
        count_right = self.dfs(curr.right)

        if count_left == 0 and count_right == 0:
            curr_count = 1

        elif count_left == 0:
            if curr.val == curr.right.val:
                curr_count = count_right + 1
            else:
                curr_count = 1

        elif count_right == 0:
            if curr.val == curr.left.val:
                curr_count = count_left + 1
            else:
                curr_count = 1

        else:
            if curr.val != curr.left.val and curr.val != curr.right.val:
                curr_count = 1
            elif curr.val == curr.right.val == curr.left.val:
                if self.longest < count_left + count_right + 1:
                    self.longest = count_left + count_right + 1
                curr_count = max(count_left + 1, count_right + 1)

            elif curr.val == curr.right.val:
                curr_count = count_right + 1
            elif curr.val == curr.left.val:
                curr_count = count_left + 1

        if curr_count > self.longest:
            self.longest = curr_count

        return curr_count
