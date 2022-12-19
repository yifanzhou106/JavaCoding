class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBstErrorNodes(self, root):
        p = []
        cur = root
        pre = None
        while cur:
            cur2 = cur.left
            if cur2:
                while cur2.right and cur2.right != cur:
                    cur2 = cur2.right
                if not cur2.right:
                    cur2.right = cur
                    cur = cur.left
                    continue
                if cur2.right == cur:
                    cur2.right = None
                    if pre.val > cur.val:
                        p.append([pre, cur])
                    pre = cur
                    cur = cur.right
                    continue
            if pre and pre.val > cur.val:
                p.append([pre, cur])
            pre = cur
            cur = cur.right
        if len(p) == 1:
            return [p[0].val]
        else:
            return [p[0][0].val, p[1][1].val]


so = Solution()
t1 = TreeNode(5)
t2 = TreeNode(6)
t3 = TreeNode(3)
t4 = TreeNode(2)
t5 = TreeNode(4)
t6 = TreeNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.right = t6

print(so.findBstErrorNodes(t1))


