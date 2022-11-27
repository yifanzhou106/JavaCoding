class Solution:
    def maxSumTree(self, root):
        maxSumInTree, maxSumNext = self.process(root)
        return maxSumInTree

    def process(self, node):
        if not node:
            return

        leftSumInTree, leftSumNext = self.process(node.left)
        rightSumInTree, rightSumNext = self.process(node.right)

        p1 = -float('inf')
        if leftSumInTree:
            p1 = leftSumInTree
        p2 = -float('inf')
        if rightSumInTree:
            p2 = rightSumInTree
        p3 = node.val

        p4 = -float('inf')
        if leftSumNext:
            p4 = leftSumNext + node.val
        p5 = -float('inf')
        if rightSumNext:
            p5 = rightSumNext + node.val
        p6 = -float('inf')
        if leftSumNext and rightSumNext:
            p6 = leftSumNext + rightSumNext + node.val
        maxSumInTree = max(p1, p2, p3, p4, p5, p6)
        maxSumNext = max(p3, p4, p5)
        return (maxSumInTree, maxSumNext)