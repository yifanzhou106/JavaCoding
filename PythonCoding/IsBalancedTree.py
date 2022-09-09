class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanceTree(self, root):
        if not root:
            return True
        diff = self.rec(root)
        return True if self.rec(root) != -1 else False

    def rec(self, node):
        if not node:
            return 0
        left = self.rec(node.left)
        right = self.rec(node.right)
        if left == -1 or right == -1:
            return -1
        return max(left,right) + 1 if abs(left-right) < 2 else -1


so = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t4.left = t8

print(so.isBalanceTree(t1))

w1 = TreeNode(1)
w2 = TreeNode(2)
w3 = TreeNode(3)
w4 = TreeNode(4)
w5 = TreeNode(5)
w6 = TreeNode(6)
w7 = TreeNode(7)
w8 = TreeNode(8)

w1.left = w2
w1.right = w3
w2.left = w4
w3.left = w6
w3.right = w7
w4.right = w8
print(so.isBalanceTree(w1))