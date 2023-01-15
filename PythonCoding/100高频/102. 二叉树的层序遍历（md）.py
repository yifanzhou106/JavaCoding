# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = [(root, 0)]
        preLevel = 0
        tmp = []
        while q:
            node, level = q.pop(0)
            if level == preLevel:
                tmp.append(node.val)
            else:
                res.append(tmp[:])
                tmp = [node.val]
                preLevel = level
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        if tmp:
             res.append(tmp[:])
        return res
