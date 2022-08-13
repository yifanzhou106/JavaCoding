# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if not root:
            return []
        stack.append(root)
        while stack:
            head = stack.pop()
            res.append(head.val)
            if head.left:
                stack.append(head.left)
            if head.right:
                stack.append(head.right)
        return res[::-1]