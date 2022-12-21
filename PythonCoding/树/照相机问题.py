class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info:
    # 认为node一下的节点都已经是covered状态
    # 每个node假设有三种状态，并在这三种状态下各自求最小照相机数
    # uncovered, 当前节点没有覆盖到，但是子节点都是已经覆盖了的状态
    # coveredWithCamera, 当前节点覆盖到了，并且照相机就在上面，子节点可能覆盖，也可能没覆盖
    # coveredNoCamera， 当前节点覆盖到了，但没有相机，子节点都是已经覆盖了的状态，并且至少有一个子节点有相机
    def __init__(self, uncovered, coveredWithCamera, coveredNoCamera):
        self.uncovered = uncovered
        self.coveredWithCamera = coveredWithCamera
        self.coveredNoCamera = coveredNoCamera

# 想用最少的照相机来覆盖整个tree，每个相机可以覆盖当前节点的所有父子节点
class Solution:

    def cameraTree(self, root):
        info = self.process(root)
        return min(info.uncovered, info.coveredWithCamera, info.coveredNoCamera)

    def process(self, node):
        if not node:
            return Info(float('inf'), float('inf'), 0)

        left = self.process(node.left)
        right = self.process(node.right)

        # 如果这个节点uncovered, 只有左右都是coveredNoCamera才可能
        uncovered = left.coveredNoCamera + right.coveredNoCamera

        # 如果这个节点coveredNoCamera：
        p1 = left.coveredWithCamera + right.coveredWithCamera
        p2 = left.coveredNoCamera + right.coveredWithCamera
        p3 = left.coveredWithCamera + right.coveredNoCamera
        coveredNoCamera = min(p1, p2, p3)

        # 如果这个节点coveredWithCamera：
        minLeft = min(left.uncovered, left.coveredWithCamera, left.coveredNoCamera)
        minRight = min(right.uncovered, right.coveredWithCamera, right.coveredNoCamera)
        coveredWithCamera = minLeft + minRight + 1
        return Info(uncovered, coveredWithCamera, coveredNoCamera)


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

print(so.cameraTree(t1))