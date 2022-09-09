class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def morrisInorder(self, root):
        if not root:
            return

        cur1 = root
        while cur1:
            cur2 = cur1.left
            if cur2:
                while cur2.right and cur2.right != cur1:
                    cur2 = cur2.right
                if not cur2.right:
                    cur2.right = cur1
                    cur1 = cur1.left
                    continue

                elif cur2.right == cur1:
                    print(cur1.val)
                    cur2.right = None
            else:
                print(cur1.val)
            cur1 = cur1.right


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

so.morrisInorder(t1)