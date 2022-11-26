class Solution:
    def differentBST(self, N):
        if N < 1:
            return 0
        dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
        return self.process(N, 1, N, dp)

    def process(self, N, i, j, dp):
        if i >= j:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]

        if i >= j:
            dp[i][j] = 1
            return dp[i][j]
        res = 0

        for k in range(i, j + 1):
            left = self.process(N, i, k - 1, dp)
            right = self.process(N, k + 1, j, dp)
            res += left * right
        dp[i][j] = res
        return dp[i][j]


so = Solution()
# print(so.differentBST(2))
# print(so.differentBST(3))
print(so.differentBST(4))