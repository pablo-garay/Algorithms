class Solution(object):  # Runtime: 52 ms, faster than 99.54%
    def isSubtree(self, root, subroot):  # Time: O(mxn) where m, n are num of nodes in trees
        def convert(p):
            return "[" + str(p.val) + "]" + convert(p.left) + convert(p.right) if p else "*"

        return convert(subroot) in convert(root)
