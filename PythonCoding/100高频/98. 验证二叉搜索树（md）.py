# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cur1 = root
        pre = None
        while cur1:
            cur2 = cur1.left
            if cur2:
                while cur2.right and cur2.right != cur1:
                    cur2 = cur2.right
                if not cur2.right:
                    cur2.right = cur1
                    cur1 = cur1.left
                    continue
                else:
                    cur2.right = None
            if pre != None and pre >= cur1.val:
                return False
            pre = cur1.val
            cur1 = cur1.right
        return True

