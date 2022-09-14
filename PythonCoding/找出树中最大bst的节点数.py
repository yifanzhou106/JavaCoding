class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLargestBST(self, root):
        if not root:
            return
        node, bstCount, _min, _max = self.rec(root)
        print(node.val, _min, _max)
        return bstCount

    def rec(self, node):
        if not node:
            return (None, 0, float('inf'), -float('inf'))
        leftBstNode, leftMaxBst, leftMin, leftMax = self.rec(node.left)
        rightBstNode, rightMaxBst, rightMin, rightMax = self.rec(node.right)

        if leftBstNode is node.left and rightBstNode is node.right and leftMax < node.val and rightMin > node.val:
            return (
            node, leftMaxBst + rightMaxBst + 1, min(leftMin, node.val, rightMin), max(rightMax, leftMax, node.val))
        elif leftMaxBst > rightMaxBst:
            return (leftBstNode, leftMaxBst, leftMin, leftMax)
        else:
            return (rightBstNode, rightMaxBst, rightMin, rightMax)


so = Solution()
t1 = TreeNode(6)
t2 = TreeNode(10)
t3 = TreeNode(4)
t4 = TreeNode(9)
t5 = TreeNode(11)
t6 = TreeNode(2)
t7 = TreeNode(5)
t8 = TreeNode(3)
t9 = TreeNode(7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t6.right = t8
t7.right = t9
print(so.findLargestBST(t1))