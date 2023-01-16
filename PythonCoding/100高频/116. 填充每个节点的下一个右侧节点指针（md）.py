"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        q = [(root,1)]
        preNode = None
        preLevel = 0
        while q:
            node,level = q.pop(0)
            if preLevel == level:
                preNode.next = node
                preNode = node
            else:
                preNode = node
                preLevel = level

            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        return root