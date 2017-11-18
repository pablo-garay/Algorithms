# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter

hasht = Counter()


def compute_sum(node):
    if node is None:
        return 0

    sum_node = node.val + compute_sum(node.left) + compute_sum(node.right)
    hasht[sum_node] += 1

    return sum_node


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global hasht

        hasht = Counter()
        li_out = []

        compute_sum(root)

        if hasht:
            mode = max(hasht.values())

            for key, val in hasht.iteritems():
                if (val == mode):
                    li_out.append(key)

        return li_out


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            root = stringToTreeNode(line)

            ret = Solution().findFrequentTreeSum(root)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()