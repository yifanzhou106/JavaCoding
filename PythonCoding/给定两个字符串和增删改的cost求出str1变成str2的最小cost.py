class Solution:
    def minCostUpdateStr(self, str1, str2, ic, dc, rc):
        if str1 == str2:
            return 0
        return self.process(str1, str2, ic, dc, rc, len(str1) - 1, len(str2) - 1)

    def process(self, str1, str2, ic, dc, rc, m, n):
        if m < 0:
            return n * ic
        if n < 0:
            return m * dc
        if n == 0 and m == 0:
            return rc if str1[0] != str2[0] else 0
        if str1[m] == str2[n]:
            return self.process(str1, str2, ic, dc, rc, m - 1, n - 1)

        p1 = self.process(str1, str2, ic, dc, rc, m - 1, n) + dc
        p2 = self.process(str1, str2, ic, dc, rc, m, n - 1) + ic
        p3 = self.process(str1, str2, ic, dc, rc, m - 1, n - 1) + rc
        return min(p1, p2, p3)

    def minCostUpdateStrDp(self, str1, str2, ic, dc, rc):
        m = len(str1)
        n = len(str2)
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        dp[0][0] = rc if str1[0] != str2[0] else 0

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + ic
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + dc

        for i in range(1, m):
            for j in range(1, n):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + dc, dp[i][j - 1] + ic, dp[i - 1][j - 1] + rc)
        return dp[-1][-1]


so = Solution()
str1 = 'abc'
str2 = 'adc'
print(so.minCostUpdateStr(str1, str2, 5, 3, 2))
print(so.minCostUpdateStrDp(str1, str2, 5, 3, 2))

str1 = 'abc'
str2 = 'adc'
print(so.minCostUpdateStr(str1, str2, 5, 3, 100))
print(so.minCostUpdateStrDp(str1, str2, 5, 3, 100))

str1 = 'abc'
str2 = 'abc'
print(so.minCostUpdateStr(str1, str2, 5, 3, 2))
print(so.minCostUpdateStrDp(str1, str2, 5, 3, 2))