#!/usr/bin/env python
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data);
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data);
    return node

"""
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None
"""

def isPresent (root,val):  # complexity: O(log n) where n is the num of elems in BST
    # return 1 or 0 depending on whether the element is present in the tree or not
    if root is None:
        return 0

    if val == root.value:
        return 1
    elif val < root.value:
        return isPresent(root.left, val)
    else:
        return isPresent(root.right, val)
    return 0


_a = None
_a_size = int(raw_input())
_a_i=0

while _a_i < _a_size:
    _a_item = int(raw_input())
    _a = _insert_node_into_binarysearchtree(_a, _a_item)
    _a_i += 1

q = int(raw_input())
i = 0

while i < q:
    _b = int(raw_input())
    _result = isPresent (_a , _b );
    print _result
    i += 1