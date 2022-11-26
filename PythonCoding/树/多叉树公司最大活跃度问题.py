class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestCompanyPartyMember(self, root):
        if not root:
            return 0
        return max(self.rec(root))

    def rec(self, node):
        if not node:
            return [0, 0]
        left = self.rec(node.left)
        right = self.rec(node.right)

        come = left[1] + right[1] + 1
        notcome = max(left[0], left[1]) + max(right[0], right[1])
        return [come, notcome]


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
print(so.largestCompanyPartyMember(t1))


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []


class Solution:
    def largestCompanyPartyMember(self, root):
        if not root:
            return 0
        return max(self.rec(root))

    def rec(self, node):
        come = node.val
        notcome = 0
        for child in node.children:
            status = self.rec(child)
            come += status[1]
            notcome += max(status[0], status[1])
        return [come, notcome]