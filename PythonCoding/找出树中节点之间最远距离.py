class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLargestDistanceInTree(self, root):
        if not root:
            return 0
        return self.rec(root)[0]

    def rec(self, node):
        if not node:
            return [0, 0]
        left = self.rec(node.left)
        right = self.rec(node.right)

        cur = left[1] + right[1] + 1
        cur = max(cur, left[0], right[0])
        return [cur, max(left[1], right[1]) + 1]


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
print(so.findLargestDistanceInTree(t1))