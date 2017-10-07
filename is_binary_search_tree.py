""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

######### INEFFICIENT SOLUTION ##############
# def check_less_than(data, node):
#     if node is not None:
#         if data < node.data:
#             return check_less_than(data, node.left) and check_less_than(data, node.right)
#     else:
#         return True
#
#
# def check_greater_than(data, node):
#     if node is not None:
#         if data > node.data:
#             return check_greater_than(data, node.left) and check_greater_than(data, node.right)
#     else:
#         return True
#
#
# def checkBST(root):
#     if root is None:
#         return True
#     else:  # root is not None
#         if check_greater_than(root.data, root.left) and check_less_than(root.data, root.right):
#             return checkBST(root.left) and checkBST(root.right)
#
#     return False

MIN = float("-inf")
MAX = float("inf")

def isValidBST(node, mini, maxi):
    if node is None:
        return True
    else:
        if node.data > mini and node.data < maxi and isValidBST(node.left, mini, node.data) and isValidBST(node.right, node.data, maxi):
            return True
        else:
            return False

def checkBST(root):
    isValidBST(root, MIN, MAX)
