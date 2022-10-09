class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Item:
    def __init__(self, node=None, isFoundA=False, isFoundB=False):
        self.node = node
        self.isFoundA = isFoundA
        self.isFoundB = isFoundB


class Solution:
    def problem(self, root, a, b):
        if not root:
            return None
        return self.process(root, a, b).node

    def process(self, node, a, b):
        if not node:
            return Item(None, False, False)
        isFoundA = False
        isFoundB = False
        if node is a:
            isFoundA = True
        if node is b:
            isFoundB = True

        left = self.process(node.left, a, b)
        right = self.process(node.right, a, b)

        isFoundA = isFoundA or left.isFoundA or right.isFoundA
        isFoundB = isFoundB or left.isFoundB or right.isFoundB
        if left.node:
            return left
        if right.node:
            return right
        if isFoundA and isFoundB:
            return Item(node, True, True)
        return Item(None, isFoundA, isFoundB)


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
print(so.problem(t1, t8, t9).val)