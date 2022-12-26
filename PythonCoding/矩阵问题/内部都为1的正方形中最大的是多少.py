# 给定二维数组，其中值不是0就是1，其中内部都为1的正方形中最大的是多少
# dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
class Solution:
    def largestValidSquareInMetrix(self, M):
        maxSpace = 0
        dp = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            dp[i][0] = M[i][0]
        for j in range(len(M[0])):
            dp[0][j] = M[0][j]

        for i in range(1, len(M)):
            for j in range(1, len(M[0])):
                if M[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSpace = max(maxSpace, dp[i][j] * dp[i][j])

        return maxSpace


so = Solution()
M = [[0, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]
print(so.largestValidSquareInMetrix(M))
