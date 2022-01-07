class Solution(object):  # Runtime: 72 ms, faster than 94.04%. Memory Usage: less than 98.67%
    def maxPathSum(self, root):  # Time: O(n) for n nodes in tree - optimal as need to traverse all elems in worst case. Space: O(1)
        self.maxSum = float("-inf")
        self.calculate(root)
        return self.maxSum

    def calculate(self, root):
        if root is None: return 0

        left_path_sum, right_path_sum = (self.calculate(root.left), self.calculate(root.right))
        self.maxSum = max(self.maxSum, root.val + (0 if left_path_sum <= 0 else left_path_sum) + (0 if right_path_sum <= 0 else right_path_sum))

        return root.val + max(0, left_path_sum, right_path_sum)

