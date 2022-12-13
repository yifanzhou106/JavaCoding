# 从树上任意一点向下走，求和为k的最大路径和
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMaxLengthSumTok(self, root, k):
        map = {}
        map[0] = -1
        self.res = 0
        self.process(root, k, map, 0, 0)
        return self.res

    def process(self, node, k, map, preSum, level):
        if not node:
            return
        curSum = preSum + node.val
        if curSum - k in map:
            self.res = max(self.res, level - map[curSum - k])
        if curSum not in map:
            map[curSum] = level

        self.process(node.left, k, map, curSum, level + 1)
        self.process(node.right, k, map, curSum, level + 1)

        if map[curSum] == level:
            del map[curSum]


so = Solution()
t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t4 = TreeNode(1)
t5 = TreeNode(1)
t6 = TreeNode(2)
t7 = TreeNode(1)
t8 = TreeNode(1)
t9 = TreeNode(1)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.right = t6
t5.right = t7
t7.right = t8
t8.right = t9
print(so.findMaxLengthSumTok(t1, 5))