class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSameSubTree(self, n, m):
        if not n or not m:
            return False
        nc = self.toCharList(n)
        mc = self.toCharList(m)
        print(nc)
        print(mc)
        next = self.findNext(mc)
        print(next)

        ni = 0
        mi = 0
        while ni < len(nc) and mi < len(mc):
            if nc[ni] == mc[mi]:
                ni += 1
                mi += 1
            elif next[mi] == -1:
                ni += 1
            else:
                mi = next[mi]
        return mi == len(mc)

    def toCharList(self, node):
        if not node:
            return '#'

        left = self.toCharList(node.left)
        right = self.toCharList(node.right)

        return left + '!' + str(node.val) + '!' + right

    def findNext(self, str):
        if len(str) == 1:
            return [-1]
        res = [None for _ in range(len(str))]
        res[0] = -1
        res[1] = 0
        pos = 2
        cn = 0
        while pos < len(str):
            if str[pos - 1] == str[cn]:
                cn += 1
                res[pos] = cn
                pos += 1
            elif cn > 0:
                cn = res[cn]
            else:
                res[pos] = 0
                pos += 1
        return res


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
print(so.findSameSubTree(t1, t3))