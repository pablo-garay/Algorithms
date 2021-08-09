from collections import Counter

class Solution(object):  # O(n) - optimal as need to traverse each node in worst case
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        roots = {_ for _ in xrange(n)}
        incoming = Counter()

        for node in leftChild + rightChild:
            roots.discard(node)
            incoming[node] += 1
            if node != -1 and incoming[node] > 1:
                return False

        if len(roots) != 1:
            return False

        self.visited = set()
        self.dfs(roots.pop(), leftChild, rightChild)

        if len(self.visited) == n:
            return True

        return False

    def dfs(self, node, leftChild, rightChild):
        if node != -1 and node not in self.visited:
            self.visited.add(node)
            self.dfs(leftChild[node], leftChild, rightChild)
            self.dfs(rightChild[node], leftChild, rightChild)







print Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])  # True
print Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])  # False
print Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])  # False
print Solution().validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1])  # False
print Solution().validateBinaryTreeNodes(n = 1, leftChild = [-1], rightChild = [-1])  # True
print Solution().validateBinaryTreeNodes(n = 1, leftChild = [-1], rightChild = [0])  # False
print Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,-1], rightChild = [-1,-1])  # True
print Solution().validateBinaryTreeNodes(4, [1,0,3,-1], [-1,-1,-1,-1])  # False
print Solution().validateBinaryTreeNodes(4, [1,3,0,-1], [-1,-1,-1,-1])  # True
