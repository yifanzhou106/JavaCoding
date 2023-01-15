# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
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
        flag = False
        while q:
            node, level = q.pop(0)
            if level == preLevel:
                tmp.append(node.val)
            else:
                if not flag:
                    res.append(tmp[:])
                else:
                    res.append(tmp[::-1])
                flag = ~flag
                tmp = [node.val]
                preLevel = level
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        if tmp:
            if not flag:
                res.append(tmp[:])
            else:
                res.append(tmp[::-1])
        return res