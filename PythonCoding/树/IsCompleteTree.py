class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root):
        queue = []
        if not root:
            return True
        res = True
        queue.append(root)
        while res and queue:
            needToBeLeaves = False
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.right and not node.left:
                    res = False
                    break
                if needToBeLeaves:
                    if node.left or node.right:
                        res = False
                        break
                if node.left and not node.right:
                    needToBeLeaves = True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res


so = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)

w1 = TreeNode(1)
w2 = TreeNode(2)
w3 = TreeNode(3)
w4 = TreeNode(4)
w5 = TreeNode(5)
w6 = TreeNode(6)
w7 = TreeNode(7)
w8 = TreeNode(8)

k1 = TreeNode(1)
k2 = TreeNode(2)
k3 = TreeNode(3)
k4 = TreeNode(4)
k5 = TreeNode(5)
k6 = TreeNode(6)
k7 = TreeNode(7)
k8 = TreeNode(8)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t4.left = t8
print(so.isCompleteTree(t1))

w1.left = w2
w1.right = w3
w2.left = w4
w2.right = w5
w3.left = w6
w3.right = w7
w4.right = w8
print(so.isCompleteTree(w1))
k1.left = k2
k1.right = k3
k2.left = k4
k3.left = k6
k3.right = k7
k4.left = k8
print(so.isCompleteTree(k1))


