class Solution:
    # N, nums from 1 to N
    # p, steps
    # k, target position
    # m, start position
    def findWaysToKInArray(self, N, p, k, m):
        if N < 2 or p < 0 or k < 1 or k > N or m < 1 or m > N:
            return 0

        if p == 0:
            return 1 if k == m else 0
        res = 0

        if m == 1:
            res = self.findWaysToKInArray(N, p - 1, k, m + 1)
        elif m == N:
            res = self.findWaysToKInArray(N, p - 1, k, m - 1)
        else:
            res = self.findWaysToKInArray(N, p - 1, k, m + 1) + self.findWaysToKInArray(N, p - 1, k, m - 1)
        return res

    def findWaysToKInArrayDP(self, N, p, k, m):
        dp = [[0 for _ in range(N + 1)] for _ in range(p + 1)]
        dp[0][k] = 1

        for i in range(1, p + 1):
            for j in range(1, N + 1):
                if j == N:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        print(dp)
        return dp[-1][m]


so = Solution()
print(so.findWaysToKInArray(10, 3, 6, 9))
print(so.findWaysToKInArrayDP(10, 3, 6, 9))