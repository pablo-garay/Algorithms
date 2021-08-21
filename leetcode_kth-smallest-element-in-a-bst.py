class Solution(object):  # Time complexity: Linear (stops search/traversing BST when kth elem is found). Optimal as need to visit each elem in BST in worst case. Faster than 99.67%
    def kthSmallest(self, root, k):
        self.res = None
        self.inorder(root, k, -1)
        return self.res

    def inorder(self, node, k, up_num):
        if node is None:
            return -1

        left_num = self.inorder(node.left, k, up_num)
        if left_num == k: return k

        if left_num == -1 and up_num == -1:
            curr_num = 1
        elif left_num == -1 and up_num != -1:
            curr_num = up_num + 1
        else:  # left_num != -1
            curr_num = left_num + 1

        if curr_num == k:
            self.res = node.val
            return k

        return max(self.inorder(node.right, k, curr_num), curr_num)
