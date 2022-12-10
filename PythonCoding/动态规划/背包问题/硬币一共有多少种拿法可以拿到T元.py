class Solution:
    def coinWays(self, C, T):

        return self.process(C, 0, T)

    def process(self, C, i, rest):
        if rest < 0:
            return 0
        if i == len(C):
            return 1 if rest == 0 else 0
        return self.process(C, i, rest - C[i]) + self.process(C, i + 1, rest)

    def coinWays2(self, C, T):
        return self.process2(C, 0, T)

    def process2(self, C, i, rest):
        if i == len(C):
            return 1 if rest == 0 else 0
        zhang = 0
        ways = 0
        while zhang * C[i] <= rest:
            ways += self.process2(C, i + 1, rest - zhang * C[i])
            zhang += 1
        return ways

    def coinWaysDP(self, C, T):
        dp = [[0 for _ in range(T + 1)] for _ in range(len(C) + 1)]
        dp[-1][0] = 1

        for i in range(len(C) - 1, -1, -1):
            for j in range(T + 1):
                dp[i][j] = dp[i + 1][j]
                if j - C[i] >= 0:
                    dp[i][j] += dp[i][j - C[i]]
        return dp[0][T]


so = Solution()
C = [5, 10, 50, 100]
s = 1000
print(so.coinWays(C, s))
print(so.coinWays2(C, s))
print(so.coinWaysDP(C, s))