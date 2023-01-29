# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, totalMax=-float('inf'), maxPath=-float('inf')):
        self.totalMax = totalMax
        self.maxPath = maxPath


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = self.process(root)
        return node.totalMax

    def process(self, node):
        if not node:
            return Node()

        leftNode = self.process(node.left)
        rightNode = self.process(node.right)
        maxPath = max(node.val, leftNode.maxPath + node.val, rightNode.maxPath + node.val)
        totalMax = max(leftNode.totalMax, rightNode.totalMax)
        totalMax = max(totalMax, maxPath, leftNode.maxPath + rightNode.maxPath + node.val)

        return Node(totalMax, maxPath)

