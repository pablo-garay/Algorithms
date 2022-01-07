class Solution(object):
    def isSubtree(self, root, subroot):
        def convert(node):
            return "[" + str(node.val) + "]" + convert(node.left) + convert(node.right) if node else "*"

        converted1, converted2 = (convert(subroot), convert(root))
        print converted1, converted2
        return converted1 in converted2
