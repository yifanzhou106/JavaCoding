# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.process(root.left,root.right)

    def process(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False

        return self.process(left.left,right.right) and self.process(left.right,right.left)