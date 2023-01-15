# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return
        n = len(preorder)
        return self.process(preorder,0,n-1,inorder,0,n-1)
    def process(self, preorder,l1,r1,inorder,l2,r2):
        if l2 == r2:
            return TreeNode(inorder[l2])
        if l1 > r1 or l2 > r2:
            return
        node = TreeNode(preorder[l1])
        index = inorder.index(node.val)
        leftRest = index - l2
        node.left = self.process(preorder,l1+1,l1+leftRest,inorder,l2,index-1)
        node.right = self.process(preorder,l1+leftRest+1,r1,inorder,index+1,r2)
        return node
