class Solution:
    def maxIncreasePathInMatrix(self, M):
        maxPath = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                val = self.process(M, i, j)
                maxPath = max(maxPath, val)
        return maxPath

    def process(self, M, i, j):
        if i < 0 or j < 0 or i == len(M) or j == len(M[0]):
            return -1
        p1 = 0
        if i > 0 and M[i][j] < M[i - 1][j]:
            p1 = self.process(M, i - 1, j)
        p2 = 0
        if i < len(M) - 1 and M[i][j] < M[i + 1][j]:
            p2 = self.process(M, i + 1, j)
        p3 = 0
        if j > 0 and M[i][j] < M[i][j - 1]:
            p3 = self.process(M, i, j - 1)
        p4 = 0
        if j < len(M[0]) - 1 and M[i][j] < M[i][j + 1]:
            p1 = self.process(M, i, j + 1)

        return 1 + max(p1, p2, p3, p4)

# 傻缓存
    def maxIncreasePathInMatrixDP(self, M):
        maxPath = 0
        dp = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                val = self.process2(M, i, j, dp)
                maxPath = max(maxPath, val)
        return maxPath

    def process2(self, M, i, j, dp):
        if i < 0 or j < 0 or i == len(M) or j == len(M[0]):
            return -1
        if dp[i][j] != 0:
            return dp[i][j]
        p1 = 0
        if i > 0 and M[i][j] < M[i - 1][j]:
            p1 = self.process(M, i - 1, j)
        p2 = 0
        if i < len(M) - 1 and M[i][j] < M[i + 1][j]:
            p2 = self.process(M, i + 1, j)
        p3 = 0
        if j > 0 and M[i][j] < M[i][j - 1]:
            p3 = self.process(M, i, j - 1)
        p4 = 0
        if j < len(M[0]) - 1 and M[i][j] < M[i][j + 1]:
            p1 = self.process(M, i, j + 1)
        dp[i][j] = 1 + max(p1, p2, p3, p4)
        return dp[i][j]


so = Solution()
arr = [[5, 4, 3], [3, 1, 2], [2, 1, 3]]
print(so.maxIncreasePathInMatrix(arr))
print(so.maxIncreasePathInMatrixDP(arr))
