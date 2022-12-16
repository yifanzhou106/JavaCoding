class Solution:
    # 有一次钞能力的机会使得某一节点的值变为相反值
    # 每一个位置计算蛇到达M[i][j]时的最大[没用能力的值，用了能力的值]
    # 全局最大值就在其中
    def snack(self, M):
        maxLength = 0
        dp = [[None for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                p = self.process(M, i, j, dp)
                maxLength = max(maxLength, p[0], p[1])
        return maxLength

    # return [没用能力的值，用了能力的值]
    # 因为计算前缀和所以从右向左递归

    def process(self, M, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        if j == 0:
            dp[i][j] = [M[i][0], -M[i][0]]
            return dp[i][j]

        # 筛选左上，左，左下中最大的没用能力的值和用了能力的值
        p = self.process(M, i, j - 1, dp)
        preNoUsed = p[0]
        preUsed = p[1]

        if i > 0:
            p2 = self.process(M, i - 1, j - 1, dp)
            preNoUsed = max(preNoUsed, p2[0])
            preUsed = max(preUsed, p2[1])
        if i < len(M) - 1:
            p3 = self.process(M, i + 1, j - 1, dp)
            preNoUsed = max(preNoUsed, p3[0])
            preUsed = max(preUsed, p3[1])

        # -1 代表从头结点开始，到达不了当前位置
        yes = -1
        no = -1
        # 如果左侧没有用过能力，他可以选择使用，或者不用
        if preNoUsed >= 0:
            no = M[i][j] + preNoUsed
            yes = -M[i][j] + preNoUsed
        # 如果左侧用过能力，他只能不用
        if preUsed >= 0:
            yes = max(yes, M[i][j] + preUsed)
        dp[i][j] = [no, yes]
        return dp[i][j]


so = Solution()
M = [[1, -4, 10], [3, -2, -1], [2, -1, 0], [0, 5, -2]]
print(so.snack(M))
