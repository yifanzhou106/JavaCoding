class Solution:
    def differentstrSubsequenceDP(self, s1, s2):
        dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

        for j in range(len(s2)):
            dp[0][j] = 1 if s1[0] == s2[j] else 0

        for i in range(1, len(s1)):
            dp[i][0] = dp[i - 1][0] if s1[i] != s2[0] else dp[i - 1][0] + 1

        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                dp[i][j] = dp[i - 1][j]
                dp[i][j] = dp[i][j] + dp[i - 1][j - 1] if s1[i] == s2[j] else dp[i][j]
        return dp[-1][-1]

    def differentstrSubsequence(self, s1, s2):
        return self.process(s1, s2, len(s1) - 1, len(s2) - 1)

    def process(self, s1, s2, m, n):
        if m == 0 and n == 0:
            return 1 if s1[m] == s2[n] else 0
        if m == 0:
            return 0
        if n == 0:
            count = 0
            for i in range(m + 1):
                if s1[i] == s2[n]:
                    count += 1
            return count
        p1 = 0
        if s1[m] == s2[n]:
            p1 = self.process(s1, s2, m - 1, n - 1)
        return p1 + self.process(s1, s2, m - 1, n)


so = Solution()
s1 = 'rabbbit'
s2 = 'rabbit'

print(so.differentstrSubsequence(s1, s2))
print(so.differentstrSubsequenceDP(s1, s2))

s1 = 'aabbcc'
s2 = 'abc'

print(so.differentstrSubsequence(s1, s2))
print(so.differentstrSubsequenceDP(s1, s2))
