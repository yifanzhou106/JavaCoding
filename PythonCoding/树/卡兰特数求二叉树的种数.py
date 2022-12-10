class Solution:

    def possibleTreeCounts(self, N):
        if N == 0:
            return 1
        elif N == 1:
            return 1
        res = 0
        for i in range(N):
            res += self.possibleTreeCounts(i) * self.possibleTreeCounts(N - i - 1)
        return res

    def possibleTreeCountsDP(self, N):
        dp = [0 for _ in range(N + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, N + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


so = Solution()

print(so.possibleTreeCounts(15))
print(so.possibleTreeCountsDP(15))