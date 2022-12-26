class Node:
    def __init__(self, val, index):
        self.val = val
        self.indexs = [index]


# 给定二维数组，其中值不是0就是1，其中内部都为1的子矩阵中最大的是多少
# 通过遍历以每一行为底的矩阵们，用单调栈来求最大space
class Solution:
    def largestValidRectangleInMetrix(self, M):
        maxSpace = 0
        recSum = [0 for _ in range(len(M[0]))]
        for i in range(len(M)):
            # 先处理矩阵的累加和，当M[i][j] == 0说明这一行上的j列没有以i为底的
            for j in range(len(M[0])):
                recSum[j] = 0 if M[i][j] == 0 else recSum[j] + 1

            # 求出当前矩阵的最大矩阵和
            maxSpace = max(maxSpace, self.process(recSum))
            print(recSum, maxSpace)

        return maxSpace

    def process(self, arr):
        stack = []
        maxSpace = 0
        for i in range(len(arr)):
            while stack and arr[i] < stack[-1].val:
                node = stack.pop()
                maxSpace = max(maxSpace, (i - node.indexs[0]) * node.val)
            if stack and stack[-1].val == arr[i]:
                stack[-1].indexs.append(i)
            stack.append(Node(arr[i], i))
        while stack:
            if len(stack) > 1:
                node = stack.pop()
                maxSpace = max(maxSpace, (node.indexs[-1] - stack[-1].indexs[-1]) * node.val)
            else:
                node = stack.pop()
                maxSpace = max(maxSpace, (node.indexs[-1] - node.indexs[0]) * node.val)
        return maxSpace


so = Solution()
M = [[0, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]
print(so.largestValidRectangleInMetrix(M))
