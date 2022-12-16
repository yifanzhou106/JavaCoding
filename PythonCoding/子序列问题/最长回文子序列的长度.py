class Solution:

    def PSubsequence(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        return self.process(s, 0, len(s) - 1, dp)

    def process(self, s, left, right, dp):
        if left == right:
            dp[left][right] = 1
            return dp[left][right]
        if left > right:
            dp[left][right] = 0
            return dp[left][right]
        if s[left] == s[right]:
            dp[left][right] = 2 + self.process(s, left + 1, right - 1, dp)
            return dp[left][right]
        dp[left][right] = max(self.process(s, left + 1, right, dp), self.process(s, left, right - 1, dp))
        return dp[left][right]

    # 从左到右的模型
    def PSubsequenceDp1(self, s):
        s2 = s[::-1]
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        dp[0][0] = 1 if s[0] == s2[0] else 0
        for i in range(1, len(s)):
            if s[i] == s2[0]:
                dp[i][0] = 1
            dp[i][0] = max(dp[i - 1][0], dp[i][0])
        for j in range(1, len(s2)):
            if s[i] == s2[0]:
                dp[0][j] = 1
            dp[0][j] = max(dp[0][j - 1], dp[0][j])

        for i in range(1, len(s)):
            for j in range(1, len(s2)):
                if s[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    # 范围尝试模型
    def PSubsequenceDp2(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s) - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 0

        for i in range(len(s) - 3, -1, -1):
            for j in range(i + 2, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


so = Solution()
s = 'aiabkbbvbaa'
print(so.PSubsequence(s))
print(so.PSubsequenceDp1(s))
print(so.PSubsequenceDp2(s))