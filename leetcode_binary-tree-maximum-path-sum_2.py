class Solution(object):  # Runtime: 72 ms, faster than 94.04%. Memory Usage: less than 98.67%
    def maxPathSum(self, root):  # Time: O(n) for n nodes in tree - optimal as need to traverse all elems in worst case. Space: O(1)
        self.maxSum = float("-inf")
        self.calculate(root)
        return self.maxSum

    def calculate(self, root):
        if root is None: return 0

        left_path_opt = max(self.calculate(root.left), 0); right_path_opt = max(self.calculate(root.right), 0)
        self.maxSum = max(self.maxSum, root.val + left_path_opt + right_path_opt)

        return root.val + max(left_path_opt, right_path_opt)
