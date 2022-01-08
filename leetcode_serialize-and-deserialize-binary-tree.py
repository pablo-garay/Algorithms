# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:  # Runtime: 124 ms, faster than 64.35%. Memory Usage: less than 95.69%
    def serialize(self, root):  # O(n) where n is num nodes - optimal as need to traverse whole tree
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = "[" + str(root.val) + "]" + self.serialize(root.left) + self.serialize(root.right) if root is not None else "#"
        return s

    def deserialize(self, data):  # O(len(data)) - linear time
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.index = 0
        return self.parse_deserialize(data)

    def parse_deserialize(self, data):
        if data[self.index] == "#":
            self.index += 1
            return None

        if data[self.index] == "[":
            self.index += 1
            token = ""
            
            while data[self.index] != "]":
                token += data[self.index]
                self.index += 1

            node = TreeNode(int(token))
            self.index += 1
            node.left = self.parse_deserialize(data)
            node.right = self.parse_deserialize(data)

            return node
