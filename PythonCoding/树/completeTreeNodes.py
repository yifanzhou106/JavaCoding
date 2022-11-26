# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        return self.rec(root, 1, self.mostLeftLevel(root, 1))

    def rec(self, root, level, h):
        if h == level:
            return 1
        if self.mostLeftLevel(root.right, level + 1) == h:
            return (1 << (h - level)) + self.rec(root.right, level + 1, h)
        else:
            return (1 << (h - level - 1)) + self.rec(root.left, level + 1, h)

    def mostLeftLevel(self, node, level):
        while node:
            node = node.left
            level += 1
        return level - 1
