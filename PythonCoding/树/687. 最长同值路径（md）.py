# 给定一个二叉树的root，返回最长的路径的长度 ，这个路径中的每个节点具有相同值。
# 这条路径可以经过也可以不经过根节点。
#
# 两个节点之间的路径长度由它们之间的边数表示。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class ReturnType:
    def __init__(self, count=0, maxCount=0):
        # 以当前节点向下的最长节点数
        self.count = count
        # 不以当前节点向下的最长节点数
        self.maxCount = maxCount


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.process(root).maxCount - 1

    def process(self, node):
        if not node:
            return ReturnType()

        left = self.process(node.left)
        right = self.process(node.right)

        count = 1

        if node.left and node.val == node.left.val:
            count = left.count + 1

        if node.right and node.val == node.right.val:
            count = max(count, right.count + 1)

        maxCount = max(left.maxCount, right.maxCount, count)
        if node.left and node.val == node.left.val and node.right and node.val == node.right.val:
            maxCount = max(maxCount, left.count + right.count + 1)

        return ReturnType(count, maxCount)

