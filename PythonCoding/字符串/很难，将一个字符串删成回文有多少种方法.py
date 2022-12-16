class Solution:
    # 给定一个字符串，将它删除成回文串的次数是啥
    # 空串不算回文串，
    # ABA 有5种分别是 'A' 'B' 'A' 'AA' 'ABA' 位置不同的当成两种删除方法
    # XXY 有4种

    def findWaysToDelete(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s) - 1):
            dp[i][i + 1] = 3 if s[i] == s[i + 1] else 2

        for i in range(len(s) - 3, -1, -1):
            for j in range(i + 2, len(s)):
                # L不要 R不要 a
                # L要 R不要 b
                # L不要 R要 c
                # L要 R要 d
                # dp[L+1][R] = a + c
                # dp[L][R-1] = a + b
                # dp[L+1][R-1] = a
                # dp[L][R] = a + b + c + d
                # d? if s[L] == s[R] d = a + 1
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                if s[i] == s[j]:
                    dp[i][j] += dp[i + 1][j - 1] + 1
        return dp[0][-1]


so = Solution()
s = 'ABA'
print(so.findWaysToDelete(s))
s = 'XXY'
print(so.findWaysToDelete(s))
s = 'aiabkbbvbaa'
print(so.findWaysToDelete(s))